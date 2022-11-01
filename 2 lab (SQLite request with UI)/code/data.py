import sqlite3
from contextlib import closing




DB = 'long_distance_calls_payment.db'
DB = 'calls.db'

class DataBase():
    def __init__(self, db):
        self.conn = sqlite3.connect(db)

    def __enter__(self):
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()


class Technologist:
    @staticmethod
    def show_client():
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute("""SELECT * FROM user ORDER BY IDномер """)
            return cur.fetchall()

    @staticmethod
    def add_client(*args):
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute("""INSERT INTO user VALUES (?,?,?,?)""", tuple(args))
        print('Клиент успешно добавлен!')

    @staticmethod
    def del_client(category,key):
        categories = ['IDномер', 'ФИО', 'Адрес', 'Дата_регистрации']
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute(f"DELETE FROM user WHERE {categories[category]} = '{key}'")
        print('Клиент успешно удалён!')

    @staticmethod
    def show_tarif():
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute("""SELECT * FROM tarif ORDER BY IDтариф """)
            return cur.fetchall()
    @staticmethod
    def add_tarif(*args):
        with DataBase(DB) as connection:
            args = list(args)
            cur = connection.cursor()
            cur.execute("""SELECT IDтариф FROM tarif ORDER BY IDтариф DESC""")
            args.insert(0, int(cur.fetchone()[0]) + 1)
            cur.execute(f"""INSERT INTO tarif VALUES (?,?,?,?,?)""", tuple(args))
        print('Тариф успешно добавлен!')

    @staticmethod
    def del_tarif(category,key):
        categories = ['IDтариф', 'Дата', 'Населённый', 'Полная_стоимость', 'Льготная_стоимость']
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute(f"DELETE FROM tarif WHERE {categories[category]} = '{key}'")
        print('Тариф успешно удалён!')

    @staticmethod
    def update_price(key,full_price,part_price):
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute(
                f"""UPDATE tarif SET Полная_стоимость = {full_price}, Льготная_стоимость = {part_price}  WHERE IDтариф = '{key}'""")
        print('Данные обновлены!')

    @staticmethod
    def search_by_company(key):
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute(
                f"""SELECT tarif.Дата, tarif.Населённый, tarif.Полная_стоимость, tarif.Льготная_стоимость FROM company INNER JOIN tarif ON company.IDтариф = tarif.IDтариф WHERE company.Название = '{key}'""")
            return cur.fetchall()
        print('Данные полученны!')
    @staticmethod
    def search_price_by_date(date):
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute(
                f"""SELECT Полная_стоимость, Льготная_стоимость FROM tarif WHERE Дата = '{date}'""")
            return cur.fetchall()
        print('Данные полученны!')


class Operator:
    @staticmethod
    def show_call():
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute("""SELECT * FROM call ORDER BY IDзвонка """)
            return cur.fetchall()

    @staticmethod
    def add_call(*args):
        with DataBase(DB) as connection:
            args = list(args)
            cur = connection.cursor()
            cur.execute("""SELECT IDзвонка FROM call ORDER BY IDзвонка DESC""")
            args.insert(0, int(cur.fetchone()[0]) + 1)
            cur.execute(f"""INSERT INTO call VALUES (?,?,?,?,?,?)""", tuple(args))
        print('Звонок успешно добавлен!')

    @staticmethod
    def del_call(category, key):
        categories = ['IDзвонка', 'Дата', 'Населённый', 'IDномер', 'Льготная_стоимость','Оплата']
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute(f"DELETE FROM call WHERE {categories[category]} = '{key}'")
        print('Звонок успешно удалён!')

    @staticmethod
    def debtors():
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute(f"""SELECT Дата, call.IDномер, ФИО, Адрес, Название  FROM call 
            INNER JOIN user USING (IDномер)
            INNER JOIN company USING (IDномер)
            WHERE JULIANDAY('2022-10-23') - JULIANDAY(Дата) >= 20 AND Оплата = 0""")
            return cur.fetchall()
        print('Должники успешно найдены!')

    @staticmethod
    def number_of_client_month_city(month,city):
        request_list = ('Месяц', 'Населённый_пункт')
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute(f"""SELECT Дата,  Count(IDномер) FROM call WHERE Дата LIKE '%-{month}-%' AND Населённый = '{city}' GROUP BY Дата""")
            return cur.fetchall()
        print('Клиенты успешно найдены!')




if __name__ == '__main__':
    i= Operator()
    print(i.debtors())




# cur.execute("""CREATE TABLE IF NOT EXISTS user(
#    IDclient INTEGER PRIMARY KEY,
#    phone_number TEXT NOT NULL,
#    full_name TEXT NOT NULL,
#    address TEXT,
#    data_of_registration TEXTб
#    );
# """)




