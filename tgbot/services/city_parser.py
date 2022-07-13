import requests
from bs4 import BeautifulSoup

from tgbot.texts import answers


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
russian_url = "https://magio.ua/ru/support/servisnye-centry/"
Ukrainian_url = "https://magio.ua/support-page/service-centres/"


async def parse(url):
    try:
        html = requests.get(url, headers=headers)

        soup = BeautifulSoup(html.text, "lxml")

        city_list = soup.find("div", attrs={"class": "services-list"}).find_all("div", attrs={"class": "services-list_row"})

    except Exception:
        city_list = []

    return city_list


async def find_address(city_name):
    lang_list = [await parse(russian_url), await parse(Ukrainian_url)]

    text = answers["city_not_found"]
    try:
        for city_list in lang_list:
            for city in city_list:
                city_detail = city.find_all("div", attrs={"class": "services-list_row-item"})

                if city_detail:
                    found_city_name = city_detail[0].text
                    city_address = city_detail[1].text
                    service_center = city_detail[2].text

                    if city_name.lower() == found_city_name.lower():
                        text += answers["city_details"].format(found_city_name, city_address, service_center) + "\n"

    except Exception:
        text = answers["wrong"]


    return text


