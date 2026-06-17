import base64, os

sites = [
    {"name": "stella",    "label": "Stella Mansur",             "esp": "Psicologa Clinica",   "url": "https://psicologastellamansur.com.br/",      "h": 8823},
    {"name": "karine",    "label": "Karine Moraes",              "esp": "Psicoterapia Online", "url": "https://karinemoraes.com/lp/psicoterapia-online/", "h": 7463},
    {"name": "rafaela",   "label": "Rafaela Beloti",             "esp": "Psicologa",           "url": "https://psirafaelabeloti.com.br/",           "h": 11045},
    {"name": "nathalia",  "label": "Nathalia Morato",            "esp": "Psicologa",           "url": "https://dranathaliamorato.com.br/",          "h": 8064},
    {"name": "rosangela", "label": "Rosangela Alvim Cassimiro",  "esp": "Psicologa Clinica",   "url": "https://rosangelaalvimcassimiro.com/",       "h": 9829},
]

imgs = {}
for s in sites:
    with open(f"psi-fullpage/{s['name']}.png", "rb") as f:
        imgs[s["name"]] = base64.b64encode(f.read()).decode()

# cover uses the above-fold mobile shots
cover_imgs = {}
for s in sites:
    with open(f"psi-mobile/{s['name']}.png", "rb") as f:
        cover_imgs[s["name"]] = base64.b64encode(f.read()).decode()

def site_page(s, i):
    num   = str(i).zfill(2)
    total = len(sites)
    domain = s["url"].replace("https://","").replace("http://","").rstrip("/")
    b64   = imgs[s["name"]]

    # mid and bottom offset as % of (image_height - container_visible_height)
    # We use CSS background-position percentages:
    # 0%   = top     | shows hero / above fold
    # 42%  = upper-mid | shows first content sections
    # 100% = bottom  | shows CTA / footer

    return f"""
<div class="page site-page">

  <div class="sp-header">
    <div class="sp-left">
      <span class="sp-num">{num}<span class="sp-total">/{total:02d}</span></span>
      <div class="sp-title-block">
        <h2 class="sp-name">{s['label']}</h2>
        <span class="sp-esp">{s['esp']}</span>
      </div>
    </div>
    <span class="sp-brand">RESULTIVA</span>
  </div>

  <div class="sp-body">

    <!-- PAINEL ESQUERDO: HERO / TOPO DO SITE -->
    <div class="panel panel-left">
      <div class="panel-label">Topo</div>
      <div class="panel-img"
           style="background-image:url('data:image/png;base64,{b64}');
                  background-position: 0% 0%;">
      </div>
    </div>

    <!-- PAINEIS DIREITOS: MEIO E RODAPE -->
    <div class="panel-col-right">

      <div class="panel panel-right panel-top">
        <div class="panel-label">Meio</div>
        <div class="panel-img"
             style="background-image:url('data:image/png;base64,{b64}');
                    background-position: 0% 42%;">
        </div>
      </div>

      <div class="panel panel-right panel-bot">
        <div class="panel-label">Rodape</div>
        <div class="panel-img"
             style="background-image:url('data:image/png;base64,{b64}');
                    background-position: 0% 100%;">
        </div>
      </div>

    </div>
  </div>

  <div class="sp-footer">
    <span class="sp-domain">{domain}</span>
    <span class="sp-note">Resultiva &mdash; Assessoria de Marketing</span>
  </div>

</div>
"""

pages_html = "".join(site_page(s, i) for i, s in enumerate(sites, 1))

cover_imgs_html = "".join(
    f'<div class="cp-mini {"cp-center" if idx==2 else ""}"><img src="data:image/png;base64,{cover_imgs[s["name"]]}" /></div>'
    for idx, s in enumerate(sites)
)

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Catalogo Resultiva</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{{margin:0;padding:0;box-sizing:border-box;}}

:root{{
  --navy: #0C1829;
  --green:#1EC28B;
  --white:#ffffff;
  --bg:   #F2F5F9;
  --brd:  #DDE3EC;
  --dark: #1A2744;
  --mid:  #5A6A7E;
  --light:#8FA3BA;
}}

body{{
  font-family:'Montserrat',sans-serif;
  background:#CBD2DA;
  -webkit-print-color-adjust:exact;
  print-color-adjust:exact;
}}

/* PAGE */
.page{{
  width:210mm; height:297mm;
  background:var(--white);
  margin:0 auto 24px;
  box-shadow:0 8px 40px rgba(0,0,0,.2);
  overflow:hidden;
  position:relative;
  display:flex;
  flex-direction:column;
}}

/* ============ CAPA ============ */
.cover{{
  background:var(--navy);
  justify-content:space-between;
  padding:52px 48px 40px;
}}
.cv-brand{{font-size:10px;font-weight:800;letter-spacing:5px;color:var(--green);text-transform:uppercase;}}
.cv-sub{{font-size:8px;letter-spacing:3px;color:rgba(255,255,255,.28);text-transform:uppercase;margin-top:3px;}}

.cv-center{{text-align:center;padding:16px 0 0;}}
.cv-tag{{
  display:inline-block;font-size:8px;font-weight:700;letter-spacing:3px;
  color:var(--green);border:1px solid rgba(30,194,139,.3);
  padding:5px 14px;border-radius:20px;margin-bottom:22px;text-transform:uppercase;
}}
.cv-title{{
  font-size:44px;font-weight:900;line-height:1.05;
  color:#fff;letter-spacing:-1.5px;
}}
.cv-title em{{font-style:normal;color:var(--green);}}
.cv-desc{{
  font-size:12px;font-weight:400;line-height:1.75;
  color:rgba(255,255,255,.4);margin-top:18px;max-width:320px;margin-inline:auto;
}}

