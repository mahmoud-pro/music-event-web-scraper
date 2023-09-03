import time
import requests as r
from selectolax.parser import HTMLParser
import sqlite3

connection = sqlite3.connect('data.db')

site_url = "http://programmer100.pythonanywhere.com/tours/"
HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0'}


def scrape(url):
    if not url:
        raise Exception("No search item found!")

    res = r.get(url, headers=HEADER)

    if res.status_code != 200:
        raise Exception("Get response error!")

    tree = HTMLParser(res.text)

    # tours = tree.css_first("div > h1.animated").text()
    temp = tree.css_first('#displaytimer').text(deep=True)

    # if temp != 'No upcoming tours':
    #     send_email()
    store_data(temp)

    return temp


# Store data to text file
def store_data(dt):
    with open('data.txt', 'a') as file:
        file.write(f"{dt} \n")


# store data to SQL database
def read_sql(dt):
    row = dt.split(',')
    row = [item.strip() for item in row]

    band, city, date = row

    cursor = connection.cursor()
    # Insert data to DB
    cursor.execute("INSERT INTO events VALUES(?,?,?)", (band, city, date))
    connection.commit()
    # Read data from DB
    cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
    rows = cursor.fetchall()
    return rows


if __name__ == "__main__":
    while True:
        scarped_data = scrape(site_url)

        if scarped_data != 'No upcoming tours':
            content = read_sql(scarped_data)
            print(scarped_data)

        time.sleep(2)
