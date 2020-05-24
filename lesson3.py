from pprint import pprint
from pymongo import MongoClient
import pymongo
import json


client = MongoClient('localhost', 27017)
db = client['vacancy_db']
vacancies = db.vacancy
salary = int(input('Введите минимальную интересующую зарплату: '))

class Mongodb_fill():

    @classmethod
    def get_vacancy(cls):
        with open('vacancy_HH_SJ.json', encoding='utf8') as f:
            vacancy_full = json.load(f)
        return vacancy_full

    @classmethod
    def fill_first_db(cls, vacancy):
        if vacancies.estimated_document_count() == 0:
            return vacancies.insert_many(vacancy)

    @classmethod
    def vacancy_updater(cls):
        vacancy_full = cls.get_vacancy()
        cls.fill_first_db(vacancy_full)

        for item in vacancy_full:
            vacancies.update_one({'link': item['link']}, {'$set': item}, upsert=True)


    @classmethod
    def show_vacancy_params(cls):
        for vacancy in vacancies.find({'$and': [{'$or': [{'min_salary': {'$gte': salary}, 'max_salary': {'$gte': salary}}]}, {'currency': 'руб.'}]}):
            pprint(vacancy)


def main():
    db_update = Mongodb_fill()
    db_update.vacancy_updater()
    print(f'Вакансии с зарплатой выше {salary} рублей: ')
    db_update.show_vacancy_params()

main()