/* mini phones strip on cover */
.cv-phones{{
  display:flex;justify-content:center;align-items:flex-end;
  gap:10px;margin-top:28px;height:195px;overflow:hidden;
}}
.cp-mini{{
  width:68px;height:148px;
  border:4px solid rgba(255,255,255,.12);
  border-radius:14px;overflow:hidden;flex-shrink:0;
}}
.cp-center{{
  width:84px;height:182px;
  border-color:rgba(30,194,139,.5);
  transform:translateY(-18px);
  box-shadow:0 12px 36px rgba(0,0,0,.5);
}}
.cp-mini img,.cp-center img{{width:100%;height:100%;object-fit:cover;object-position:top;}}

.cv-bottom{{
  display:flex;justify-content:space-between;align-items:center;
  padding-top:22px;border-top:1px solid rgba(255,255,255,.07);
}}
.cv-stats{{display:flex;gap:36px;}}
.cv-stat-n{{font-size:24px;font-weight:900;color:var(--green);}}
.cv-stat-l{{font-size:7px;font-weight:600;letter-spacing:2px;color:rgba(255,255,255,.28);margin-top:2px;text-transform:uppercase;}}
.cv-note{{font-size:9px;font-weight:600;letter-spacing:2px;color:rgba(255,255,255,.2);text-transform:uppercase;}}

/* ============ SITE PAGE ============ */

/* header strip */
.sp-header{{
  display:flex;justify-content:space-between;align-items:center;
  padding:14px 24px;
  background:var(--bg);
  border-bottom:1px solid var(--brd);
  flex-shrink:0;
  height:58px;
}}
.sp-left{{display:flex;align-items:center;gap:12px;}}
.sp-num{{
  font-size:13px;font-weight:900;color:var(--green);letter-spacing:-0.5px;
  white-space:nowrap;
}}
.sp-total{{font-size:10px;font-weight:600;color:var(--light);}}
.sp-name{{font-size:15px;font-weight:800;color:var(--dark);letter-spacing:-.3px;}}
.sp-esp{{font-size:9px;font-weight:500;color:var(--light);letter-spacing:.5px;margin-top:1px;display:block;}}
.sp-brand{{font-size:9px;font-weight:800;letter-spacing:4px;color:var(--green);text-transform:uppercase;}}

/* body: panels */
.sp-body{{
  flex:1;
  display:flex;
  gap:0;
  overflow:hidden;
}}

.panel{{
  position:relative;
  overflow:hidden;
}}

.panel-left{{
  width:52%;
  border-right:2px solid var(--brd);
}}

.panel-col-right{{
  flex:1;
  display:flex;
  flex-direction:column;
}}

.panel-right{{flex:1;}}
.panel-top{{border-bottom:2px solid var(--brd);}}

/* the actual image window */
.panel-img{{
  width:100%;
  height:100%;
  background-repeat:no-repeat;
  background-size:100% auto;   /* fills width, height scales */
  background-position:0% 0%;
}}

/* section label chip */
.panel-label{{
  position:absolute;
  top:10px;left:10px;
  font-size:7px;font-weight:700;letter-spacing:2px;
  text-transform:uppercase;
  color:var(--light);
  background:rgba(255,255,255,.92);
  border:1px solid var(--brd);
  padding:4px 8px;
  border-radius:4px;
  z-index:10;
}}

/* footer strip */
.sp-footer{{
  display:flex;justify-content:space-between;align-items:center;
  padding:10px 24px;
  background:var(--bg);
  border-top:1px solid var(--brd);
  flex-shrink:0;
  height:38px;
}}
.sp-domain{{font-size:9px;font-weight:600;color:var(--mid);letter-spacing:.3px;}}
.sp-note{{font-size:8px;font-weight:500;color:var(--light);letter-spacing:.5px;}}

/* ============ PRINT ============ */
@media print{{
  body{{background:white;}}
  .page{{
    margin:0;
    box-shadow:none;
    page-break-after:always;
    width:100%;height:100vh;
  }}
}}
</style>
</head>
<body>

<!-- CAPA -->
<div class="page cover">
  <div>
    <div class="cv-brand">Resultiva</div>
    <div class="cv-sub">Assessoria de Marketing</div>
  </div>

  <div class="cv-center">
    <div class="cv-tag">Portfolio de Sites</div>
    <h1 class="cv-title">Sites que<br><em>convertem</em><br>pacientes</h1>
    <p class="cv-desc">Selecao de presencas digitais para psicologas que querem ser encontradas e escolhidas online.</p>
    <div class="cv-phones">
      {cover_imgs_html}
    </div>
  </div>

  <div class="cv-bottom">
    <div class="cv-stats">
      <div>
        <div class="cv-stat-n">5</div>
        <div class="cv-stat-l">Sites</div>
      </div>
      <div>
        <div class="cv-stat-n">3</div>
        <div class="cv-stat-l">Views por site</div>
      </div>
    </div>
    <div class="cv-note">Visualizacao completa em cada pagina</div>
  </div>
</div>

{pages_html}

</body>
</html>"""

with open("catalogo-psicologas-v3.html", "w", encoding="utf-8") as f:
    f.write(html)
print("HTML v3 gerado!")
