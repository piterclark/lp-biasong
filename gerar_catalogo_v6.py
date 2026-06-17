import base64, struct, math

def png_size(path):
    with open(path, 'rb') as f:
        f.read(8); f.read(4); f.read(4)
        w = struct.unpack('>I', f.read(4))[0]
        h = struct.unpack('>I', f.read(4))[0]
    return w, h

sites = [
    {"name": "stella",    "label": "Stella Mansur",            "esp": "Psicologa Clinica",   "url": "psicologastellamansur.com.br"},
    {"name": "karine",    "label": "Karine Moraes",             "esp": "Psicoterapia Online", "url": "karinemoraes.com"},
    {"name": "rafaela",   "label": "Rafaela Beloti",            "esp": "Psicologa",           "url": "psirafaelabeloti.com.br"},
    {"name": "nathalia",  "label": "Nathalia Morato",           "esp": "Psicologa",           "url": "dranathaliamorato.com.br"},
    {"name": "rosangela", "label": "Rosangela Alvim Cassimiro", "esp": "Psicologa Clinica",   "url": "rosangelaalvimcassimiro.com"},
]

imgs = {}
dims = {}
for s in sites:
    path = f"psi-fullpage/{s['name']}.png"
    dims[s['name']] = png_size(path)
    with open(path, 'rb') as f:
        imgs[s['name']] = base64.b64encode(f.read()).decode()

cover_imgs = {}
for s in sites:
    with open(f"psi-mobile/{s['name']}.png", 'rb') as f:
        cover_imgs[s['name']] = base64.b64encode(f.read()).decode()

# A4 at 96 dpi
PAGE_W_PX = 794
PAGE_H_PX = 1122
HEADER_H  = 44
CONTENT_H = PAGE_H_PX - HEADER_H   # 1078 px per page

def site_pages_html(s, site_idx):
    orig_w, orig_h = dims[s['name']]
    scale          = PAGE_W_PX / orig_w
    displayed_h    = math.ceil(orig_h * scale)
    n_pages        = math.ceil(displayed_h / CONTENT_H)
    b64            = imgs[s['name']]
    num            = str(site_idx).zfill(2)

    parts = []
    for i in range(n_pages):
        offset = i * CONTENT_H
        parts.append(f"""<div class="page site-page">
  <div class="sp-header">
    <div class="sp-left">
      <span class="sp-num">{num}</span>
      <span class="sp-name">{s['label']}</span>
      <span class="sp-sep">&middot;</span>
      <span class="sp-esp">{s['esp']}</span>
    </div>
    <div class="sp-right">
      <span class="sp-brand">RESULTIVA</span>
      <span class="sp-pag">{i+1} / {n_pages}</span>
    </div>
  </div>
  <div class="sp-content">
    <img src="data:image/png;base64,{b64}"
         style="width:100%;height:auto;display:block;margin-top:-{offset}px">
  </div>
</div>""")
    return '\n'.join(parts)

all_pages = '\n'.join(site_pages_html(s, i+1) for i, s in enumerate(sites))

# ── cover thumbnail strip ──────────────────────────────────────────────────
cover_strip = ''.join(
    f'<div class="cv-thumb{" hl" if s["name"]=="stella" else ""}">'
    f'<img src="data:image/png;base64,{cover_imgs[s["name"]]}" /></div>'
    for s in sites
)

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Catalogo Resultiva - Portfolio Psicologia</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{{margin:0;padding:0;box-sizing:border-box;}}

body{{
  font-family:'Montserrat',sans-serif;
  background:#B0B8C4;
  -webkit-print-color-adjust:exact;
  print-color-adjust:exact;
}}

/* ── PAGE ── */
.page{{
  width:210mm;
  height:297mm;
  background:#fff;
  margin:0 auto 20px;
  box-shadow:0 8px 48px rgba(0,0,0,.22);
  overflow:hidden;
  display:flex;
  flex-direction:column;
  position:relative;
}}

