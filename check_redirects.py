import requests
from urllib.parse import urlsplit
import time

# 在这里添加你收藏的链接
urls = [
    "https://answers.microsoft.com/zh-hans/microsoftedge/forum/all/%E6%80%8E%E4%B9%88%E6%8A%8Aedge%E7%9A%84%E7%94%A8/78f4615d-c41b-4145-b42b-b718b32d98e8",
    "https://www.qbittorrent.org",
    "https://zhuanlan.zhihu.com/p/550722045",
    "https://zhuanlan.zhihu.com/p/000000000"
]

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    "Referer": "https://www.google.com",
    "DNT": "1",
    "Upgrade-Insecure-Requests": "1",
    "Accept-Language": "zh-CN,en;q=0.9"
}

def get_base_url(url):
    return "{0.scheme}://{0.netloc}{0.path}".format(urlsplit(url))

def check_urls(urls):
    results = []
    session = requests.Session()
    for url in urls:
        try:
            response = session.get(url, allow_redirects=True, headers=headers)
            final_base_url = get_base_url(response.url).rstrip('/')
            original_base_url = get_base_url(url).rstrip('/')
            if response.history and final_base_url != original_base_url:
                redirect_info = f"{url} (· 重定向到 {response.url} ·)\n(· 重定向过程"
                for resp in response.history:
                    redirect_info += f" ---> 状态码: {resp.status_code}, URL: {resp.url}"
                redirect_info += f" ---> 最终请求状态码: {response.status_code}, URL: {response.url} ·)"
                results.append(redirect_info)
            elif response.status_code != 200:
                results.append(f"{url} (· 无效，状态码: {response.status_code} ·)")
            # 注释掉正常的输出
            # elif response.status_code == 200:
            #     results.append(f"{url} (· 有效 ·)")
        except requests.RequestException as e:
            results.append(f"{url} (· 检查时出错: {e} ·)")
        time.sleep(2)  # 每次请求之间添加2秒的延迟
    return results

if __name__ == "__main__":
    results = check_urls(urls)
    with open("check_results.md", "w", encoding="utf-8") as f:
        for result in results:
            f.write(result + "\n")
