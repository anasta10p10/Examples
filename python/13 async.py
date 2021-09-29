# Assignment.1
# Выполнить асинхронный парсинг сайта.
# Сравнить время выполнения скрипта с его синхронной версией
# Для асинхронной версии requests не подойдет, т.к. она блокирующая.
# Нужно использовать aiohttp

import json
import time

from requests.sessions import session
import aiohttp
import asyncio
from bs4 import BeautifulSoup
import datetime
import csv


start_time = time.time()
async def pages():
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
    }

    url = "https://www.labirint.ru/genres/2308/?available=1&paperbooks=1&display=table"
    session =  aiohttp.ClientSession()
    response = await session.get(url=url, headers=headers)
    response = await response.content.read()
    response=response.decode('utf-8')
    soup = BeautifulSoup(response, "lxml")

    pages_count = int(soup.find("div", class_="pagination-numbers").find_all("a")[-1].text)
    # print(pages_count)
    return pages_count, session

async def get_data(page, pages_count, session):
    cur_time = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M")

    with open(f"data/labirint_{cur_time}.csv", "w", newline="", encoding="utf8") as file:
        writer = csv.writer(file)

        writer.writerow(
            (
                "Название книги",
                "Автор",
                "Издательство",
                "Цена со скидкой",
                "Цена без скидки",
                "Процент скидки",
                "Наличие на складе"
            )
        )

    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
    }

    url = "https://www.labirint.ru/genres/2308/?available=1&paperbooks=1&display=table"

    # response = aiohttp.ClientSession().get(url=url, headers=headers)
    # soup = BeautifulSoup(response.text, "lxml")

    # pages_count = int(soup.find("div", class_="pagination-numbers").find_all("a")[-1].text)

    books_data = []
    # for page in range(1, pages_count + 1):
    # for page in range(1, 2):
    url = f"{url}&page={page}"

    response = await session.get(url=url, headers=headers)
    response = await response.content.read()
    response=response.decode('utf-8')

    soup = BeautifulSoup(response, "lxml")

    books_items = soup.find("tbody", class_="products-table__body").find_all("tr")

    for bi in books_items:
        book_data = bi.find_all("td")

        try:
            book_title = book_data[0].find("a").text.strip()
        except:
            book_title = "Нет названия книги"

        try:
            book_author = book_data[1].text.strip()
        except:
            book_author = "Нет автора"

        try:
            # book_publishing = book_data[2].text
            book_publishing = book_data[2].find_all("a")
            book_publishing = ":".join([bp.text for bp in book_publishing])
        except:
            book_publishing = "Нет издательства"

        try:
            book_new_price = int(book_data[3].find("div", class_="price").find("span").find("span").text.strip().replace(" ", ""))
        except:
            book_new_price = "Нет нового прайса"

        try:
            book_old_price = int(book_data[3].find("span", class_="price-gray").text.strip().replace(" ", ""))
        except:
            book_old_price = "Нет старого прайса"

        try:
            book_sale = round(((book_old_price - book_new_price) / book_old_price) * 100)
        except:
            book_sale = "Нет скидки"

        try:
            book_status = book_data[-1].text.strip()
        except:
            book_status = "Нет статуса"

        # print(book_title)
        # print(book_author)
        # print(book_publishing)
        # print(book_new_price)
        # print(book_old_price)
        # print(book_sale)
        # print(book_status)
        # print("#" * 10)

        books_data.append(
            {
                "book_title": book_title,
                "book_author": book_author,
                "book_publishing": book_publishing,
                "book_new_price": book_new_price,
                "book_old_price": book_old_price,
                "book_sale": book_sale,
                "book_status": book_status
            }
        )

        with open(f"data/labirint_{cur_time}.csv", "a", newline="", encoding="utf8") as file:
            writer = csv.writer(file)

            writer.writerow(
                (
                    book_title,
                    book_author,
                    book_publishing,
                    book_new_price,
                    book_old_price,
                    book_sale,
                    book_status
                )
            )

    print(f"Обработана {page}/{pages_count}")
    await asyncio.sleep(1)

    with open(f"data/labirint_{cur_time}.json", "w", encoding="utf8") as file:
        json.dump(books_data, file, indent=4, ensure_ascii=False)


async def main():
    x, session=await pages()
    await asyncio.gather(*(get_data(i, x, session) for i in range(1,x+1)))
    finish_time = time.time() - start_time
    print(f"Затраченное на работу скрипта время: {finish_time}")
    await session.close()


if __name__ == '__main__':
    asyncio.run(main())