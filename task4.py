import re
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
HEADERS = {"User-Agent": "Mozilla/5.0"}


def get_soup(url):
    r = requests.get(url, headers=HEADERS)
    r.raise_for_status()
    return BeautifulSoup(r.text, "html.parser")


def get_page_count(url):
    soup = get_soup(url)
    pag = soup.select_one("ul.pagination")
    nums = []
    if not pag:
        return 1

    for a in pag.select("a"):
        if a.get_text(strip=True).isdigit():
            nums.append(int(a.get_text(strip=True)))

    return max(nums)


def parse_list_page(url):
    soup = get_soup(url)
    items = soup.select("div.product-wrapper") or soup.select("div.thumbnail")
    laptops = []
    for it in items:
        title = it.select_one("a.title")
        price = it.select_one("h4.price")
        desc = it.select_one("p.description")
        rc = it.select_one("p.review-count") or it.select_one(".pull-right")
        txt = rc.get_text(" ", strip=True) if rc else ""
        m = re.search(r"\d+", txt)
        reviews = int(m.group()) if m else 0
        pr = it.select_one(".ratings p[data-rating]")
        if pr and pr.has_attr("data-rating") and pr["data-rating"].isdigit():
            rating = int(pr["data-rating"])
        else:
            stars = it.select(".ratings .glyphicon.glyphicon-star")
            rating = len(stars) if stars else None
        laptops.append({
            "title": title.get_text(strip=True) if title else None,
            "price": price.get_text(strip=True) if price else None,
            "short_description": desc.get_text(strip=True) if desc else None,
            "reviews": reviews,
            "rating": rating
        })
    return laptops


def scrape_all_laptops():
    pages = get_page_count(BASE_URL)
    all_rows = []
    for p in range(1, pages + 1):
        url = BASE_URL if p == 1 else f"{BASE_URL}?page={p}"
        all_rows.extend(parse_list_page(url))
    return all_rows


laptops = scrape_all_laptops()
print("Зібрано:", len(laptops))
for laptop in laptops:
    print(laptop)
