# Ближайшие бары

Скрипт выводит самый большой, самый маленький и самый близкий бар из библиотеки баров г.Москвы - [с оф. сайта данных города Москвы]https://data.mos.ru/
Уже скачанные данные можно найти по ссылке: https://devman.org/media/filer_public/95/74/957441dc-78df-4c99-83b2-e93dfd13c2fa/bars.json 
Название скачанного файла нужно указать в методе load_data в переменной filepath

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5
Скрипт требует установки сторонних библотек: math, requests 

Запуск на Linux:

```bash

$ python script.py # possibly requires call of python3 executive instead of just python
# Пример ответа скрипта: 
MAX BAR:  {'geometry': {'coordinates': [37.638228501070095, 55.70111462948684], 'type': 'Point'}, 'properties': {'DatasetId': 1796,       'VersionNumber': 2, 'ReleaseNumber': 2, 'RowId': 'fbe6c340-4707-4d74-b7ca-2b84a23bf3a8', 'Attributes': {'global_id': 169375059, 'Name': 'Спорт бар «Красная машина»', 'IsNetObject': 'нет', 'OperatingCompany': None, 'AdmArea': 'Южный административный округ', 'District': 'Даниловский район', 'Address': 'Автозаводская улица, дом 23, строение 1', 'PublicPhone': [{'PublicPhone': '(905) 795-15-84'}], 'SeatsCount': 450, 'SocialPrivileges': 'нет'}}, 'type': 'Feature'}

MIN BAR:  {'geometry': {'coordinates': [37.35805920566864, 55.84614475898795], 'type': 'Point'}, 'properties': {'DatasetId': 1796, 'VersionNumber': 2, 'ReleaseNumber': 2, 'RowId': '17adc22c-5c41-4e4b-872f-815b521f2b53', 'Attributes': {'global_id': 20675518, 'Name': 'БАР. СОКИ', 'IsNetObject': 'нет', 'OperatingCompany': None, 'AdmArea': 'Северо-Западный административный округ', 'District': 'район Митино', 'Address': 'Дубравная улица, дом 34/29', 'PublicPhone': [{'PublicPhone': '(495) 258-94-19'}], 'SeatsCount': 0, 'SocialPrivileges': 'нет'}}, 'type': 'Feature'}

введите координатy: 44
введите координатy: 55
CLOSEST BAR:  {'geometry': {'coordinates': [36.900000000253, 55.303299999814], 'type': 'Point'}, 'properties': {'DatasetId': 1796, 'VersionNumber': 2, 'ReleaseNumber': 2, 'RowId': 'bb9eb30d-d16b-4821-8d9c-894b581ac762', 'Attributes': {'global_id': 281494712, 'Name': 'Staropramen', 'IsNetObject': 'нет', 'OperatingCompany': None, 'AdmArea': 'Центральный административный округ', 'District': 'Красносельский район', 'Address': 'Садовая-Спасская улица, дом 19, корпус 1', 'PublicPhone': [{'PublicPhone': '(985) 069-34-47'}], 'SeatsCount': 50, 'SocialPrivileges': 'нет'}}, 'type': 'Feature'}

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
