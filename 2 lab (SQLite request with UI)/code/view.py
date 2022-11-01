from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import os.path

from data import Technologist, Operator

Builder.load_file("ui.kv")


class MenuScreen(Screen):
    pass

class OperatorScreen(Screen):
    pass

class TechnologistScreen(Screen):
    def update(self, navigation=0):
        information = Controller.update(Controller, navigation)
        self.ids['full_name_base_id'].text = information[0]
        self.ids['group_base_id'].text = information[1]
        self.ids['valid_reason_base_id'].text = information[2]
        self.ids['invalid_reason_base_id'].text = information[3]
        self.ids['totall_base_id'].text = information[4]

    def change_number_of_strings(self, number_of_strings):
        Controller.change_number_of_strings(Model, number_of_strings)


class ClientsScreen(Screen):
    #work
    def current_data(self):
        self.data = Technologist.show_client()
        self.phone_number, self.full_name, self.city, self.date = 'Номер телефона\n','ФИО\n','Адрес\n','Дата\n'
        for i in self.data:
            self.phone_number += f"{i[0]}\n"
            self.full_name += f"{i[1]}\n"
            self.city += f"{i[2]}\n"
            self.date += f"{i[3]}\n"
    #work
    def show_clients(self):
        self.current_data()
        self.ids['id_phonenumber_label'].text = self.phone_number
        self.ids['id_fullname_label'].text = self.full_name
        self.ids['id_city_label'].text = self.city
        self.ids['id_date_label'].text = self.date

#work
class AddClientScreen(Screen):
    def add(self,*args):
        Technologist.add_client(*args)
#work
class DelClientScreen(Screen):
    def delclient(self,category,key):
        Technologist.del_client(category,key)

class TarifScreen(Screen):
    def current_data(self):
        self.data = Technologist.show_tarif()
        self.id, self.date, self.city, self.full, self.part = 'IDтариф\n', 'Дата\n', 'Населённый пункт\n', 'Полная стоимость\n', 'Льготная стоимость\n'
        for i in self.data:
            self.id += f"{i[0]}\n"
            self.date += f"{i[1]}\n"
            self.city += f"{i[2]}\n"
            self.full += f"{i[3]}\n"
            self.part += f"{i[4]}\n"
    #work
    def show_tarif(self):
        self.current_data()
        self.ids['id_id_label'].text = self.id
        self.ids['id_date_label'].text = self.date
        self.ids['id_city_label'].text = self.city
        self.ids['id_full_label'].text = self.full
        self.ids['id_part_label'].text = self.part
class AddTarifScreen(Screen):
    def add(self,*args):
        Technologist.add_tarif(*args)
class DelTarifScreen(Screen):
    def deltarif(self,category,key):
        Technologist.del_tarif(category,key)
class UpdateTarifScreen(Screen):
    def update(self,key,full_price,part_price):
        Technologist.update_price(key,full_price,part_price)
class SearchByCompanyScreen(Screen):
    def current_data(self,key):
        self.data = Technologist.search_by_company(key)
        self.date, self.city, self.full, self.part = 'Дата\n', 'Населённый пункт\n', 'Полная стоимость\n', 'Льготная стоимость\n'
        for i in self.data:
            self.date += f"{i[0]}\n"
            self.city += f"{i[1]}\n"
            self.full += f"{i[2]}\n"
            self.part += f"{i[3]}\n"
    def show(self,key):
        self.current_data(key)
        self.ids['id_date_label'].text = self.date
        self.ids['id_city_label'].text = self.city
        self.ids['id_full_label'].text = self.full
        self.ids['id_part_label'].text = self.part

class SearchPriceByDateScreen(Screen):
    def current_data(self,key):
        self.data = Technologist.search_price_by_date(key)
        self.full, self.part =  'Полная стоимость\n', 'Льготная стоимость\n'
        for i in self.data:
            self.full += f"{i[0]}\n"
            self.part += f"{i[1]}\n"
    def show(self,key):
        self.current_data(key)
        self.ids['id_full_label'].text = self.full
        self.ids['id_part_label'].text = self.part


