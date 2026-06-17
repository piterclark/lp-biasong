import base64

sites = [
    {"name": "stella",    "label": "Stella Mansur",             "esp": "Psicologa Clinica",   "url": "psicologastellamansur.com.br"},
    {"name": "karine",    "label": "Karine Moraes",              "esp": "Psicoterapia Online", "url": "karinemoraes.com"},
    {"name": "rafaela",   "label": "Rafaela Beloti",             "esp": "Psicologa",           "url": "psirafaelabeloti.com.br"},
    {"name": "nathalia",  "label": "Nathalia Morato",            "esp": "Psicologa",           "url": "dranathaliamorato.com.br"},
    {"name": "rosangela", "label": "Rosangela Alvim Cassimiro",  "esp": "Psicologa Clinica",   "url": "rosangelaalvimcassimiro.com"},
]

imgs = {}
for s in sites:
    with open(f"psi-mobile/{s['name']}.png", "rb") as f:
        imgs[s["name"]] = base64.b64encode(f.read()).decode()

def card(s, i):
    return f"""<div class="card">
  <div class="card-head">
    <span class="card-num">{str(i).zfill(2)}</span>
    <div>
      <div class="card-name">{s['label']}</div>
      <div class="card-esp">{s['esp']}</div>
    </div>
  </div>
  <div class="card-img">
    <img src="data:image/png;base64,{imgs[s['name']]}" alt="{s['label']}">
  </div>
  <div class="card-foot">{s['url']}</div>
</div>"""

