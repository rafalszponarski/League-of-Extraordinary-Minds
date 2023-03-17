from requests import post
from json import loads
from os import mkdir


PATH = "C:/Users/rafal/Desktop/LNU"
URL = "https://edu.t-lem.com/"
MAIL = ""  # Zmień to
PASSWORD = ""  # Zmień to
COOKIE = post(URL, data={"act[module]": "auth", "act[cmd]": "login", "act[params][login]": MAIL, "act[params][pass]": PASSWORD}).cookies.get("LNU_SESSION")
HEADERS = {
    "Host": "edu.t-lem.com",
    f"Cookie": f"LNU_SESSION={COOKIE}",
    #"Content-Length": "",
    "Sec-Ch-Ua": "\"Chromium\";v=\"111\", \"Not(A:Brand\";v=\"8\"",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.65 Safari/537.36",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Origin": "https://edu.t-lem.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://edu.t-lem.com/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "close"
}

main = post(URL, headers=HEADERS, data="act%5Bid%5D=menus&act%5Bmodule%5D=menus&act%5Bparams%5D%5B%5D=get").content

for language in {"Python": 2}.values():
    MODULE = loads(main)['data']['menus'][1]['submenus'][language]
    module_title = MODULE['title'].split()[-1]  # np. Język Python
    mkdir(f"{PATH}/{module_title}")

    for exp in {"Podstawa": 0, "Rozszerzenie": 1}.values():
        LEVEL = MODULE['submenus'][exp]
        level_title = LEVEL['title']  # np. Poziom Podstawowy
        mkdir(f"{PATH}/{module_title}/{level_title}")

        for topic_num in range(len(LEVEL['submenus'])):
            TOPIC = LEVEL['submenus'][topic_num]
            topic_title = TOPIC['title']  # np. Zmienne i stringi
            mkdir(f"{PATH}/{module_title}/{level_title}/{topic_title}")

            for task_num in range(len(TOPIC['submenus'])):
                TASK = TOPIC['submenus'][task_num]
                task_title = TASK['title'].replace(":", "").replace("?", "").replace("..", "").replace("/", " ").strip()
                print(f"{module_title} --> {level_title} --> {topic_title} --> {task_title}")

                page = post(URL, headers=HEADERS, data=f"act%5Bid%5D=lekcja&act%5Bmodule%5D=lekcja&act%5Bparams%5D%5B%5D=get&act%5Bparams%5D%5B%5D={TASK['id']}").content

                if "quiz" not in loads(page)['data']['lekcja']['s_tytul'].lower():

                    files = loads(page)['data']['lekcja']['t_code']['files']
                    for file in files:
                        if not file['readOnly']:
                            with open(f"{PATH}/{module_title}/{level_title}/{topic_title}/{task_title}.py", 'w') as save:
                                save.write(file['code'])

print("\nFinished!")
