import base64

sites = [
    {"name": "stella",    "label": "Stella Mansur",             "esp": "Psicologa Clinica",   "url": "psicologastellamansur.com.br"},
    {"name": "karine",    "label": "Karine Moraes",              "esp": "Psicoterapia Online", "url": "karinemoraes.com"},
    {"name": "rafaela",   "label": "Rafaela Beloti",             "esp": "Psicologa",           "url": "psirafaelabeloti.com.br"},
    {"name": "nathalia",  "label": "Nathalia Morato",            "esp": "Psicologa",           "url": "dranathaliamorato.com.br"},
    {"name": "rosangela", "label": "Rosangela Alvim Cassimiro",  "esp": "Psicologa Clinica",   "url": "rosangelaalvimcassimiro.com"},
]

# Full-page screenshots for card body (fill entire card)
imgs = {}
for s in sites:
    with open(f"psi-fullpage/{s['name']}.png", "rb") as f:
        imgs[s["name"]] = base64.b64encode(f.read()).decode()

# Above-fold mobile shots for cover strip
cover_imgs = {}
for s in sites:
    with open(f"psi-mobile/{s['name']}.png", "rb") as f:
        cover_imgs[s["name"]] = base64.b64encode(f.read()).decode()

def card(s, i):
    return f"""<div class="card">
  <div class="card-head">
    <span class="card-num">{str(i).zfill(2)}</span>
    <div class="card-meta">
      <div class="card-name">{s['label']}</div>
      <div class="card-esp">{s['esp']}</div>
    </div>
  </div>
  <div class="card-img">
    <img src="data:image/png;base64,{imgs[s['name']]}" alt="{s['label']}">
  </div>
  <div class="card-foot">
    <span class="foot-dot"></span>
    {s['url']}
  </div>
</div>"""

pages_html = ""
for i in range(0, len(sites), 2):
    pair = sites[i:i+2]
    nums = range(i+1, i+1+len(pair))
    cards_html = "\n".join(card(s, n) for s, n in zip(pair, nums))

    if len(pair) == 1:
        cards_html = f'<div class="single-wrap">{cards_html}</div>'

    pages_html += f"""
<div class="page content-page">
  <div class="pg-header">
    <span class="pg-brand">RESULTIVA</span>
    <span class="pg-sub">Portfolio de Sites &middot; Psicologia</span>
  </div>
  <div class="cards-row">
    {cards_html}
  </div>
</div>
"""

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Catalogo Resultiva</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
*, *::before, *::after {{ margin:0; padding:0; box-sizing:border-box; }}

