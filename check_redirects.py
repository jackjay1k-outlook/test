import asyncio
from playwright.async_api import async_playwright

# 在这里添加你收藏的链接
urls = [
    "https://answers.microsoft.com/zh-hans/microsoftedge/forum/all/%E6%80%8E%E4%B9%88%E6%8A%8Aedge%E7%9A%84%E7%94%A8/78f4615d-c41b-4145-b42b-b718b32d98e8",
    "https://www.qbittorrent.org",
    "https://zhuanlan.zhihu.com/p/550722045",
    "https://zhuanlan.zhihu.com/p/000000000"
]

async def check_urls(urls):
    results = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()

        for url in urls:
            try:
                page = await context.new_page()
                await page.goto(url)
                await page.wait_for_load_state('networkidle')
                status_code = await page.evaluate("() => document.readyState")
                if status_code == "complete":
                    results.append(f"{url} (· 有效 ·)")
                else:
                    results.append(f"{url} (· 无效，加载未完成 ·)")
            except Exception as e:
                results.append(f"{url} (· 检查时出错: {e} ·)")

        await browser.close()
    return results

if __name__ == "__main__":
    results = asyncio.run(check_urls(urls))
    with open("check_results.md", "w", encoding="utf-8") as f:
        for result in results:
            f.write(result + "\n")
