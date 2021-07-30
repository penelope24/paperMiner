import requests
from selenium import webdriver


class RequestMask:

    def __init__(self, request):
        self.request = request

    @staticmethod
    def visit_httpbin():
        url = 'https://httpbin.org/headers'
        response = requests.get(url)
        if response.status_code == 200:
            print(response.text)

    @staticmethod
    def make_mask_header():
        my_headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "authority": "dl.acm.org",
            "Sec-Ch-Ua": "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
            "X-Amzn-Trace-Id": "Root=1-6103a2df-6139eb7d4f3df899562b89ff",
            "Referer": "https://doi.org"
        }
        return my_headers


if __name__ == "__main__":
    # RequestMask.visit_httpbin()

    proxy = {
        'http': 'http://58.58.213.55:8888',
        'https': 'http://58.58.213.55:8888'
    }

    url = "https://doi.org/10.1145/1368088.1368206"
    httpbin = "https://httpbin.org/headers"
    # brose = webdriver.Chrome(executable_path="C:\\Users\\fy\\Desktop\\icses\\chromedriver.exe")
    # brose.get(httpbin)
    # print(brose.page_source)
    # brose.close()
    headers = {"Referer": url}
    response = requests.get(url, headers=my_headers)
    print(response.text)