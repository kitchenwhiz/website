/* Assembly animation for 3D line renders.
   Markup: <figure class="assemble" data-cuts='[[x,yTop],...]' data-k="0.3" data-labels='["A","B",...]'>
             <div class="asm-stage"><img src="..." width="W" height="H"></div><figcaption>...</figcaption></figure>
   Each cut is a module boundary: a vertical edge at x from the floor up to yTop, then a depth line up-right with slope k.
   Without JS (or with reduced motion) the plain image shows. */
(function () {
  if (!("IntersectionObserver" in window) || !Element.prototype.animate) return;
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function boundary(x, yt, k, W, H) {
    return [[x, H + 40], [x, yt], [x + k * (yt + 40), -40]];
  }
  const pct = (p, W, H) => `${(p[0] / W * 100).toFixed(2)}% ${(p[1] / H * 100).toFixed(2)}%`;

  function build(fig) {
    const stage = fig.querySelector(".asm-stage");
    const img = stage.querySelector("img");
    const W = +img.getAttribute("width"), H = +img.getAttribute("height");
    const k = parseFloat(fig.dataset.k || "0.3");
    const cuts = JSON.parse(fig.dataset.cuts || "[]");
    const labels = JSON.parse(fig.dataset.labels || "[]");
    const bounds = [boundary(-400, 0, 0, W, H)]
      .concat(cuts.map(c => boundary(c[0], c[1], k, W, H)))
      .concat([boundary(W + 400, 0, 0, W, H)]);
    const pieces = [];
    for (let i = 0; i < bounds.length - 1; i++) {
      const a = bounds[i], b = bounds[i + 1];
      const poly = [a[0], a[1], a[2], b[2], b[1], b[0]].map(p => pct(p, W, H)).join(",");
      const el = document.createElement("div");
      el.className = "asm-piece";
      el.style.backgroundImage = `url("${img.currentSrc || img.src}")`;
      el.style.clipPath = `polygon(${poly})`;
      stage.appendChild(el);
      // label anchor: middle of the module's front face
      const left = i === 0 ? Math.max(0, cuts[0] ? cuts[0][0] - 140 : 0) : cuts[i - 1][0];
      const right = i < cuts.length ? cuts[i][0] : Math.min(W, left + 180);
      const yt = (cuts[i] || cuts[i - 1] || [0, H * 0.45])[1];
      pieces.push({ el, cx: (left + right) / 2, yt, label: labels[i] });
    }
    const shine = document.createElement("div");
    shine.className = "asm-shine";
    stage.appendChild(shine);
    const tags = [];
    pieces.forEach((p, i) => {
      if (!p.label) return;
      const t = document.createElement("span");
      t.className = "asm-tag";
      t.textContent = p.label;
      t.style.left = (p.cx / W * 100) + "%";
      t.style.top = (Math.min(p.yt + (i % 2 ? 125 : 70), H * 0.86) / H * 100) + "%";
      stage.appendChild(t);
      tags.push(t);
    });
    fig.classList.add("asm-ready");
    return { pieces, shine, tags, W };
  }

  function play(fig, parts) {
    const { pieces, shine, tags, W } = parts;
    fig.classList.remove("asm-done");
    fig.classList.add("asm-playing");
    const n = pieces.length;
    const order = pieces.map((_, i) => i);
    const stagger = 170, dur = 900;
    const anims = order.map((i, step) => {
      const p = pieces[i];
      const fromLeft = p.cx < W / 2;
      const dx = (fromLeft ? -1 : 1) * (60 + Math.random() * 120);
      const dy = -(140 + Math.random() * 160);
      const rot = (fromLeft ? -1 : 1) * (4 + Math.random() * 6);
      return p.el.animate([
        { transform: `translate(${dx}px, ${dy}px) rotate(${rot}deg) scale(.92)`, opacity: 0 },
        { opacity: 1, offset: 0.35 },
        { transform: "translate(0, 6px) rotate(0) scale(1.01)", offset: 0.82 },
        { transform: "translate(0,0) rotate(0) scale(1)", opacity: 1 }
      ], { duration: dur, delay: 250 + step * stagger, easing: "cubic-bezier(.2,.8,.2,1)", fill: "both" });
    });
    const landed = 250 + (n - 1) * stagger + dur;
    shine.animate([{ transform: "translateX(-120%)", opacity: 0 }, { opacity: 1, offset: .2 }, { opacity: 1, offset: .8 }, { transform: "translateX(120%)", opacity: 0 }],
      { duration: 1100, delay: landed, easing: "ease-in-out", fill: "both" });
    tags.forEach((t, i) => t.animate([{ opacity: 0, transform: "translate(-50%, 8px)" }, { opacity: 1, transform: "translate(-50%, 0)" }],
      { duration: 380, delay: landed + 500 + i * 110, easing: "ease-out", fill: "both" }));
    setTimeout(() => { fig.classList.add("asm-done"); fig.classList.remove("asm-playing"); }, landed + 600);
    return anims;
  }

  function setup(fig) {
    const img = fig.querySelector(".asm-stage img");
    const go = () => {
      const parts = build(fig);
      if (reduce) { fig.classList.add("asm-done"); parts.tags.forEach(t => t.style.opacity = 1); return; }
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "asm-replay";
      btn.textContent = "↻ Replay";
      btn.addEventListener("click", () => play(fig, parts));
      fig.querySelector(".asm-stage").appendChild(btn);
      const io = new IntersectionObserver(es => {
        if (es.some(e => e.isIntersecting)) { io.disconnect(); play(fig, parts); }
      }, { threshold: 0.35 });
      io.observe(fig);
    };
    if (img.complete && img.naturalWidth) go(); else img.addEventListener("load", go, { once: true });
  }

  document.querySelectorAll("figure.assemble").forEach(setup);
})();