body {{
  font-family: 'Montserrat', sans-serif;
  background: #B8BEC8;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}}

/* === PAGE === */
.page {{
  width: 210mm;
  height: 297mm;
  background: #ffffff;
  margin: 0 auto 20px;
  box-shadow: 0 8px 48px rgba(0,0,0,.22);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  position: relative;
}}

/* === COVER === */
.cover {{
  background: linear-gradient(160deg, #0C1829 0%, #101f35 60%, #0a2240 100%);
  align-items: stretch;
  justify-content: space-between;
  padding: 52px 52px 44px;
  text-align: center;
  flex-direction: column;
}}

/* Top logo row */
.cv-topbar {{
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
}}
.cv-logo {{
  text-align: left;
}}
.cv-logo-name {{
  font-size: 11px; font-weight: 800; letter-spacing: 5px;
  color: #1EC28B; text-transform: uppercase;
}}
.cv-logo-sub {{
  font-size: 8px; font-weight: 400; letter-spacing: 3px;
  color: rgba(255,255,255,.3); margin-top: 3px; text-transform: uppercase;
}}
.cv-badge {{
  font-size: 8px; font-weight: 700; letter-spacing: 2px;
  color: #1EC28B; border: 1px solid rgba(30,194,139,.35);
  padding: 5px 12px; border-radius: 20px; text-transform: uppercase;
  align-self: center;
}}

/* Headline block */
.cv-headline {{
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 28px 0 0;
}}
.cv-title {{
  font-size: 50px; font-weight: 900; line-height: 1.0;
  color: #fff; letter-spacing: -2px;
}}
.cv-title em {{ font-style: normal; color: #1EC28B; }}
.cv-desc {{
  font-size: 12px; font-weight: 400; line-height: 1.8;
  color: rgba(255,255,255,.42); margin-top: 14px; max-width: 300px;
}}

/* thumb strip */
.cv-thumbs {{
  display: flex; gap: 10px; justify-content: center; align-items: flex-end;
  margin-top: 28px; height: 178px; overflow: hidden; flex-shrink: 0;
}}
.cv-thumb {{
  width: 64px; height: 138px;
  border-radius: 13px; overflow: hidden;
  border: 2px solid rgba(255,255,255,.1);
  flex-shrink: 0;
}}
.cv-thumb.hl {{
  width: 80px; height: 170px;
  border-color: rgba(30,194,139,.6);
  transform: translateY(-16px);
  box-shadow: 0 14px 36px rgba(0,0,0,.55);
}}
.cv-thumb img {{ width: 100%; height: 100%; object-fit: cover; object-position: top; }}

/* stats bar */
.cv-stats {{
  display: flex; gap: 0; justify-content: center;
  border-top: 1px solid rgba(255,255,255,.08);
  padding-top: 24px; margin-top: 28px; width: 100%;
}}
.cv-stat {{
  flex: 1; text-align: center;
  border-right: 1px solid rgba(255,255,255,.06);
}}
.cv-stat:last-child {{ border-right: none; }}
.cv-stat-n {{ font-size: 26px; font-weight: 900; color: #1EC28B; }}
.cv-stat-l {{
  font-size: 7px; font-weight: 600; letter-spacing: 2px;
  color: rgba(255,255,255,.28); margin-top: 3px; text-transform: uppercase;
}}

/* === CONTENT PAGE === */
.content-page {{ flex-direction: column; }}

.pg-header {{
  height: 44px;
  background: #0C1829;
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 20px;
  flex-shrink: 0;
}}
.pg-brand {{
  font-size: 9px; font-weight: 800; letter-spacing: 5px;
  color: #1EC28B; text-transform: uppercase;
}}
.pg-sub {{
  font-size: 8px; font-weight: 500; letter-spacing: 1px;
  color: rgba(255,255,255,.28);
}}

.cards-row {{
  flex: 1;
  display: flex;
  gap: 0;
  background: #DDE3EC;
  overflow: hidden;
  min-height: 0;
}}

.single-wrap {{
  flex: 1;
  display: flex;
  justify-content: center;
  background: #fff;
  padding: 0 15%;
}}

/* === CARD === */
.card {{
  flex: 1;
  display: flex;
  flex-direction: column;
  background: #fff;
  overflow: hidden;
  min-width: 0;
  border-right: 1px solid #DDE3EC;
}}
.card:last-child {{ border-right: none; }}

.card-head {{
  height: 50px;
  display: flex; align-items: center; gap: 10px;
  padding: 0 14px;
  background: #F7F9FB;
  border-bottom: 1.5px solid #DDE3EC;
  flex-shrink: 0;
}}
.card-num {{
  font-size: 13px; font-weight: 900; color: #1EC28B;
  background: rgba(30,194,139,.1);
  padding: 4px 8px; border-radius: 5px;
  flex-shrink: 0; line-height: 1;
}}
.card-meta {{ min-width: 0; overflow: hidden; }}
.card-name {{
  font-size: 11px; font-weight: 700; color: #1A2744;
  line-height: 1.2; white-space: nowrap;
  overflow: hidden; text-overflow: ellipsis;
}}
.card-esp {{
  font-size: 8px; font-weight: 500; color: #8FA3BA; margin-top: 1px;
}}

.card-img {{
  flex: 1;
  overflow: hidden;
  min-height: 0;
  position: relative;
}}
.card-img img {{
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: top center;
  display: block;
}}

.card-foot {{
  height: 28px;
  display: flex; align-items: center; gap: 6px;
  padding: 0 14px;
  background: #F7F9FB;
  border-top: 1.5px solid #DDE3EC;
  font-size: 8px; font-weight: 600; color: #6A7E92;
  letter-spacing: .3px;
  flex-shrink: 0;
}}
.foot-dot {{
  width: 5px; height: 5px; border-radius: 50%;
  background: #1EC28B; flex-shrink: 0;
}}

/* === PRINT === */
@media print {{
  body {{ background: white; }}
  .page {{
    margin: 0; box-shadow: none;
    page-break-after: always;
    width: 100%; height: 100vh;
  }}
}}
</style>
</head>
<body>

<!-- CAPA -->
<div class="page cover" style="display:flex;flex-direction:column;">
  <div class="cv-topbar">
    <div class="cv-logo">
      <div class="cv-logo-name">Resultiva</div>
      <div class="cv-logo-sub">Assessoria de Marketing</div>
    </div>
    <div class="cv-badge">Portfolio · 2025</div>
  </div>

  <div class="cv-headline">
    <h1 class="cv-title">Sites que<br><em>convertem</em><br>pacientes</h1>
    <p class="cv-desc">Portfolio de presencas digitais desenvolvidas para psicologas que querem ser encontradas e agendadas online.</p>
    <div class="cv-thumbs">
      <div class="cv-thumb"><img src="data:image/png;base64,{cover_imgs['karine']}" /></div>
      <div class="cv-thumb"><img src="data:image/png;base64,{cover_imgs['rafaela']}" /></div>
      <div class="cv-thumb hl"><img src="data:image/png;base64,{cover_imgs['stella']}" /></div>
      <div class="cv-thumb"><img src="data:image/png;base64,{cover_imgs['nathalia']}" /></div>
      <div class="cv-thumb"><img src="data:image/png;base64,{cover_imgs['rosangela']}" /></div>
    </div>
  </div>

  <div class="cv-stats">
    <div class="cv-stat">
      <div class="cv-stat-n">5</div>
      <div class="cv-stat-l">Sites</div>
    </div>
    <div class="cv-stat">
      <div class="cv-stat-n">100%</div>
      <div class="cv-stat-l">Mobile-First</div>
    </div>
    <div class="cv-stat">
      <div class="cv-stat-n">+Agenda</div>
      <div class="cv-stat-l">Foco em resultado</div>
    </div>
  </div>
</div>

{pages_html}

</body>
</html>"""

with open("catalogo-resultiva-v5.html", "w", encoding="utf-8") as f:
    f.write(html)
print("HTML v5 gerado.")
