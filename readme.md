**О проекте**: API для клиентской части для форма с рецептами. Позволяет управлять своими рецептами и ставить отзывы другим рецептам. Так же есть поиск рецептов.

**Стэк используемых технологий:**
- Fraemwork: django rest framework
- Database: PostgreSQL
- Libraries for DB: psycopg2
- Library for tests: UnitTest
  
**Запуск приложения.**
1. Создать виртуальную среду и клонировать репозиторий.
2. Установить зависимости из requirements.txt
3. Добавить переменные среды: SECRET_KEY для Django, PASSWORD базы данных в settings.py, api_key для mistral_ai.py
4. Поднять PostgreSQL по порту 5432
5.  Запустить проект при помощи manage.py.