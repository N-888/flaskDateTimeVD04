"""
app.py - ГЛАВНЫЙ ФАЙЛ ПРИЛОЖЕНИЯ
Это мозг нашего приложения. Он управляет всем, что происходит на сайте.
"""

# Импортируем нужные инструменты из библиотек:
# from библиотека import инструмент1, инструмент2

# Flask - это главная библиотека для создания сайтов
# render_template - умеет показывать HTML страницы
# jsonify - умеет создавать ответы в формате JSON (как для API)
from flask import Flask, render_template, jsonify

# datetime - встроенная библиотека Python для работы с датой и временем
from datetime import datetime

# pytz - библиотека для работы с часовыми поясами (Москва, Нью-Йорк и т.д.)
import pytz

# СОЗДАЕМ ПРИЛОЖЕНИЕ:
# app - это наше главное приложение, как двигатель у машины
# __name__ - говорит Flask, где искать файлы (шаблоны, картинки и т.д.)
app = Flask(__name__)

# НАСТРОЙКИ:
# TIMEZONE - переменная, где хранится наш часовой пояс
# 'Europe/Moscow' - это Москва, UTC+3
# Можно поменять на: 'America/New_York' (Нью-Йорк) или 'Asia/Tokyo' (Токио)
TIMEZONE = 'Europe/Moscow'

# СОЗДАЕМ СТРАНИЦЫ САЙТА:

# Страница 1: Главная страница (как входная дверь в дом)
# @app.route('/') - говорит: "Когда кто-то зайдет на главную страницу (/), сделай следующее:"
@app.route('/')
def index():
    """
    index() - функция, которая работает, когда открывают главную страницу
    Она собирает информацию о времени и показывает красивую страницу
    """

    # Шаг 1: Берем правильный часовой пояс (например, Московское время)
    tz = pytz.timezone(TIMEZONE)

    # Шаг 2: Узнаем, КОТОРЫЙ СЕЙЧАС ЧАС в этом часовом поясе
    now = datetime.now(tz)

    # Шаг 3: Делаем красивые надписи из времени:

    # Время в формате "14:30:45" (часы:минуты:секунды)
    current_time = now.strftime("%H:%M:%S")

    # Дата в формате "01 января 2024" (число месяц год)
    current_date = now.strftime("%d %B %Y")

    # День недели: "Понедельник", "Вторник" и т.д.
    current_weekday = now.strftime("%A")

    # Дополнительные форматы (на всякий случай):
    time_24h = now.strftime("%H:%M")        # "14:30" (без секунд)
    time_12h = now.strftime("%I:%M %p")     # "02:30 PM" (американский формат)
    date_short = now.strftime("%d/%m/%Y")   # "01/01/2024"
    iso_date = now.strftime("%Y-%m-%d")     # "2024-01-01" (как в компьютерах)

    # Разбираем время на кусочки (для красивых цифр на сайте):
    hour = now.hour      # Часы (14)
    minute = now.minute  # Минуты (30)
    second = now.second  # Секунды (45)
    day = now.day        # День (1)
    month = now.month    # Месяц (1)
    year = now.year      # Год (2024)

    # Unix timestamp - сколько секунд прошло с 1 января 1970 года
    # Компьютеры любят такие числа
    timestamp = int(now.timestamp())

    # Шаг 4: Показываем красивую страницу со всей этой информацией
    # render_template - как художник, который рисует страницу
    # 'index.html' - имя файла с чертежом страницы
    # После запятой - все данные, которые нужно вставить на страницу
    return render_template(
        'index.html',
        time=current_time,
        date=current_date,
        weekday=current_weekday,
        timezone=TIMEZONE,
        time_24h=time_24h,
        time_12h=time_12h,
        date_short=date_short,
        iso_date=iso_date,
        hour=hour,
        minute=minute,
        second=second,
        day=day,
        month=month,
        year=year,
        timestamp=timestamp
    )

# Страница 2: API для времени (как окошко для роботов)
# Роботы (JavaScript) могут сюда заходить и получать время в формате JSON
@app.route('/api/current_time')
def api_current_time():
    """
    api_current_time() - дает время в формате для компьютеров (JSON)
    Нужно для того, чтобы время обновлялось без перезагрузки страницы
    """

    # Делаем то же самое, что и для главной страницы:
    tz = pytz.timezone(TIMEZONE)
    now = datetime.now(tz)

    # Но возвращаем не HTML страницу, а JSON данные:
    # JSON - это как язык общения между сайтом и JavaScript
    return jsonify({
        'time': now.strftime("%H:%M:%S"),
        'date': now.strftime("%d %B %Y"),
        'weekday': now.strftime("%A"),
        'timezone': TIMEZONE,
        'timestamp': int(now.timestamp()),
        'iso': now.isoformat()
    })

# Страница 3: Проверка здоровья (как доктор для сайта)
@app.route('/health')
def health_check():
    """
    health_check() - как сказать: "Я жив и здоров!"
    Системы мониторинга проверяют эту страницу, чтобы знать, работает ли сайт
    """

    return jsonify({
        'status': 'healthy',
        'service': 'Flask DateTime App VD04',
        'timestamp': datetime.now().isoformat()
    })

# Страница 4: Информация о приложении (как паспорт)
@app.route('/about')
def about():
    """
    about() - рассказывает о нашем приложении
    Показывает, что умеет делать наше приложение
    """

    return jsonify({
        'application': 'Flask DateTime Display VD04',
        'description': 'Приложение для красивого показа времени',
        'version': '1.0.0',
        'author': 'Flask Developer'
    })

# ЗАПУСК ПРИЛОЖЕНИЯ:
# Этот код срабатывает ТОЛЬКО когда мы запускаем файл напрямую
if __name__ == '__main__':
    """
    Это КНОПКА ПУСК для нашего приложения
    Когда мы говорим "python app.py", запускается этот код
    """

    # app.run() - запускает веб-сервер (как включаем двигатель)
    # debug=True - режим отладки (видим ошибки, автообновление)
    # port=5000 - порт 5000 (как дверь номер 5000)
    # host='0.0.0.0' - пускаем всех в гости (можно зайти с других устройств)
    app.run(debug=True, port=5000)