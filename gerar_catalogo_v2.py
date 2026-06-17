import base64

sites = [
    {"name": "stella",    "label": "Stella Mansur",            "esp": "Psicologa Clinica",       "url": "https://psicologastellamansur.com.br/"},
    {"name": "karine",    "label": "Karine Moraes",             "esp": "Psicoterapia Online",     "url": "https://karinemoraes.com/lp/psicoterapia-online/"},
    {"name": "rafaela",   "label": "Rafaela Beloti",            "esp": "Psicologa",               "url": "https://psirafaelabeloti.com.br/"},
    {"name": "nathalia",  "label": "Nathalia Morato",           "esp": "Psicologa",               "url": "https://dranathaliamorato.com.br/"},
    {"name": "rosangela", "label": "Rosangela Alvim Cassimiro", "esp": "Psicologa Clinica",       "url": "https://rosangelaalvimcassimiro.com/"},
]

imgs = {}
for s in sites:
    with open(f"psi-mobile/{s['name']}.png", "rb") as f:
        imgs[s["name"]] = base64.b64encode(f.read()).decode()

def site_page(s, i):
    num = str(i).zfill(2)
    domain = s["url"].replace("https://","").replace("http://","").rstrip("/")
    return f"""
<div class="page site-page">

  <div class="top-bar">
    <span class="top-num">{num} <span class="top-sep">/</span> 05</span>
    <span class="top-brand">RESULTIVA</span>
  </div>

  <div class="site-body">

    <div class="phone-col">
      <a href="{s['url']}" target="_blank" class="phone-link">
        <div class="phone-wrap">
          <div class="phone-frame">
            <div class="phone-notch"></div>
            <div class="phone-screen">
              <img src="data:image/png;base64,{imgs[s['name']]}" alt="{s['label']}" />
            </div>
            <div class="phone-bar"></div>
          </div>
          <div class="phone-shadow"></div>
        </div>
        <div class="tap-hint">Toque para visitar</div>
      </a>
    </div>

    <div class="info-col">
      <div class="info-inner">
        <div class="info-tag">Portfolio Resultiva</div>
        <h2 class="info-name">{s['label']}</h2>
        <p class="info-esp">{s['esp']}</p>
        <div class="info-divider"></div>
        <p class="info-desc">
          Presenca digital profissional desenvolvida para
          atrair e converter pacientes online.
        </p>
        <a href="{s['url']}" target="_blank" class="info-btn">
          Acessar site &#8599;
        </a>
        <div class="info-url">{domain}</div>
      </div>
    </div>

  </div>

  <div class="page-footer">
    <span>Resultiva &mdash; Assessoria de Marketing</span>
    <span>Todos os sites sao clicaveis</span>
  </div>

</div>
"""

cards = "".join(site_page(s, i) for i, s in enumerate(sites, 1))

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Catalogo Resultiva</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
*, *::before, *::after {{ margin:0; padding:0; box-sizing:border-box; }}

:root {{
  --navy:   #0C1829;
  --green:  #1EC28B;
  --green2: #17A877;
  --white:  #ffffff;
  --gray:   #F4F6FA;
  --border: #E2E8F0;
  --dark:   #1A2744;
  --mid:    #4A5568;
  --light:  #8896A8;
}}

