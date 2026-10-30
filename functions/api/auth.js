// Cloudflare Pages Function: /api/auth
async function sha256(str) {
  const buf = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(str));
  return Array.from(new Uint8Array(buf)).map(b => b.toString(16).padStart(2, "0")).join("");
}

export async function onRequest(context) {
  const { request, env } = context;
  const db = env.DB;

  const url = new URL(request.url);
  const action = url.searchParams.get("action");

  if (request.method === "POST") {
    try {
      const body = await request.json();

      // Admin passcode login
      if (action === "admin" || body.password === "papercrane2026" || body.passcode === "papercrane2026") {
        if (body.passcode === "papercrane2026" || body.password === "papercrane2026") {
          return new Response(JSON.stringify({
            success: true,
            user: {
              uid: "adm_papercrane",
              email: body.email || "admin@thepapercraneacademy.com",
              name: "Faculty Staff",
              level: "Faculty",
              admin: true,
              interests: ["Law", "Politics", "International Relations", "Public Policy", "Economics"]
            }
          }), { headers: { "Content-Type": "application/json" } });
        } else {
          return new Response(JSON.stringify({ error: "Incorrect passcode" }), { status: 401, headers: { "Content-Type": "application/json" } });
        }
      }

      if (!db) {
        return new Response(JSON.stringify({ error: "D1 database not bound" }), {
          status: 500,
          headers: { "Content-Type": "application/json" }
        });
      }

      // User Registration
      if (action === "register" || action === "signup") {
        const email = (body.email || "").trim().toLowerCase();
        const name = (body.name || "Student").trim();
        const level = body.level || "Pre-university";
        const password = body.password || "";
        const interests = JSON.stringify(body.interests || ["Law", "Politics"]);

        if (!email || !password) {
          return new Response(JSON.stringify({ error: "Email and password required" }), { status: 400, headers: { "Content-Type": "application/json" } });
        }

        // Check if user already exists
        const existing = await db.prepare("SELECT uid FROM users WHERE email = ?").bind(email).first();
        if (existing) {
          return new Response(JSON.stringify({ error: "An account with this email already exists." }), { status: 409, headers: { "Content-Type": "application/json" } });
        }

        const uid = "std_" + crypto.randomUUID().slice(0, 8);
        const passHash = await sha256(password);
        const now = new Date().toISOString();

        await db.prepare(
          "INSERT INTO users (uid, email, password_hash, display_name, academic_level, interests, goals, is_admin, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, 0, ?, ?)"
        ).bind(uid, email, passHash, name, level, interests, body.goals || "", now, now).run();

        return new Response(JSON.stringify({
          success: true,
          user: {
            uid,
            email,
            name,
            level,
            interests: body.interests || ["Law", "Politics"],
            admin: false
          }
        }), { headers: { "Content-Type": "application/json" } });
      }

      // User Login
      if (action === "login") {
        const email = (body.email || "").trim().toLowerCase();
        const password = body.password || "";

        const row = await db.prepare("SELECT * FROM users WHERE email = ?").bind(email).first();
        if (!row) {
          return new Response(JSON.stringify({ error: "No account found with this email." }), { status: 404, headers: { "Content-Type": "application/json" } });
        }

        const passHash = await sha256(password);
        if (row.password_hash && row.password_hash !== passHash) {
          return new Response(JSON.stringify({ error: "Incorrect password." }), { status: 401, headers: { "Content-Type": "application/json" } });
        }

        let interests = [];
        try { interests = JSON.parse(row.interests || "[]"); } catch(e){}

        return new Response(JSON.stringify({
          success: true,
          user: {
            uid: row.uid,
            email: row.email,
            name: row.display_name,
            level: row.academic_level,
            interests,
            admin: row.is_admin === 1
          }
        }), { headers: { "Content-Type": "application/json" } });
      }

    } catch (e) {
      return new Response(JSON.stringify({ error: e.message || "Server error" }), { status: 500, headers: { "Content-Type": "application/json" } });
    }
  }

  return new Response(JSON.stringify({ error: "Invalid request" }), { status: 400, headers: { "Content-Type": "application/json" } });
}
