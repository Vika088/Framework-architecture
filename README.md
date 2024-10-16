# Framework-architecture
## **Дипломная работа. Архитектура фреймворка.**

### Задача: автоматизировать UI- и API-тесты из финальной работы по ручному тестированию.

Было составлено 5 UI тестов, составленных по функциональному чек-листу и 
5 API тестов, составленных на основе коллекции в Postman.

#### Продукт: сервис о кино “Кинопоиск” - крупнейший сервис о кино в рунете.

#### UI тесты направлены на функциональную проверку расширенного поиска фильмов:
1. Поиск по названию фильма
2. Поиск по году выпуска фильма
3. Поиск по стране
4. Поиск по прокатчику
5. Поиск по жанру фильма

#### API тесты направлены на проверку метода GET, чтобы убедиться, что он работает правильно и возвращает ожидаемые результаты.
1. Поиск по названию фильма
2. Поиск фильма по ID
3. Поиск по фильма  по актеру
4. Поиск по названию фильма с неправильными параметрами
5. Поиск фильма по несуществующему ID

Проект выполнялся в PyCharm - кроссплатформенной интегрированной среде разработки для языка программирования Python.
Запуск тестов производится командой _pytest_ с дальнейшей выгрузкой результатов командой _allure serve_ в Allure.

**Ссылка на проект в GitHub: https://github.com/Vika088/Framework-architecture.**