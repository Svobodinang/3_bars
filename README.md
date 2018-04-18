# Ближайшие бары

Скрипт выводит самый большой, самый маленький и самый близкий бар из библиотеки баров г.Москвы - https://data.mos.ru/

Уже скачанные данные можно найти по ссылке: https://devman.org/media/filer_public/95/74/957441dc-78df-4c99-83b2-e93dfd13c2fa/bars.json 

Скачанный файл стоит поместить в корневую папку, и указать его название.

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5 и выше

Запуск на Linux:

```bash

$ python bars.py <"название фала  с данными".json># possibly requires call of python3 executive instead of just python

Пример ответа скрипта: 

C:\Users\svobodinang\Desktop\Python\3_bars>python bars.py a.json
САМЫЙ БОЛЬШОЙ БАР:
"Спорт бар «Красная машина»"
САМЫЙ МАЛЕНЬКИЙ БАР:
"БАР. СОКИ"
БЛИЖАЙШИЙ БАР:
введите координатy: 77
введите координатy: 55
"Staropramen"

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
