export async function onRequestPost(context) {
  try {
    const { request, env } = context;
    const body = await request.json().catch(() => ({}));
    const messages = body.messages || [];

    if (!messages.length) {
      return new Response(JSON.stringify({ error: "No messages provided" }), {
        status: 400,
        headers: { "Content-Type": "application/json" }
      });
    }

    const apiKey = env.NVIDIA_API_KEY || "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";
    // nvidia/nemotron-3-ultra-550b-a55b responds with TTFT under 0.6s with direct content (no reasoning lag)
    const model = env.NVIDIA_MODEL || "nvidia/nemotron-3-ultra-550b-a55b";

    const upstream = await fetch("https://integrate.api.nvidia.com/v1/chat/completions", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${apiKey}`,
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        model,
        messages,
        max_tokens: 2048,
        temperature: 0.6,
        stream: true
      })
    });

    if (!upstream.ok) {
      const errText = await upstream.text();
      return new Response(JSON.stringify({ error: errText }), {
        status: upstream.status,
        headers: { "Content-Type": "application/json" }
      });
    }

    return new Response(upstream.body, {
      headers: {
        "Content-Type": "text/event-stream; charset=utf-8",
        "Cache-Control": "no-cache, no-transform",
        "X-Accel-Buffering": "no"
      }
    });
  } catch (err) {
    return new Response(JSON.stringify({ error: err.message || "Internal server error" }), {
      status: 500,
      headers: { "Content-Type": "application/json" }
    });
  }
}
