import asyncio
from playwright.async_api import async_playwright

# 在这里添加你收藏的链接
urls = [
    "https://github.com/233boy/v2ray",
    "https://learn.microsoft.com/zh-cn/windows-server/get-started/kms-client-activation-keys",
    "https://learn.microsoft.com/zh-cn/deployoffice/vlactivation/gvlks",
    "https://learn.microsoft.com/zh-CN/cpp/windows/latest-supported-vc-redist?view=msvc-170",
    "https://learn.microsoft.com/zh-cn/windows-hardware/manufacture/desktop/clean-up-the-winsxs-folder",
    "https://learn.microsoft.com/zh-cn/windows/deployment/upgrade/windows-edition-upgrades",
    "https://learn.microsoft.com/zh-cn/windows-hardware/manufacture/desktop/dism-windows-edition-servicing-command-line-options",
    "https://learn.microsoft.com/zh-cn/windows-hardware/design/device-experiences/powercfg-command-line-options",
    "https://tonkiang.us",
    "https://github.com/iptv-org/iptv",
    "https://github.com/fanmingming/live",
    "https://live.fanmingming.com/tv/m3u/ipv6.m3u",
    "https://www.microsoft.com/zh-cn/edge/business",
    "https://www.google.com/intl/zh-CN/chrome/?standalone=1&platform=win",
    "https://www.google.com/intl/zh-CN/chrome/?standalone=1&platform=win64",
    "https://pan.baidu.com/s/1cSkNVFOS4pi6XesaRFUwyQ",
    "https://www.microsoft.com/zh-cn/software-download/home",
    "https://www.microsoft.com/en-us/software-download/windowsinsiderpreviewiso",
    "https://www.microsoft.com/zh-cn/evalcenter/download-windows-10-enterprise",
    "https://www.microsoft.com/zh-cn/evalcenter/download-windows-11-enterprise",
    "https://answers.microsoft.com/zh-hans/microsoftedge/forum/all/%E6%80%8E%E4%B9%88%E6%8A%8Aedge%E7%9A%84%E7%94%A8/78f4615d-c41b-4145-b42b-b718b32d98e8",
    "https://www.microsoft.com/en-us/download/details.aspx?id=25250",
    "https://kukusun.github.io/blog/download/38/Windows_PolicySettings.xlsx",
    "https://download.microsoft.com/download/F/2/2/F22D5FDB-59CD-4275-8C95-1BE17BF70B21/wushowhide.diagcab",
    "https://kukusun.github.io/blog/download/47/wushowhide.diagcab",
    "https://httpd.apache.org",
    "https://github.com/Wind4/vlmcsd",
    "https://github.com/massgravel/Microsoft-Activation-Scripts",
    "https://github.com/TGSAN/CMWTAT_Digital_Edition",
    "https://github.com/zbezj/HEU_KMS_Activator",
    "https://hexo.io",
    "https://github.com/Shen-Yu/hexo-theme-ayer",
    "https://git-scm.com",
    "https://nodejs.org",
    "https://github.com/shen-yu/hexo-theme-ayer",
    "https://github.com/xcodebuild/hexo-asset-image",
    "https://github.com/wzpan/hexo-generator-search",
    "https://github.com/D0n9X1n/hexo-blog-encrypt",
    "https://github.com/rozbo/hexo-abbrlink",
    "https://blog.csdn.net/Copanko/article/details/105428249",
    "https://github.com/hexojs/hexo-deployer-git",
    "https://www.cnblogs.com/wutou/p/14302569.html",
    "https://www.zhihu.com/question/34541107",
    "https://snapdrop.net",
    "https://github.com/RobinLinus/snapdrop",
    "https://transfer.zip",
    "https://github.com/robinkarlberg/transfer.zip-web",
    "https://deershare.com",
    "https://github.com/fanchangyong/deershare",
    "https://www.ppzhilian.com",
    "https://github.com/FelisCatus/SwitchyOmega",
    "https://zhuanlan.zhihu.com/p/550722045",
    "https://www.qbittorrent.org",
    "https://github.com/qbittorrent/qBittorrent",
    "https://github.com/c0re100/qBittorrent-Enhanced-Edition",
    "https://www.bitcomet.com/cn",
    "https://www.bitcomet.com/cn/archive",
    "https://motrix.app/zh-CN",
    "https://github.com/agalwood/Motrix",
    "https://transmissionbt.com",
    "https://github.com/transmission/transmission",
    "https://github.com/ohroy/hexo-neat",
    "https://github.com/lxl80/hexo-admonition",
    "https://blog.csdn.net/mtj66/article/details/74959287",
    "https://blog.csdn.net/ARPOSPF/article/details/112163281",
    "https://zhuanlan.zhihu.com/p/405968623",
    "https://adblockplus.org/zh_CN",
    "https://adguard.com/zh_cn/adguard-browser-extension/overview.html",
    "https://github.com/AdguardTeam/AdguardBrowserExtension",
    "https://github.com/polywock/globalSpeed",
    "https://potplayer.tv",
    "https://potplayer.app",
    "https://potplayer.daum.net",
    "https://github.com/1Panel-dev/1Panel",
    "https://github.com/studyzy/imewlconverter",
    "https://github.com/zhimin-dev/iptv-checker",
    "https://github.com/Aira-Sakuranomiya/CleanFlashInstaller",
    "https://gitlab.com/cleanflash/installer",
    "https://github.com/Stirling-Tools/Stirling-PDF",
    "https://github.com/NaiboWang/EasySpider",
    "https://github.com/BluePointLilac/ContextMenuManager",
    "https://github.com/mifi/lossless-cut",
    "https://github.com/Vanessa219/vditor",
    "https://github.com/gildas-lormeau/SingleFile",
    "https://github.com/hiroi-sora/Umi-OCR",
    "https://github.com/nxtrace/NTrace-core",
    "https://github.com/Archeb/opentrace",
    "https://github.com/nxtrace/NextTraceroute",
    "https://github.com/rustdesk/rustdesk",
    "https://github.com/localsend/localsend",
    "https://github.com/hellzerg/optimizer",
    "https://github.com/Code52/carnac",
    "https://github.com/taojy123/KeymouseGo",
    "https://zhuanlan.zhihu.com/p/000000000",
    "https://github.com/xiaoxinpro/ChineseSubtitleConversionTool"
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