body {{
  font-family: 'Montserrat', sans-serif;
  background: #D0D5DE;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}}

/* ── PAGE ── */
.page {{
  width: 210mm;
  height: 297mm;
  background: var(--white);
  margin: 0 auto 24px;
  box-shadow: 0 8px 40px rgba(0,0,0,.18);
  overflow: hidden;
  position: relative;
  display: flex;
  flex-direction: column;
}}

/* ── COVER ── */
.cover {{
  background: var(--navy);
  justify-content: space-between;
  padding: 56px 52px 40px;
}}

.cover-top {{ display:flex; flex-direction:column; gap:4px; }}
.cover-brand {{ font-size:11px; font-weight:800; letter-spacing:5px; color:var(--green); text-transform:uppercase; }}
.cover-brand-sub {{ font-size:9px; letter-spacing:3px; color:rgba(255,255,255,.3); text-transform:uppercase; }}

.cover-center {{ text-align:center; padding:20px 0; }}
.cover-tag {{
  display:inline-block;
  font-size:9px; font-weight:700; letter-spacing:3px; text-transform:uppercase;
  color:var(--green); border:1px solid rgba(30,194,139,.35);
  padding:6px 16px; border-radius:20px; margin-bottom:28px;
}}
.cover-title {{
  font-size:42px; font-weight:900; line-height:1.08;
  color:var(--white); letter-spacing:-1px;
}}
.cover-title em {{ font-style:normal; color:var(--green); }}
.cover-sub {{
  font-size:13px; font-weight:400; line-height:1.75;
  color:rgba(255,255,255,.45); margin-top:20px; max-width:340px; margin-left:auto; margin-right:auto;
}}

/* phones mockup row on cover */
.cover-phones {{
  display:flex; justify-content:center; align-items:flex-end;
  gap:16px; margin-top:32px; height:200px; overflow:hidden;
}}
.cover-phone-mini {{
  width:72px; height:148px;
  border:5px solid rgba(255,255,255,.15);
  border-radius:16px; overflow:hidden;
  flex-shrink:0;
}}
.cover-phone-mini.main {{
  width:90px; height:185px;
  border-color:rgba(30,194,139,.5);
  transform:translateY(-20px);
}}
.cover-phone-mini img {{ width:100%; height:100%; object-fit:cover; object-position:top; }}

.cover-bottom {{
  display:flex; justify-content:space-between; align-items:center;
  padding-top:24px; border-top:1px solid rgba(255,255,255,.08);
}}
.cover-count {{ display:flex; gap:40px; }}
.cover-stat-n {{ font-size:26px; font-weight:900; color:var(--green); }}
.cover-stat-l {{ font-size:8px; font-weight:600; letter-spacing:2px; text-transform:uppercase; color:rgba(255,255,255,.3); margin-top:3px; }}
.cover-cta {{
  font-size:10px; font-weight:700; letter-spacing:2px; text-transform:uppercase;
  color:rgba(255,255,255,.25);
}}

/* ── TOP BAR (site pages) ── */
.top-bar {{
  display:flex; justify-content:space-between; align-items:center;
  padding:18px 32px;
  border-bottom:1px solid var(--border);
  background:var(--gray);
  flex-shrink:0;
}}
.top-num {{ font-size:11px; font-weight:700; color:var(--light); letter-spacing:2px; }}
.top-sep {{ color:var(--border); }}
.top-brand {{ font-size:10px; font-weight:800; letter-spacing:4px; color:var(--green); text-transform:uppercase; }}

/* ── SITE BODY ── */
.site-body {{
  flex:1; display:flex; align-items:stretch; overflow:hidden;
}}

/* phone column */
.phone-col {{
  width:42%; background:var(--gray);
  display:flex; flex-direction:column; align-items:center; justify-content:center;
  padding:24px 20px 16px;
  border-right:1px solid var(--border);
}}
.phone-link {{ text-decoration:none; display:flex; flex-direction:column; align-items:center; gap:10px; }}

.phone-wrap {{ position:relative; }}
.phone-frame {{
  width:165px; height:340px;
  background:#0C1829;
  border-radius:32px;
  padding:14px 7px 16px;
  position:relative;
  box-shadow:
    0 0 0 1.5px rgba(255,255,255,.08),
    0 20px 60px rgba(0,0,0,.45),
    inset 0 1px 0 rgba(255,255,255,.12);
}}
.phone-notch {{
  position:absolute; top:10px; left:50%; transform:translateX(-50%);
  width:52px; height:12px;
  background:#0C1829;
  border-radius:0 0 10px 10px;
  z-index:10;
}}
.phone-screen {{
  width:100%; height:100%;
  border-radius:22px;
  overflow:hidden;
  background:#000;
}}
.phone-screen img {{
  width:100%; height:100%;
  object-fit:cover; object-position:top;
  display:block;
}}
.phone-bar {{
  position:absolute; bottom:8px; left:50%; transform:translateX(-50%);
  width:48px; height:4px;
  background:rgba(255,255,255,.3);
  border-radius:4px;
}}
.phone-shadow {{
  position:absolute; bottom:-16px; left:50%; transform:translateX(-50%);
  width:120px; height:20px;
  background:rgba(0,0,0,.25);
  border-radius:50%;
  filter:blur(10px);
}}

.tap-hint {{
  font-size:9px; font-weight:600; letter-spacing:1.5px; text-transform:uppercase;
  color:var(--green); margin-top:20px;
}}
.phone-link:hover .phone-frame {{ box-shadow: 0 0 0 2px var(--green), 0 24px 64px rgba(0,0,0,.5); }}

/* info column */
.info-col {{
  flex:1; display:flex; align-items:center; padding:32px 36px;
}}
.info-inner {{ display:flex; flex-direction:column; gap:0; width:100%; }}

.info-tag {{
  font-size:8px; font-weight:700; letter-spacing:3px; text-transform:uppercase;
  color:var(--green); margin-bottom:14px;
}}
.info-name {{
  font-size:24px; font-weight:800; line-height:1.15;
  color:var(--dark); letter-spacing:-.5px;
}}
.info-esp {{
  font-size:11px; font-weight:500; color:var(--light);
  margin-top:6px; letter-spacing:.5px;
}}
.info-divider {{
  width:36px; height:2px; background:var(--green);
  border-radius:2px; margin:20px 0;
}}
.info-desc {{
  font-size:12px; font-weight:400; line-height:1.7;
  color:var(--mid); margin-bottom:28px;
}}
.info-btn {{
  display:inline-flex; align-items:center; gap:6px;
  background:var(--navy); color:var(--white);
  font-size:11px; font-weight:700; letter-spacing:1px; text-transform:uppercase;
  text-decoration:none;
  padding:13px 24px; border-radius:6px;
  width:fit-content;
  transition:background .2s;
}}
.info-btn:hover {{ background:var(--green); }}
.info-url {{
  font-size:10px; color:var(--light); margin-top:14px;
  word-break:break-all; letter-spacing:.3px;
}}

/* ── PAGE FOOTER ── */
.page-footer {{
  display:flex; justify-content:space-between; align-items:center;
  padding:12px 32px;
  border-top:1px solid var(--border);
  background:var(--gray);
  font-size:9px; font-weight:500; color:var(--light);
  letter-spacing:.5px;
  flex-shrink:0;
}}

/* ── PRINT ── */
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
<div class="page cover">

  <div class="cover-top">
    <div class="cover-brand">Resultiva</div>
    <div class="cover-brand-sub">Assessoria de Marketing</div>
  </div>

  <div class="cover-center">
    <div class="cover-tag">Portfolio de Sites</div>
    <h1 class="cover-title">Sites que<br><em>convertem</em><br>pacientes</h1>
    <p class="cover-sub">Selecao de presencas digitais desenvolvidas para psicologas que querem ser encontradas e escolhidas online.</p>
    <div class="cover-phones">
      <div class="cover-phone-mini"><img src="data:image/png;base64,{imgs['rosangela']}" /></div>
      <div class="cover-phone-mini"><img src="data:image/png;base64,{imgs['karine']}" /></div>
      <div class="cover-phone-mini main"><img src="data:image/png;base64,{imgs['stella']}" /></div>
      <div class="cover-phone-mini"><img src="data:image/png;base64,{imgs['rafaela']}" /></div>
      <div class="cover-phone-mini"><img src="data:image/png;base64,{imgs['nathalia']}" /></div>
    </div>
  </div>

  <div class="cover-bottom">
    <div class="cover-count">
      <div>
        <div class="cover-stat-n">5</div>
        <div class="cover-stat-l">Sites</div>
      </div>
      <div>
        <div class="cover-stat-n">100%</div>
        <div class="cover-stat-l">Clicaveis</div>
      </div>
    </div>
    <div class="cover-cta">Clique em qualquer site &rarr;</div>
  </div>

</div>

{cards}

</body>
</html>"""

with open("catalogo-psicologas-v2.html", "w", encoding="utf-8") as f:
    f.write(html)

print("HTML gerado: catalogo-psicologas-v2.html")
