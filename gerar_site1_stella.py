import base64, struct, math, asyncio

def png_size(path):
    with open(path, 'rb') as f:
        f.read(8); f.read(4); f.read(4)
        w = struct.unpack('>I', f.read(4))[0]
        h = struct.unpack('>I', f.read(4))[0]
    return w, h

# ── site data ────────────────────────────────────────────────────────────────
site = {
    "num":   "01",
    "name":  "stella",
    "label": "Stella Mansur",
    "esp":   "Psicologa Clinica",
    "url":   "psicologastellamansur.com.br",
}

fp_path = f"psi-fullpage/{site['name']}.png"
mb_path = f"psi-mobile/{site['name']}.png"

orig_w, orig_h = png_size(fp_path)
with open(fp_path, 'rb') as f:
    b64_full = base64.b64encode(f.read()).decode()
with open(mb_path, 'rb') as f:
    b64_mobile = base64.b64encode(f.read()).decode()

# ── A4 layout ────────────────────────────────────────────────────────────────
PAGE_W_PX = 794      # 210 mm at 96 dpi
PAGE_H_PX = 1122     # 297 mm at 96 dpi
HEADER_H  = 46
CONTENT_H = PAGE_H_PX - HEADER_H   # 1076 px

scale       = PAGE_W_PX / orig_w    # how much the img scales to fill page width
disp_h      = math.ceil(orig_h * scale)
n_pages     = math.ceil(disp_h / CONTENT_H)

print(f"Stella: {orig_w}x{orig_h}px  scale={scale:.3f}  "
      f"displayed={PAGE_W_PX}x{disp_h}px  pages={n_pages}")

# ── content pages (background-image slicing) ─────────────────────────────────
content_pages = []
for i in range(n_pages):
    offset = i * CONTENT_H          # px shift in display-space
    content_pages.append(f"""
<div class="page content-page">
  <div class="sp-hdr">
    <div class="sp-left">
      <span class="sp-num">{site['num']}</span>
      <span class="sp-name">{site['label']}</span>
      <span class="sp-sep">&middot;</span>
      <span class="sp-esp">{site['esp']}</span>
    </div>
    <div class="sp-right">
      <span class="sp-brand">RESULTIVA</span>
      <span class="sp-pg">{i+1}&thinsp;/&thinsp;{n_pages}</span>
    </div>
  </div>
  <div class="sp-body" style="
    background-image: url('data:image/png;base64,{b64_full}');
    background-size: {PAGE_W_PX}px auto;
    background-position: 0px -{offset}px;
    background-repeat: no-repeat;
  "></div>
</div>""")

pages_html = "\n".join(content_pages)

# ── cover page ────────────────────────────────────────────────────────────────
cover_html = f"""
<div class="page cover-page">
  <div class="cv-deco"></div>

  <div class="cv-top">
    <div class="cv-brand">
      <div class="cv-brand-name">Resultiva</div>
      <div class="cv-brand-sub">Assessoria de Marketing</div>
    </div>
    <div class="cv-badge">Site {site['num']} de 05</div>
  </div>

  <div class="cv-body">
    <div class="cv-phone">
      <div class="cv-phone-frame">
        <div class="cv-phone-notch"></div>
        <div class="cv-phone-screen">
          <img src="data:image/png;base64,{b64_mobile}" alt="{site['label']}">
        </div>
        <div class="cv-phone-bar"></div>
      </div>
    </div>

    <div class="cv-info">
      <div class="cv-tag">Portfolio Resultiva</div>
      <h1 class="cv-name">{site['label']}</h1>
      <p class="cv-esp">{site['esp']}</p>
      <div class="cv-line"></div>
      <p class="cv-desc">
        Presença digital desenvolvida para atrair e converter
        pacientes online com foco em agendamentos.
      </p>
      <div class="cv-url-wrap">
        <span class="cv-url-dot"></span>
        <span class="cv-url">{site['url']}</span>
      </div>
      <div class="cv-pages-info">
        <span class="cv-pi-n">{n_pages}</span>
        <span class="cv-pi-l">páginas de conteúdo</span>
      </div>
    </div>
  </div>

  <div class="cv-footer">
    <span>Resultiva &mdash; Assessoria de Marketing</span>
    <span>{site['url']}</span>
  </div>
</div>
"""

# ── full HTML ─────────────────────────────────────────────────────────────────
html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>{site['label']} - Resultiva Portfolio</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{{margin:0;padding:0;box-sizing:border-box;}}

body{{
  font-family:'Montserrat',sans-serif;
  background:#A8B0BC;
  -webkit-print-color-adjust:exact;
  print-color-adjust:exact;
}}

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