class CallScreen(Screen):
    def current_data(self):
        self.data = Operator.show_call()
        self.id,self.date, self.city, self.phone_number, self.time, self.pay = 'IDзвонка\n','Дата\n', 'Город\n', 'Номер\n', 'Длительность\n', 'Оплата\n'
        for i in self.data:
            self.id += f"{i[0]}\n"
            self.date += f"{i[1]}\n"
            self.city += f"{i[2]}\n"
            self.phone_number += f"{i[3]}\n"
            self.time += f"{i[4]}\n"
            self.pay += f"{i[5]}\n"
    def show_clients(self):
        self.current_data()
        self.ids['id_id_label'].text = self.id
        self.ids['id_date_label'].text = self.date
        self.ids['id_city_label'].text = self.city
        self.ids['id_phone_number_label'].text = self.phone_number
        self.ids['id_time_label'].text = self.time
        self.ids['id_pay_label'].text = self.pay

class AddCallScreen(Screen):
    def add(self,*args):
        Operator.add_call(*args)
class DelCallScreen(Screen):
    def delcall(self,category,key):
        Operator.del_call(category,key)
class DebstorScreen(Screen):
    def current_data(self):
        self.data = Operator.debtors()
        self.date, self.phone_number, self.full_name, self.city, self.name = 'Дата\n','Номер\n', 'ФИО\n', 'Город\n', 'Название компании\n'
        for i in self.data:
            self.date += f"{i[0]}\n"
            self.phone_number += f"{i[1]}\n"
            self.full_name += f"{i[2]}\n"
            self.city += f"{i[3]}\n"
            self.name += f"{i[4]}\n"

    def show(self):
        self.current_data()
        self.ids['id_date_label'].text = self.date
        self.ids['id_phone_number_label'].text = self.phone_number
        self.ids['id_full_name_label'].text = self.full_name
        self.ids['id_city_label'].text = self.city
        self.ids['id_name_label'].text = self.name

class NumberByMonthAndCityScreen(Screen):
    def current_data(self,month,city):
        self.data = Operator.number_of_client_month_city(month,city)
        self.date, self.client =  'Дата\n', 'Количество клиентов связавшихся с городом\n'
        for i in self.data:
            self.date += f"{i[0]}\n"
            self.client += f"{i[1]}\n"
    def show(self,month,city):
        self.current_data(month,city)
        self.ids['id_date_label'].text = self.date
        self.ids['id_client_label'].text = self.client



class TestApp(App):
    Window.clearcolor = (.98,.89,.85,1)

    def build(self):
        self.title = "Long_distance_calls_payment"
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(TechnologistScreen(name='technologist'))
        sm.add_widget(ClientsScreen(name='clients'))
        sm.add_widget(AddClientScreen(name='addclient'))
        sm.add_widget(DelClientScreen(name='delclient'))
        sm.add_widget(TarifScreen(name='tarif'))
        sm.add_widget(AddTarifScreen(name = 'addtarif'))
        sm.add_widget(DelTarifScreen(name= 'deltarif'))
        sm.add_widget(UpdateTarifScreen(name = 'updatetarif'))
        sm.add_widget(SearchByCompanyScreen(name = 'searchbycompany'))
        sm.add_widget(SearchPriceByDateScreen(name = 'searchpricebydate'))
        sm.add_widget(OperatorScreen(name='operator'))
        sm.add_widget(CallScreen(name ='call'))
        sm.add_widget(AddCallScreen(name = 'addcall'))
        sm.add_widget(DelCallScreen(name= 'delcall'))
        sm.add_widget(DebstorScreen(name = 'debstor'))
        sm.add_widget(NumberByMonthAndCityScreen(name = 'numberbymonthandcity'))

        return sm


if __name__ == '__main__':
    TestApp().run()
'''
Вывести для просмотра стоимость оплаты одной минуты разговора для разных населенных пунктов на заданную дату:
название организации, предоставляющей услуги связи - дата, название населенного пункта, стоимость одной минуты, льготная стоимость одной минуты.
Информация о компании
Поиск стоимости по дате
'''
