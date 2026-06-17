import base64

sites = [
    {"name": "stella",    "label": "Stella Mansur",          "esp": "Psicologia Clinica",      "url": "https://psicologastellamansur.com.br/"},
    {"name": "karine",    "label": "Karine Moraes",           "esp": "Psicoterapia Online",     "url": "https://karinemoraes.com/lp/psicoterapia-online/"},
    {"name": "rafaela",   "label": "Rafaela Beloti",          "esp": "Psicologia",              "url": "https://psirafaelabeloti.com.br/"},
    {"name": "nathalia",  "label": "Nathalia Morato",         "esp": "Psicologia",              "url": "https://dranathaliamorato.com.br/"},
    {"name": "rosangela", "label": "Rosangela Alvim Cassimiro","esp": "Psicologia Clinica",     "url": "https://rosangelaalvimcassimiro.com/"},
]

imgs = {}
for s in sites:
    with open(f"psi-screenshots/{s['name']}.png", "rb") as f:
        imgs[s["name"]] = base64.b64encode(f.read()).decode()

def site_card(s, i):
    num = str(i).zfill(2)
    return f"""
    <div class="page site-page">
      <div class="page-header">
        <span class="site-num">{num}</span>
        <div class="site-meta">
          <h2 class="site-name">{s['label']}</h2>
          <span class="site-esp">{s['esp']}</span>
        </div>
        <a class="site-url-pill" href="{s['url']}" target="_blank">{s['url'].replace('https://','').rstrip('/')}</a>
      </div>
      <a href="{s['url']}" target="_blank" class="screenshot-link">
        <div class="screenshot-wrap">
          <img src="data:image/png;base64,{imgs[s['name']]}" class="screenshot" alt="{s['label']}" />
          <div class="screenshot-overlay">
            <span class="visit-btn">Visitar site &#8599;</span>
          </div>
        </div>
      </a>
      <div class="site-footer-note">
        Clique na imagem ou no link acima para acessar o site completo
      </div>
    </div>
"""

