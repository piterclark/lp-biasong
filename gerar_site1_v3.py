import base64, asyncio, math, os

SITE = {
    "num":   "01",
    "name":  "stella",
    "label": "Stella Mansur",
    "esp":   "Psicologa Clinica",
    "url":   "https://psicologastellamansur.com.br/",
}

VW = 390        # viewport width  (mobile)
VH = 844        # viewport height (mobile)
STEP = 790      # scroll step (ligeiro overlap para nao perder conteudo)
HDR = 36        # header strip height in pdf page

# ── capture scroll frames ─────────────────────────────────────────────────────
async def capture():
    from playwright.async_api import async_playwright
    frames = []
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        ctx = await browser.new_context(
            viewport={"width": VW, "height": VH},
            is_mobile=True,
            has_touch=True,
            user_agent=(
                "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) "
                "AppleWebKit/605.1.15 (KHTML, like Gecko) "
                "Version/15.0 Mobile/15E148 Safari/604.1"
            ),
        )
        page = await ctx.new_page()
        await page.goto(SITE["url"], wait_until="networkidle", timeout=45000)
        await page.wait_for_timeout(3000)

        # dismiss overlays
        try:
            await page.keyboard.press("Escape")
            await page.wait_for_timeout(300)
        except Exception:
            pass

        total_h = await page.evaluate(
            "Math.max(document.body.scrollHeight, document.documentElement.scrollHeight)"
        )
        scroll_w = await page.evaluate("document.documentElement.scrollWidth")
        print(f"Tamanho da pagina: {scroll_w}x{total_h}px")

        # Se o site renderiza mais largo que o viewport, centraliza horizontalmente
        scroll_x = max(0, (scroll_w - VW) // 2)
        print(f"Scroll horizontal: {scroll_x}px")

        scroll_y = 0
        while scroll_y < total_h:
            await page.evaluate(f"window.scrollTo({scroll_x}, {scroll_y})")
            await page.wait_for_timeout(400)
            # sem clip — captura exatamente o viewport visivel (390x844)
            raw = await page.screenshot()
            frames.append(base64.b64encode(raw).decode())
            scroll_y += STEP

        await browser.close()
    print(f"Frames capturados: {len(frames)}")
    return frames

frames = asyncio.run(capture())

# ── build HTML ────────────────────────────────────────────────────────────────
# page dimensions match mobile viewport (no scaling needed)
# 390px = 103.3mm | 844px = 223.7mm  (at 96dpi)
PAGE_W_MM = 103
PAGE_H_MM = 224   # header 36px + content 808px  (stays inside 844)

pages_html = []
total = len(frames)
for i, b64 in enumerate(frames):
    pages_html.append(f"""<div class="page">
  <div class="hdr">
    <div class="hdr-l">
      <span class="hdr-num">{SITE['num']}</span>
      <span class="hdr-name">{SITE['label']}</span>
      <span class="hdr-sep">&middot;</span>
      <span class="hdr-esp">{SITE['esp']}</span>
    </div>
    <div class="hdr-r">
      <span class="hdr-brand">RESULTIVA</span>
      <span class="hdr-pg">{i+1}&thinsp;/&thinsp;{total}</span>
    </div>
  </div>
  <div class="body">
    <img src="data:image/png;base64,{b64}" alt="frame {i+1}">
  </div>
</div>""")

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800;900&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{{margin:0;padding:0;box-sizing:border-box;}}
body{{
  font-family:'Montserrat',sans-serif;
  background:#999;
  -webkit-print-color-adjust:exact;
  print-color-adjust:exact;
}}
.page{{
  width:{PAGE_W_MM}mm;
  height:{PAGE_H_MM}mm;
  background:#fff;
  margin:0 auto 10px;
  overflow:hidden;
  display:flex;
  flex-direction:column;
  box-shadow:0 4px 24px rgba(0,0,0,.25);
}}
.hdr{{
  height:{HDR}px;
  background:#0C1829;
  display:flex;align-items:center;justify-content:space-between;
  padding:0 12px;flex-shrink:0;
}}
.hdr-l{{display:flex;align-items:center;gap:6px;min-width:0;}}
.hdr-num{{
  font-size:9px;font-weight:900;color:#1EC28B;
  background:rgba(30,194,139,.14);padding:2px 6px;border-radius:3px;flex-shrink:0;
}}
.hdr-name{{font-size:9px;font-weight:700;color:#fff;white-space:nowrap;}}
.hdr-sep{{color:rgba(255,255,255,.2);flex-shrink:0;}}
.hdr-esp{{font-size:7px;font-weight:400;color:rgba(255,255,255,.38);white-space:nowrap;}}
.hdr-r{{display:flex;align-items:center;gap:8px;flex-shrink:0;}}
.hdr-brand{{font-size:7px;font-weight:800;letter-spacing:3px;color:#1EC28B;text-transform:uppercase;}}
.hdr-pg{{font-size:7px;color:rgba(255,255,255,.3);}}
.body{{
  flex:1;overflow:hidden;min-height:0;
}}
.body img{{
  width:100%;
  height:100%;
  object-fit:cover;
  object-position:top left;
  display:block;
}}
@media print{{
  body{{background:white;}}
  .page{{
    margin:0;box-shadow:none;
    page-break-after:always;
    width:{PAGE_W_MM}mm;height:{PAGE_H_MM}mm;
  }}
}}
</style>
</head>
<body>
{"".join(pages_html)}
</body>
</html>"""

out_html = "site1-stella-v3.html"
with open(out_html, "w", encoding="utf-8") as f:
    f.write(html)
print(f"HTML gerado: {out_html}  ({total} paginas)")

# ── generate PDF ─────────────────────────────────────────────────────────────
async def make_pdf():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        html_path = os.path.abspath(out_html)
        await page.goto(f"file:///{html_path}", wait_until="networkidle")
        await page.wait_for_timeout(3000)
        out_pdf = "site1-stella-FINAL.pdf"
        await page.pdf(
            path=out_pdf,
            width=f"{PAGE_W_MM}mm",
            height=f"{PAGE_H_MM}mm",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        )
        await browser.close()
        size = os.path.getsize(out_pdf)
        print(f"PDF gerado: {out_pdf}  ({size/1024:.0f} KB)")

asyncio.run(make_pdf())
