from typing import TextIO

import requests

id = 100

def data_sql():
    global id
    response = requests.get('https://xn--riigiphad-v9a.ee/?output=json')
    print(response)
    responseJson = response.json()
    with open('data.sql', 'w' , encoding="utf-8") as f:
        for obj in responseJson:
        f.write((f'insert into Riigipyhad(id, date, title)\nvalues({id}, \'{obj["date"]}\', \'{obj["title"]}\')\n\n'))
        id += 1


    if __name__ == '__main__':
        data_sql()