/* ── COVER ── */
.cover-page{{
  background:linear-gradient(160deg,#0a1523 0%,#0d2040 60%,#0a1830 100%);
  padding:0;
}}

.cv-deco{{
  position:absolute;
  top:0;right:0;
  width:180px;height:180px;
  background:radial-gradient(circle,rgba(30,194,139,.15) 0%,transparent 70%);
  pointer-events:none;
}}

.cv-top{{
  display:flex;align-items:flex-start;justify-content:space-between;
  padding:44px 48px 0;
}}
.cv-brand-name{{
  font-size:11px;font-weight:800;letter-spacing:5px;
  color:#1EC28B;text-transform:uppercase;
}}
.cv-brand-sub{{
  font-size:8px;letter-spacing:3px;
  color:rgba(255,255,255,.28);margin-top:3px;text-transform:uppercase;
}}
.cv-badge{{
  font-size:8px;font-weight:700;letter-spacing:2px;
  color:#1EC28B;border:1px solid rgba(30,194,139,.4);
  padding:5px 13px;border-radius:20px;text-transform:uppercase;
}}

.cv-body{{
  flex:1;
  display:flex;
  align-items:center;
  gap:44px;
  padding:32px 48px;
}}

/* phone mockup */
.cv-phone{{
  flex-shrink:0;
  display:flex;align-items:center;justify-content:center;
}}
.cv-phone-frame{{
  width:158px;height:310px;
  background:#0C1829;
  border-radius:30px;
  padding:14px 7px 14px;
  position:relative;
  box-shadow:
    0 0 0 1.5px rgba(255,255,255,.08),
    0 24px 64px rgba(0,0,0,.6),
    inset 0 1px 0 rgba(255,255,255,.1);
}}
.cv-phone-notch{{
  position:absolute;top:9px;left:50%;transform:translateX(-50%);
  width:48px;height:10px;
  background:#0C1829;border-radius:0 0 8px 8px;z-index:10;
}}
.cv-phone-screen{{
  width:100%;height:100%;
  border-radius:20px;overflow:hidden;background:#000;
}}
.cv-phone-screen img{{
  width:100%;height:100%;object-fit:cover;object-position:top;display:block;
}}
.cv-phone-bar{{
  position:absolute;bottom:7px;left:50%;transform:translateX(-50%);
  width:44px;height:3px;
  background:rgba(255,255,255,.28);border-radius:3px;
}}

/* info block */
.cv-info{{flex:1;}}
.cv-tag{{
  font-size:8px;font-weight:700;letter-spacing:3px;
  color:#1EC28B;text-transform:uppercase;margin-bottom:16px;
}}
.cv-name{{
  font-size:28px;font-weight:900;line-height:1.1;
  color:#fff;letter-spacing:-.5px;
}}
.cv-esp{{
  font-size:11px;font-weight:500;
  color:rgba(255,255,255,.45);margin-top:6px;letter-spacing:.5px;
}}
.cv-line{{
  width:32px;height:2px;background:#1EC28B;
  border-radius:2px;margin:20px 0;
}}
.cv-desc{{
  font-size:11px;font-weight:400;line-height:1.75;
  color:rgba(255,255,255,.5);margin-bottom:22px;
}}
.cv-url-wrap{{display:flex;align-items:center;gap:7px;margin-bottom:24px;}}
.cv-url-dot{{
  width:6px;height:6px;border-radius:50%;
  background:#1EC28B;flex-shrink:0;
}}
.cv-url{{
  font-size:10px;font-weight:600;
  color:rgba(255,255,255,.6);letter-spacing:.3px;
}}
.cv-pages-info{{
  display:inline-flex;align-items:baseline;gap:8px;
  background:rgba(30,194,139,.1);
  border:1px solid rgba(30,194,139,.2);
  padding:10px 18px;border-radius:8px;
}}
.cv-pi-n{{font-size:22px;font-weight:900;color:#1EC28B;}}
.cv-pi-l{{font-size:9px;font-weight:600;color:rgba(255,255,255,.4);letter-spacing:1px;}}

.cv-footer{{
  display:flex;justify-content:space-between;
  padding:14px 48px;
  border-top:1px solid rgba(255,255,255,.07);
  font-size:8px;font-weight:500;
  color:rgba(255,255,255,.22);letter-spacing:.5px;
  flex-shrink:0;
}}

/* ── CONTENT PAGES ── */
.content-page{{}}

.sp-hdr{{
  height:{HEADER_H}px;
  background:#0C1829;
  display:flex;align-items:center;justify-content:space-between;
  padding:0 18px;flex-shrink:0;
}}
.sp-left{{display:flex;align-items:center;gap:8px;min-width:0;}}
.sp-num{{
  font-size:10px;font-weight:900;color:#1EC28B;
  background:rgba(30,194,139,.12);padding:3px 8px;border-radius:4px;flex-shrink:0;
}}
.sp-name{{font-size:10px;font-weight:700;color:#fff;white-space:nowrap;}}
.sp-sep{{color:rgba(255,255,255,.2);flex-shrink:0;}}
.sp-esp{{font-size:8px;font-weight:400;color:rgba(255,255,255,.38);white-space:nowrap;}}
.sp-right{{display:flex;align-items:center;gap:10px;flex-shrink:0;}}
.sp-brand{{
  font-size:8px;font-weight:800;letter-spacing:4px;
  color:#1EC28B;text-transform:uppercase;
}}
.sp-pg{{font-size:8px;font-weight:500;color:rgba(255,255,255,.3);}}

.sp-body{{
  flex:1;
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

{cover_html}

{pages_html}

</body>
</html>"""

out_html = "site1-stella.html"
with open(out_html, "w", encoding="utf-8") as f:
    f.write(html)
print(f"HTML gerado: {out_html}  ({n_pages+1} paginas total com capa)")

# ── generate PDF ─────────────────────────────────────────────────────────────
async def make_pdf():
    from playwright.async_api import async_playwright
    import os
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        html_path = os.path.abspath(out_html)
        await page.goto(f'file:///{html_path}', wait_until='networkidle')
        await page.wait_for_timeout(4000)
        await page.pdf(
            path='site1-stella-RESULTIVA.pdf',
            format='A4',
            print_background=True,
            margin={'top':'0','right':'0','bottom':'0','left':'0'}
        )
        await browser.close()
        import os as _os
        size = _os.path.getsize('site1-stella-RESULTIVA.pdf')
        print(f"PDF gerado: site1-stella-RESULTIVA.pdf  ({size/1024/1024:.1f} MB)")

asyncio.run(make_pdf())
