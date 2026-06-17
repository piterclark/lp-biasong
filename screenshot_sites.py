import asyncio
from playwright.async_api import async_playwright
import os

sites = [
    {"name": "stella", "url": "https://psicologastellamansur.com.br/"},
    {"name": "karine", "url": "https://karinemoraes.com/lp/psicoterapia-online/"},
    {"name": "rafaela", "url": "https://psirafaelabeloti.com.br/"},
    {"name": "nathalia", "url": "https://dranathaliamorato.com.br/"},
    {"name": "rosangela", "url": "https://rosangelaalvimcassimiro.com/"},
]

out_dir = "psi-screenshots"
os.makedirs(out_dir, exist_ok=True)

async def screenshot_site(page, site):
    print(f"Capturando: {site['url']}")
    try:
        await page.goto(site["url"], wait_until="networkidle", timeout=30000)
        await page.wait_for_timeout(2000)
        await page.screenshot(path=f"{out_dir}/{site['name']}.png", full_page=False, clip={"x": 0, "y": 0, "width": 1280, "height": 800})
        print(f"  OK {site['name']}.png salvo")
    except Exception as e:
        print(f"  ERRO em {site['name']}: {e}")

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1280, "height": 800})
        for site in sites:
            await screenshot_site(page, site)
        await browser.close()
    print("\nTodos os screenshots concluidos!")

asyncio.run(main())