/* ══════════════════════════════
   CAPA
══════════════════════════════ */
.cover{{
  background: linear-gradient(170deg,#0a1624 0%,#0d1f38 55%,#091830 100%);
  flex-direction:column;
  padding:52px 52px 44px;
}}

.cv-topbar{{
  display:flex;align-items:flex-start;justify-content:space-between;
}}
.cv-logo-name{{
  font-size:11px;font-weight:800;letter-spacing:5px;
  color:#1EC28B;text-transform:uppercase;
}}
.cv-logo-sub{{
  font-size:8px;font-weight:400;letter-spacing:3px;
  color:rgba(255,255,255,.3);margin-top:3px;text-transform:uppercase;
}}
.cv-badge{{
  font-size:8px;font-weight:700;letter-spacing:2px;
  color:#1EC28B;border:1px solid rgba(30,194,139,.35);
  padding:5px 13px;border-radius:20px;text-transform:uppercase;
  align-self:center;
}}

.cv-headline{{
  flex:1;display:flex;flex-direction:column;
  align-items:center;justify-content:center;
  text-align:center;padding:24px 0 0;
}}
.cv-tag{{
  font-size:8px;font-weight:700;letter-spacing:3px;
  color:#1EC28B;text-transform:uppercase;
  border:1px solid rgba(30,194,139,.25);
  padding:5px 14px;border-radius:20px;margin-bottom:20px;
  display:inline-block;
}}
.cv-title{{
  font-size:50px;font-weight:900;line-height:1.0;
  color:#fff;letter-spacing:-2px;
}}
.cv-title em{{font-style:normal;color:#1EC28B;}}
.cv-desc{{
  font-size:12px;font-weight:400;line-height:1.8;
  color:rgba(255,255,255,.4);margin-top:14px;max-width:290px;
}}

/* phone strip */
.cv-thumbs{{
  display:flex;gap:10px;justify-content:center;align-items:flex-end;
  margin-top:26px;height:170px;overflow:hidden;flex-shrink:0;
}}
.cv-thumb{{
  width:62px;height:132px;border-radius:12px;overflow:hidden;
  border:2px solid rgba(255,255,255,.1);flex-shrink:0;
}}
.cv-thumb.hl{{
  width:78px;height:165px;
  border-color:rgba(30,194,139,.6);
  transform:translateY(-16px);
  box-shadow:0 14px 36px rgba(0,0,0,.55);
}}
.cv-thumb img{{width:100%;height:100%;object-fit:cover;object-position:top;}}

/* stats */
.cv-stats{{
  display:flex;justify-content:center;
  border-top:1px solid rgba(255,255,255,.07);
  padding-top:22px;margin-top:24px;
}}
.cv-stat{{flex:1;text-align:center;border-right:1px solid rgba(255,255,255,.06);}}
.cv-stat:last-child{{border-right:none;}}
.cv-stat-n{{font-size:24px;font-weight:900;color:#1EC28B;}}
.cv-stat-l{{
  font-size:7px;font-weight:600;letter-spacing:2px;
  color:rgba(255,255,255,.28);margin-top:3px;text-transform:uppercase;
}}

/* ══════════════════════════════
   SITE PAGES
══════════════════════════════ */
.site-page{{flex-direction:column;}}

.sp-header{{
  height:{HEADER_H}px;
  background:#0C1829;
  display:flex;align-items:center;justify-content:space-between;
  padding:0 18px;flex-shrink:0;
}}
.sp-left{{display:flex;align-items:center;gap:8px;}}
.sp-num{{
  font-size:10px;font-weight:900;color:#1EC28B;
  background:rgba(30,194,139,.12);
  padding:3px 7px;border-radius:4px;flex-shrink:0;
}}
.sp-name{{font-size:10px;font-weight:700;color:#fff;white-space:nowrap;}}
.sp-sep{{color:rgba(255,255,255,.2);}}
.sp-esp{{font-size:8px;font-weight:400;color:rgba(255,255,255,.38);}}
.sp-right{{display:flex;align-items:center;gap:10px;}}
.sp-brand{{
  font-size:8px;font-weight:800;letter-spacing:4px;
  color:#1EC28B;text-transform:uppercase;
}}
.sp-pag{{
  font-size:8px;font-weight:500;
  color:rgba(255,255,255,.28);
}}

.sp-content{{
  flex:1;
  overflow:hidden;
  min-height:0;
  background:#fff;
}}

/* ── PRINT ── */
@media print{{
  body{{background:white;}}
  .page{{
    margin:0;box-shadow:none;
    page-break-after:always;
    width:100%;height:100vh;
  }}
}}
</style>
</head>
<body>

<!-- CAPA -->
<div class="page cover">
  <div class="cv-topbar">
    <div>
      <div class="cv-logo-name">Resultiva</div>
      <div class="cv-logo-sub">Assessoria de Marketing</div>
    </div>
    <div class="cv-badge">Portfolio &middot; Psicologia</div>
  </div>

  <div class="cv-headline">
    <div class="cv-tag">5 sites reais de clientes</div>
    <h1 class="cv-title">Sites que<br><em>convertem</em><br>pacientes</h1>
    <p class="cv-desc">Presenças digitais desenvolvidas para psicólogas que querem ser encontradas e escolhidas online.</p>
    <div class="cv-thumbs">
      {cover_strip}
    </div>
  </div>

  <div class="cv-stats">
    <div class="cv-stat">
      <div class="cv-stat-n">5</div>
      <div class="cv-stat-l">Sites reais</div>
    </div>
    <div class="cv-stat">
      <div class="cv-stat-n">100%</div>
      <div class="cv-stat-l">Mobile-first</div>
    </div>
    <div class="cv-stat">
      <div class="cv-stat-n">+Agenda</div>
      <div class="cv-stat-l">Objetivo</div>
    </div>
  </div>
</div>

{all_pages}

</body>
</html>"""

out = "catalogo-resultiva-v6.html"
with open(out, "w", encoding="utf-8") as f:
    f.write(html)

print(f"HTML v6 gerado: {out}")
print("Paginas por site:")
total = 0
for i, s in enumerate(sites, 1):
    orig_w, orig_h = dims[s['name']]
    scale = PAGE_W_PX / orig_w
    n = math.ceil(math.ceil(orig_h * scale) / CONTENT_H)
    total += n
    print(f"  {i}. {s['label']}: {n} paginas")
print(f"Total: 1 capa + {total} conteudo = {total+1} paginas")