cards_html = ""
for i, s in enumerate(sites, 1):
    cards_html += site_card(s, i)

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Catalogo de Sites - Resultiva</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}

  :root {{
    --navy: #0D1B2A;
    --accent: #1EC28B;
    --accent2: #0FA878;
    --light-bg: #F7F9FC;
    --border: #E2E8F0;
    --text-dark: #1a2744;
    --text-mid: #4A5568;
    --text-light: #718096;
    --white: #ffffff;
  }}

  body {{
    font-family: 'Montserrat', sans-serif;
    background: #e8ecf0;
    color: var(--text-dark);
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }}

  /* PAGE LAYOUT */
  .page {{
    width: 210mm;
    min-height: 297mm;
    background: var(--white);
    margin: 0 auto 20px;
    box-shadow: 0 4px 24px rgba(0,0,0,0.1);
    position: relative;
    overflow: hidden;
  }}

  /* COVER PAGE */
  .cover-page {{
    background: var(--navy);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 60px 48px;
    text-align: center;
  }}

  .cover-logo-area {{
    margin-bottom: 60px;
  }}

  .cover-logo {{
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 6px;
  }}

  .cover-logo-sub {{
    font-size: 10px;
    font-weight: 400;
    letter-spacing: 2px;
    color: rgba(255,255,255,0.4);
    text-transform: uppercase;
  }}

  .cover-divider {{
    width: 48px;
    height: 2px;
    background: var(--accent);
    margin: 48px auto;
    opacity: 0.6;
  }}

  .cover-tag {{
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 20px;
    opacity: 0.9;
  }}

  .cover-title {{
    font-size: 36px;
    font-weight: 800;
    color: #ffffff;
    line-height: 1.15;
    margin-bottom: 16px;
    letter-spacing: -0.5px;
  }}

  .cover-title span {{
    color: var(--accent);
  }}

  .cover-subtitle {{
    font-size: 14px;
    font-weight: 400;
    color: rgba(255,255,255,0.55);
    line-height: 1.7;
    max-width: 380px;
    margin: 0 auto;
  }}

  .cover-stats {{
    display: flex;
    gap: 40px;
    margin-top: 72px;
    border-top: 1px solid rgba(255,255,255,0.1);
    padding-top: 40px;
    width: 100%;
    justify-content: center;
  }}

  .stat {{
    text-align: center;
  }}

  .stat-num {{
    font-size: 28px;
    font-weight: 800;
    color: var(--accent);
  }}

  .stat-label {{
    font-size: 9px;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: rgba(255,255,255,0.35);
    margin-top: 4px;
  }}

  .cover-bottom {{
    position: absolute;
    bottom: 32px;
    left: 0; right: 0;
    text-align: center;
    font-size: 10px;
    color: rgba(255,255,255,0.2);
    letter-spacing: 1px;
  }}

  /* SITE PAGES */
  .site-page {{
    display: flex;
    flex-direction: column;
    padding: 0;
  }}

  .page-header {{
    display: flex;
    align-items: center;
    gap: 16px;
    padding: 24px 32px;
    border-bottom: 1px solid var(--border);
    background: var(--light-bg);
  }}

  .site-num {{
    font-size: 11px;
    font-weight: 800;
    color: var(--accent);
    letter-spacing: 2px;
    background: rgba(30,194,139,0.1);
    padding: 6px 10px;
    border-radius: 6px;
    flex-shrink: 0;
  }}

  .site-meta {{
    flex: 1;
    min-width: 0;
  }}

  .site-name {{
    font-size: 17px;
    font-weight: 700;
    color: var(--text-dark);
    line-height: 1.2;
  }}

  .site-esp {{
    font-size: 11px;
    font-weight: 500;
    color: var(--text-light);
    letter-spacing: 0.5px;
    margin-top: 2px;
    display: block;
  }}

  .site-url-pill {{
    font-size: 10px;
    font-weight: 600;
    color: var(--accent2);
    background: rgba(30,194,139,0.08);
    border: 1px solid rgba(30,194,139,0.25);
    padding: 6px 12px;
    border-radius: 20px;
    text-decoration: none;
    white-space: nowrap;
    flex-shrink: 0;
    transition: all 0.2s;
    letter-spacing: 0.3px;
  }}

  .site-url-pill:hover {{
    background: var(--accent);
    color: white;
    border-color: var(--accent);
  }}

  .screenshot-link {{
    display: block;
    flex: 1;
    text-decoration: none;
    cursor: pointer;
    position: relative;
  }}

  .screenshot-wrap {{
    position: relative;
    overflow: hidden;
    height: 220mm;
  }}

  .screenshot {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: top;
    display: block;
    transition: transform 0.3s;
  }}

  .screenshot-overlay {{
    position: absolute;
    inset: 0;
    background: rgba(13,27,42,0);
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background 0.3s;
  }}

  .screenshot-link:hover .screenshot-overlay {{
    background: rgba(13,27,42,0.55);
  }}

  .visit-btn {{
    background: var(--accent);
    color: white;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1px;
    padding: 12px 28px;
    border-radius: 4px;
    opacity: 0;
    transform: translateY(8px);
    transition: all 0.3s;
  }}

  .screenshot-link:hover .visit-btn {{
    opacity: 1;
    transform: translateY(0);
  }}

  .site-footer-note {{
    font-size: 10px;
    color: var(--text-light);
    text-align: center;
    padding: 10px 32px;
    border-top: 1px solid var(--border);
    background: var(--light-bg);
    letter-spacing: 0.3px;
  }}

  /* PRINT */
  @media print {{
    body {{ background: white; }}
    .page {{
      margin: 0;
      box-shadow: none;
      page-break-after: always;
      width: 100%;
    }}
    .screenshot-wrap {{ height: 218mm; }}
    .cover-page {{ min-height: 297mm; }}
  }}
</style>
</head>
<body>

<!-- CAPA -->
<div class="page cover-page">
  <div class="cover-logo-area">
    <div class="cover-logo">Resultiva</div>
    <div class="cover-logo-sub">Assessoria de Marketing</div>
  </div>

  <div>
    <div class="cover-tag">Catalogo de Portfolio</div>
    <h1 class="cover-title">Sites que <span>convertem</span><br>pacientes em<br>agendamentos</h1>
    <p class="cover-subtitle">
      Uma selecao de presencas digitais desenvolvidas para psicologas
      que querem ser encontradas e escolhidas online.
    </p>
  </div>

  <div class="cover-divider"></div>

  <div class="cover-stats">
    <div class="stat">
      <div class="stat-num">5</div>
      <div class="stat-label">Sites no catalogo</div>
    </div>
    <div class="stat">
      <div class="stat-num">100%</div>
      <div class="stat-label">Clicaveis</div>
    </div>
    <div class="stat">
      <div class="stat-num">+Agenda</div>
      <div class="stat-label">Foco em resultado</div>
    </div>
  </div>

  <div class="cover-bottom">resultiva.com.br &nbsp;&middot;&nbsp; Todos os sites sao clicaveis</div>
</div>

{cards_html}

</body>
</html>"""

with open("catalogo-psicologas.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Catalogo gerado: catalogo-psicologas.html")
