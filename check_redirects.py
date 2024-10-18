import requests

# 在这里添加你收藏的链接
urls = [
    "https://avsox.website/cn",
    "https://www.javdb6.com",
    "https://www.b49t.com",
    "https://www.busfan.club"
]

def check_urls(urls):
    results = []
    for url in urls:
        try:
            response = requests.get(url, allow_redirects=True, headers={"Cache-Control": "no-cache"})
            final_url = response.url.rstrip('/')
            original_url = url.rstrip('/')

            if response.history and final_url != original_url:
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
    return results

if __name__ == "__main__":
    results = check_urls(urls)
    with open("check_results.md", "w", encoding="utf-8") as f:
        for result in results:
            f.write(result + "\n")
