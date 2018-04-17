# Ближайшие бары

Скрипт выводит самый большой, самый маленький и самый близкий бар из библиотеки баров г.Москвы - https://data.mos.ru/

Уже скачанные данные можно найти по ссылке: https://devman.org/media/filer_public/95/74/957441dc-78df-4c99-83b2-e93dfd13c2fa/bars.json 

Скачанный файл стоит поместить в корневую папку, и указать просто его название.

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash

$ python script.py # possibly requires call of python3 executive instead of just python

Пример ответа скрипта: 

введите путь к файлу: bars.json
САМЫЙ БОЛЬШОЙ БАР:
{
    "geometry": {
        "coordinates": [
            37.638228501070095,
            55.70111462948684
        ],
        "type": "Point"
    },
    "properties": {
        "Attributes": {
            "Address": "Автозаводская улица, дом 23, строение 1",
            "AdmArea": "Южный административный округ",
            "District": "Даниловский район",
            "IsNetObject": "нет",
            "Name": "Спорт бар «Красная машина»",
            "OperatingCompany": null,
            "PublicPhone": [
                {
                    "PublicPhone": "(905) 795-15-84"
                }
            ],
            "SeatsCount": 450,
            "SocialPrivileges": "нет",
            "global_id": 169375059
        },
        "DatasetId": 1796,
        "ReleaseNumber": 2,
        "RowId": "fbe6c340-4707-4d74-b7ca-2b84a23bf3a8",
        "VersionNumber": 2
    },
    "type": "Feature"
}

ЕСЛИ ПРИ ПРОСЬБЕ ПРОГРАММЫ ВВЕСТИ ВАШИ КООРДИНАТЫ ВЫ ВВЕДЕТЕ НЕ ЧИСЛО, СРАБОТАЕТ ИСКЛЮЧЕНИЕ:

введите координатy: j
ЭТО ИСКЛЮЧЕНИЕ: ВЫ ВВЕЛИ НЕ ЧИСЛО!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Traceback (most recent call last):
  File "bars.py", line 67, in <module>
    get_closest_bar(data, get_bar_coordinate(), get_bar_coordinate())
  File "bars.py", line 37, in get_bar_coordinate
    return coordinate
UnboundLocalError: local variable 'coordinate' referenced before assignment

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
