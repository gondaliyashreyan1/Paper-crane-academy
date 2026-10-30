// Cloudflare Pages Function: /api/db
export async function onRequest(context) {
  const { request, env } = context;
  const db = env.DB;

  if (!db) {
    return new Response(JSON.stringify({ error: "D1 database not bound" }), {
      status: 500,
      headers: { "Content-Type": "application/json" }
    });
  }

  const url = new URL(request.url);
  const col = url.searchParams.get("col");
  const uid = url.searchParams.get("uid");

  // GET data
  if (request.method === "GET") {
    try {
      // 1. Fetch Events
      if (col === "events") {
        const rows = await db.prepare("SELECT * FROM events ORDER BY date ASC").all();
        const events = (rows.results || []).map(r => ({
          id: r.id,
          title: r.title,
          type: r.type,
          date: r.date,
          time: r.time,
          location: r.location,
          capacity: r.capacity,
          deadline: r.deadline,
          description: r.description,
          instructions: r.instructions,
          registration: r.registration_open === 1,
          featured: r.featured === 1
        }));
        return new Response(JSON.stringify({ success: true, events }), { headers: { "Content-Type": "application/json" } });
      }

      // 2. Fetch Published Articles
      if (col === "articles") {
        const rows = await db.prepare("SELECT * FROM articles WHERE status = 'published' ORDER BY date DESC").all();
        const articles = (rows.results || []).map(r => {
          let sources = [];
          try { sources = JSON.parse(r.sources || "[]"); } catch(e){}
          return {
            id: r.id,
            title: r.title,
            subtitle: r.subtitle,
            category: r.category,
            kind: r.kind,
            authorName: r.author_name || "PaperCrane AI",
            body: r.body,
            sources,
            date: r.date,
            publishAt: r.publish_at,
            featured: r.featured === 1,
            correction: r.correction
          };
        });
        return new Response(JSON.stringify({ success: true, articles }), { headers: { "Content-Type": "application/json" } });
      }

      // 3. Fetch Admin Submissions
      if (col === "submissions") {
        const rows = await db.prepare("SELECT * FROM articles WHERE status != 'published' ORDER BY updated_at DESC").all();
        const subs = (rows.results || []).map(r => {
          let sources = [];
          try { sources = JSON.parse(r.sources || "[]"); } catch(e){}
          return {
            id: r.id,
            aid: r.id,
            uid: r.author_id,
            author: r.author_name,
            title: r.title,
            subtitle: r.subtitle,
            category: r.category,
            kind: r.kind,
            body: r.body,
            sources,
            status: r.status,
            editorNote: r.editor_note,
            updatedAt: r.updated_at
          };
        });
        return new Response(JSON.stringify({ success: true, submissions: subs }), { headers: { "Content-Type": "application/json" } });
      }

      // 4. Fetch User Progress & Data
      if (uid) {
        const progRows = await db.prepare("SELECT * FROM user_progress WHERE user_id = ?").bind(uid).all();
        const progress = { courses: {} };
        for (const p of progRows.results || []) {
          let done = {}, scores = {};
          try { done = JSON.parse(p.done_lessons || "{}"); } catch(e){}
          try { scores = JSON.parse(p.scores || "{}"); } catch(e){}
          progress.courses[p.course_id] = {
            done,
            scores,
            started: p.started_at,
            last: p.last_lesson
          };
        }

        const savedRows = await db.prepare("SELECT * FROM user_saved WHERE user_id = ?").bind(uid).all();
        const saved = { opps: {}, articles: {}, courses: {} };
        for (const s of savedRows.results || []) {
          if (!saved[s.kind]) saved[s.kind] = {};
          saved[s.kind][s.target_id] = s.saved_at;
        }

        const subRows = await db.prepare("SELECT * FROM articles WHERE author_id = ?").bind(uid).all();
        const userArticles = {};
        for (const a of subRows.results || []) {
          let sources = [];
          try { sources = JSON.parse(a.sources || "[]"); } catch(e){}
          userArticles[a.id] = {
            title: a.title,
            subtitle: a.subtitle,
            category: a.category,
            kind: a.kind,
            body: a.body,
            sources,
            status: a.status,
            editorNote: a.editor_note,
            updatedAt: a.updated_at
          };
        }

        const certRows = await db.prepare("SELECT * FROM certificates WHERE user_id = ?").bind(uid).all();
        const certs = (certRows.results || []).map(c => ({
          id: c.id,
          userId: c.user_id,
          studentName: c.student_name,
          courseId: c.course_id,
          courseTitle: c.course_title,
          issuedAt: c.issued_at,
          status: c.status
        }));

        return new Response(JSON.stringify({
          success: true,
          progress,
          saved,
          submissions: { articles: userArticles },
          certificates: certs
        }), { headers: { "Content-Type": "application/json" } });
      }

      return new Response(JSON.stringify({ error: "Missing collection or uid" }), { status: 400, headers: { "Content-Type": "application/json" } });
    } catch(e) {
      return new Response(JSON.stringify({ error: e.message }), { status: 500, headers: { "Content-Type": "application/json" } });
    }
  }

  // POST (Mutation / Write)
  if (request.method === "POST") {
    try {
      const body = await request.json();
      const action = body.action || url.searchParams.get("action");
      const now = new Date().toISOString();

      // Schedule or update an event
      if (action === "save-event") {
        const ev = body.event;
        await db.prepare(
          "INSERT INTO events (id, title, type, date, time, location, capacity, deadline, description, instructions, registration_open, created_at, updated_at) " +
          "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) " +
          "ON CONFLICT(id) DO UPDATE SET title=excluded.title, type=excluded.type, date=excluded.date, time=excluded.time, location=excluded.location, capacity=excluded.capacity, deadline=excluded.deadline, description=excluded.description, instructions=excluded.instructions, registration_open=excluded.registration_open, updated_at=excluded.updated_at"
        ).bind(
          ev.id, ev.title, ev.type, ev.date, ev.time || "", ev.location || "Online",
          ev.capacity ? +ev.capacity : null, ev.deadline || "", ev.description || "",
          ev.instructions || "", ev.registration ? 1 : 0, now, now
        ).run();
        return new Response(JSON.stringify({ success: true, id: ev.id }), { headers: { "Content-Type": "application/json" } });
      }

      // Delete an event
      if (action === "delete-event") {
        await db.prepare("DELETE FROM events WHERE id = ?").bind(body.id).run();
        return new Response(JSON.stringify({ success: true }), { headers: { "Content-Type": "application/json" } });
      }

      // Save student article draft or submission
      if (action === "save-article") {
        const a = body.article;
        const uid = body.uid;
        await db.prepare(
          "INSERT INTO articles (id, title, subtitle, category, kind, author_name, author_id, body, sources, status, editor_note, publish_at, date, created_at, updated_at) " +
          "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) " +
          "ON CONFLICT(id) DO UPDATE SET title=excluded.title, subtitle=excluded.subtitle, category=excluded.category, kind=excluded.kind, author_name=excluded.author_name, body=excluded.body, sources=excluded.sources, status=excluded.status, editor_note=excluded.editor_note, publish_at=excluded.publish_at, date=excluded.date, updated_at=excluded.updated_at"
        ).bind(
          a.id, a.title, a.subtitle || "", a.category, a.kind, a.authorName || body.authorName || "PaperCrane AI",
          uid, a.body, JSON.stringify(a.sources || []), a.status || "draft",
          a.editorNote || "", a.publishAt || a.date || "", a.date || "", now, now
        ).run();
        return new Response(JSON.stringify({ success: true, id: a.id }), { headers: { "Content-Type": "application/json" } });
      }

      // Save user course progress
      if (action === "save-progress") {
        const { uid, courseId, done, scores, started, last } = body;
        await db.prepare(
          "INSERT INTO user_progress (user_id, course_id, done_lessons, scores, started_at, last_lesson, updated_at) " +
          "VALUES (?, ?, ?, ?, ?, ?, ?) " +
          "ON CONFLICT(user_id, course_id) DO UPDATE SET done_lessons=excluded.done_lessons, scores=excluded.scores, last_lesson=excluded.last_lesson, updated_at=excluded.updated_at"
        ).bind(
          uid, courseId, JSON.stringify(done || {}), JSON.stringify(scores || {}), started || "", last || "", now
        ).run();
        return new Response(JSON.stringify({ success: true }), { headers: { "Content-Type": "application/json" } });
      }

      // Toggle saved item
      if (action === "toggle-saved") {
        const { uid, kind, targetId, saved } = body;
        if (saved) {
          await db.prepare("INSERT OR REPLACE INTO user_saved (user_id, kind, target_id, saved_at) VALUES (?, ?, ?, ?)").bind(uid, kind, targetId, now).run();
        } else {
          await db.prepare("DELETE FROM user_saved WHERE user_id = ? AND kind = ? AND target_id = ?").bind(uid, kind, targetId).run();
        }
        return new Response(JSON.stringify({ success: true }), { headers: { "Content-Type": "application/json" } });
      }

      // Issue Certificate
      if (action === "issue-cert") {
        const { certId, userId, studentName, courseId, courseTitle, score } = body;
        await db.prepare(
          "INSERT INTO certificates (id, user_id, student_name, course_id, course_title, score, issued_at, issuer, status) VALUES (?, ?, ?, ?, ?, ?, ?, 'The Paper Crane Academy', 'valid')"
        ).bind(certId, userId, studentName, courseId, courseTitle, score || 100, now.slice(0, 10)).run();
        return new Response(JSON.stringify({ success: true, certId }), { headers: { "Content-Type": "application/json" } });
      }

      return new Response(JSON.stringify({ error: "Unknown action" }), { status: 400, headers: { "Content-Type": "application/json" } });
    } catch(e) {
      return new Response(JSON.stringify({ error: e.message }), { status: 500, headers: { "Content-Type": "application/json" } });
    }
  }

  return new Response(JSON.stringify({ error: "Method not allowed" }), { status: 405, headers: { "Content-Type": "application/json" } });
}
