import requests
from bs4 import BeautifulSoup
import random

HEADERS = [
    {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"},
    {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
]

def get_price_history(url):
    headers = random.choice(HEADERS)
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception("获取页面失败，状态码: " + str(response.status_code))

    soup = BeautifulSoup(response.text, 'html.parser')

    price = None
    if "taobao.com" in url:
        price = soup.select_one(".tm-price").text if soup.select_one(".tm-price") else "价格不可用"
    elif "jd.com" in url:
        price = soup.select_one(".p-price > span").text if soup.select_one(".p-price > span") else "价格不可用"

    return {"url": url, "price": price}
