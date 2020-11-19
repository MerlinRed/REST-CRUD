import sqlite3
from sqlite3 import Error


class CRUD:

    def __init__(self):
        self.connection = sqlite3.connect('Rest_Crud.db')
        self.cursor = self.connection.cursor()

    def create(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS records(
                id Integer PRIMARY KEY AUTOINCREMENT,
                name char(30) not null,'
                self_records text not null default "text")""")
        self.connection.commit()

    def insert(self, user_input):
        self.cursor.execute('INSERT INTO records(name, self_records) VALUES(?, ?)', user_input)
        self.connection.commit()

    def insert_input(self):
        value_1 = input('Ваше имя: ')
        value_2 = input('Ваша запись: ')
        user_input = (value_1, value_2)
        return user_input

    def update_name(self, user_input):
        self.cursor.execute('UPDATE records SET name = ? WHERE id = ?', user_input)
        self.connection.commit()

    def update_input_name(self):
        value_2 = input('Введите ID записи которую нужно изменить: ')
        value_1 = input('Введите новое имя: ')
        user_input = (value_1, int(value_2))
        return user_input

    def update_text(self, user_input):
        self.cursor.execute('UPDATE records SET self_records = ? WHERE id = ?', user_input)
        self.connection.commit()

    def update_input_text(self):
        value_2 = input('Введите ID записи которую нужно изменить: ')
        value_1 = input('Введите новый текст: ')
        user_input = (value_1, int(value_2))
        return user_input

    def select(self):
        self.cursor.execute('SELECT * FROM records')
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def delete(self, user_input):
        self.cursor.execute('DELETE FROM records WHERE id = ?', user_input)
        self.connection.commit()

    def delete_input(self):
        user_input = input('Введите номер удаляемой записи: ')
        return user_input

    def exit(self):
        self.connection.close()
        exit()


class DataBaseWorker:

    def __init__(self):
        self.work_with_db = CRUD()

    def create(self):
        self.work_with_db.create()
        print('Таблица готова к работе')

    def insert(self):
        try:
            self.work_with_db.insert(user_input=self.work_with_db.insert_input())
        except Error:
            print('Ошибка при вставке данных в таблицу')

    def update_name(self):
        # нужно указать номер обновляемой записи
        try:
            self.work_with_db.update_name(user_input=self.work_with_db.update_input_name())
        except Error:
            print('Ошибка при обновление таблицы')

    def update_text(self):
        # нужно указать номер обновляемой записи
        try:
            self.work_with_db.update_text(user_input=self.work_with_db.update_input_text())
        except Error:
            print('Ошибка при обновление таблицы')

    def select(self):
        try:
            self.work_with_db.select()
        except Error:
            print('Ошибка при выводе содержимого таблицы')

    def delete(self):
        # нужно указать номер удаляемой записи
        try:
            self.work_with_db.delete(user_input=self.work_with_db.delete_input())
        except Error:
            print('Ошибка при удаление запись')


work_with_db = DataBaseWorker()

if __name__ == '__main__':
    work_with_db