# group into pairs
pages_html = ""
for i in range(0, len(sites), 2):
    pair = sites[i:i+2]
    nums = range(i+1, i+1+len(pair))
    cards_html = "\n".join(card(s, n) for s, n in zip(pair, nums))

    # if only 1 site in this page, wrap it centered
    if len(pair) == 1:
        cards_html = f'<div class="single-wrap">{cards_html}</div>'

    pages_html += f"""
<div class="page content-page">
  <div class="pg-header">
    <span class="pg-brand">RESULTIVA</span>
    <span class="pg-sub">Portfolio de Sites · Psicologia</span>
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
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<style>
*, *::before, *::after {{ margin:0; padding:0; box-sizing:border-box; }}

body {{
  font-family: 'Montserrat', sans-serif;
  background: #C8CDD6;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}}

/* === PAGE === */
.page {{
  width: 210mm;
  height: 297mm;
  background: #ffffff;
  margin: 0 auto 20px;
  box-shadow: 0 4px 32px rgba(0,0,0,.18);
  overflow: hidden;
  display: flex;
  flex-direction: column;
}}

/* === COVER === */
.cover {{
  background: #0C1829;
  align-items: center;
  justify-content: space-between;
  padding: 56px 52px 44px;
  text-align: center;
}}
.cv-logo {{
  font-size: 11px; font-weight: 800; letter-spacing: 5px;
  color: #1EC28B; text-transform: uppercase; align-self: flex-start;
}}
.cv-logo span {{ display:block; font-size:8px; font-weight:400; letter-spacing:3px; color:rgba(255,255,255,.3); margin-top:3px; }}
.cv-title {{
  font-size: 46px; font-weight: 900; line-height: 1.05;
  color: #fff; letter-spacing: -1.5px;
}}
.cv-title em {{ font-style:normal; color:#1EC28B; }}
.cv-desc {{
  font-size: 13px; font-weight: 400; line-height: 1.8;
  color: rgba(255,255,255,.4); margin-top:16px;
}}

/* thumb strip on cover */
.cv-thumbs {{
  display:flex; gap:10px; justify-content:center; align-items:flex-end;
  margin-top:36px; height:190px; overflow:hidden;
}}
.cv-thumb {{
  width:66px; height:145px;
  border-radius:12px; overflow:hidden;
  border:3px solid rgba(255,255,255,.1);
  flex-shrink:0;
}}
.cv-thumb.hl {{
  width:82px; height:180px;
  border-color: rgba(30,194,139,.5);
  transform: translateY(-18px);
  box-shadow: 0 12px 32px rgba(0,0,0,.5);
}}
.cv-thumb img {{ width:100%; height:100%; object-fit:cover; object-position:top; }}

.cv-stats {{
  display:flex; gap:48px; justify-content:center;
  border-top:1px solid rgba(255,255,255,.08);
  padding-top:28px; margin-top:36px; width:100%;
}}
.cv-stat-n {{ font-size:28px; font-weight:900; color:#1EC28B; }}
.cv-stat-l {{ font-size:8px; font-weight:600; letter-spacing:2px; color:rgba(255,255,255,.28); margin-top:3px; text-transform:uppercase; }}

/* === CONTENT PAGE === */
.content-page {{ flex-direction:column; }}

.pg-header {{
  height: 46px;
  background: #0C1829;
  display:flex; align-items:center; justify-content:space-between;
  padding: 0 22px;
  flex-shrink:0;
}}
.pg-brand {{
  font-size:10px; font-weight:800; letter-spacing:4px;
  color:#1EC28B; text-transform:uppercase;
}}
.pg-sub {{
  font-size:9px; font-weight:500; letter-spacing:1px;
  color:rgba(255,255,255,.3);
}}

.cards-row {{
  flex:1;
  display:flex;
  gap:2px;
  background:#E2E8F0;
  overflow:hidden;
}}

.single-wrap {{
  flex:1;
  display:flex;
  justify-content:center;
  background:#fff;
  padding:0 15%;
}}

/* === CARD === */
.card {{
  flex:1;
  display:flex;
  flex-direction:column;
  background:#fff;
  overflow:hidden;
  min-width:0;
}}

.card-head {{
  height: 46px;
  display:flex; align-items:center; gap:10px;
  padding: 0 14px;
  background:#F4F6FA;
  border-bottom:1px solid #DDE3EC;
  flex-shrink:0;
}}
.card-num {{
  font-size:12px; font-weight:900; color:#1EC28B;
  background:rgba(30,194,139,.1);
  padding:3px 7px; border-radius:4px;
  flex-shrink:0;
}}
.card-name {{ font-size:11px; font-weight:700; color:#1A2744; line-height:1.2; }}
.card-esp  {{ font-size:8px;  font-weight:500; color:#8FA3BA; margin-top:1px; }}

.card-img {{
  flex:1;
  overflow:hidden;
  background:#f0f0f0;
}}
.card-img img {{
  width:100%;
  height:auto;
  display:block;
}}

.card-foot {{
  height: 30px;
  display:flex; align-items:center;
  padding: 0 14px;
  background:#F4F6FA;
  border-top:1px solid #DDE3EC;
  font-size:8px; font-weight:600; color:#5A6A7E;
  letter-spacing:.3px;
  flex-shrink:0;
}}

/* === PRINT === */
@media print {{
  body {{ background:white; }}
  .page {{
    margin:0; box-shadow:none;
    page-break-after:always;
    width:100%; height:100vh;
  }}
}}
</style>
</head>
<body>

<!-- CAPA -->
<div class="page cover" style="display:flex;flex-direction:column;">
  <div class="cv-logo">Resultiva <span>Assessoria de Marketing</span></div>

  <div>
    <h1 class="cv-title">Sites que<br><em>convertem</em><br>pacientes</h1>
    <p class="cv-desc">Portfolio de presencas digitais para psicologas<br>que querem ser encontradas e escolhidas online.</p>
    <div class="cv-thumbs">
      <div class="cv-thumb"><img src="data:image/png;base64,{imgs['karine']}" /></div>
      <div class="cv-thumb"><img src="data:image/png;base64,{imgs['rafaela']}" /></div>
      <div class="cv-thumb hl"><img src="data:image/png;base64,{imgs['stella']}" /></div>
      <div class="cv-thumb"><img src="data:image/png;base64,{imgs['nathalia']}" /></div>
      <div class="cv-thumb"><img src="data:image/png;base64,{imgs['rosangela']}" /></div>
    </div>
  </div>

  <div class="cv-stats">
    <div><div class="cv-stat-n">5</div><div class="cv-stat-l">Sites</div></div>
    <div><div class="cv-stat-n">100%</div><div class="cv-stat-l">Mobile</div></div>
    <div><div class="cv-stat-n">+Agenda</div><div class="cv-stat-l">Objetivo</div></div>
  </div>
</div>

{pages_html}

</body>
</html>"""

with open("catalogo-resultiva-v4.html", "w", encoding="utf-8") as f:
    f.write(html)
print("HTML v4 gerado.")
