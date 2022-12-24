import conf
import random
from random import randint
from faker import Faker
import json

# {
#     "model": "shop_final.book",
#     "pk": 1,
#     "fields": {
#         "title": "test_book",
#         "year": 2020,
#         "pages": 123,
#         "isbn13": "978-1-60487-647-5",
#         "rating": 5,
#         "price": 123456.0,
#         "author": [
#             "test_author_1",
#             "test_author_2"
#         ]
#     }
# }

def get_model() -> str:
    """
    Функция получает значение переменной MODEL из файла conf.py
    :return: значение переменный MODEL
    """
    model = conf.MODEL
    return model

# Cхалтурил на генераторе и получил значение счетчика в теле for функции main
# def get_pk(start_pk: int) -> int:
#     yield start_pk
#     start_pk += 1


def get_title(file_path='books.txt') -> str:
    """
    Получает случайное название книги из файла file_path
    :param file_path: расположение файла со списком книг
    :return: рандомное название книги
    """
    book_name = ""
    with open(file_path, 'r', encoding='utf-8') as f:
        book_list = [line for line in f]
        book_name = book_list[randint(0, len(book_list)-1)]
    return book_name


def get_year() -> int:
    """
    Генерирует случайное значение года выпуска книги
    :return: Случайный год выпуска
    """
    year = randint(1900, 2023)
    return year


def get_pages_number() -> int:
    """
    Генерирует случайное значение количества страниц
    :return: значение количества страниц
    """
    pages_number = randint(10, 1000)
    return pages_number


def get_isbn() -> str:
    """
    Генерирует случайное значение isbn книги
    :return: isbn книги
    """
    fake = Faker('ru_RU')
    isbn = fake.isbn13()
    return isbn


def get_rating() -> int:
    """
    Генерирует случайное значение рейтинга книги
    :return: рейтинг книги
    """
    rating = randint(0, 5)
    return rating


def get_price() -> float:
    """
    Генерирует случайное значение цены книги
    :return: цена книги
    """
    price = round(random.uniform(10, 10000), 1)
    return price


def get_author_list() -> list[str]:
    """
    Генерирует случайный список авторов переменной длины от 1 до 3
    :return: список авторов
    """
    fake = Faker('ru_RU')
    author_list = []
    for i in range(randint(1, 3)):
        true_false = random.choice([True, False])
        if true_false:
            first_name = fake.first_name_male()
            last_name = fake.last_name_male()
        else:
            first_name = fake.first_name_female()
            last_name = fake.last_name_female()

        author_list.append(" ".join([first_name, last_name]))
        i += 1
    return author_list


def main(start_pk: int) -> None:
    """
    Генерирует список словарей с данными о книги и записывает его в файл output.json
    :param start_pk: стартовое значение индекса книги в списке
    :return: None
    """
    with open('output.json', 'w') as f:
        json_list = []
        for i in range(100):
            json_dict = {
                "model": conf.MODEL,
                "pk": i+1+start_pk,
                "fields": {
                    "title": get_title(),
                    "year": get_year(),
                    "pages": get_pages_number(),
                    "isbn13": get_isbn(),
                    "rating": get_rating(),
                    "price": get_price(),
                    "author": get_author_list()
                }
            }
            json_list.append(json_dict)
        json.dump(json_list, f, ensure_ascii=False, indent=4)
    return None


if __name__ == '__main__':
    main(1)

