from db_manager import DatabaseManager
from search import search_by_keyword, search_by_genre_and_year, search_by_actor_last_name
from display import display_results

def main():
    try:
        db = DatabaseManager(host='ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com', user='ich1', password='password', database='sakila')
    except Exception as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return

    try:
        while True:
            print("\nДоступные команды:")
            print("1. Поиск по ключевому слову")
            print("2. Поиск по жанру и году")
            print("3. Поиск по актерским фамилиям")
            print("4. Популярные запросы")
            print("5. Выход")
            choice = input("Введите команду: ")

            if choice == "1":
                keyword = input("Введите ключевое слово: ")
                try:
                    results = search_by_keyword(db, keyword)
                    display_results(results)
                except Exception as e:
                    print(f"Ошибка выполнения поиска по ключевому слову: {e}")
            elif choice == "2":
                genre = input("Введите жанр: ")
                year = input("Введите год: ")
                try:
                    results = search_by_genre_and_year(db, genre, year)
                    display_results(results)
                except Exception as e:
                    print(f"Ошибка выполнения поиска по жанру и году: {e}")
            elif choice == "3":
                last_name = input("Введите актерскую фамилию: ")
                try:
                    results = search_by_actor_last_name(db, last_name)
                    display_results(results)
                except Exception as e:
                    print(f"Ошибка выполнения поиска по актерским фамилиям: {e}")
            elif choice == "4":
                try:
                    popular_queries = db.get_popular_queries()
                    for row in popular_queries:
                        print(f"{row['query_text']} - {row['total_searches']} запросов")
                except Exception as e:
                    print(f"Ошибка выполнения запроса популярных запросов: {e}")
            elif choice == "5":
                print("Выход из программы.")
                break
            else:
                print("Неверная команда!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    main()
