import configuration
import requests
import data

#создание заказа
post_creat_order = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.create_order_body,
                         headers=data.headers)

order_body = post_creat_order.json() #объект, содержащий номер отслеживания
current_track_number = order_body["track"] #выделяем номер отслеживания в переменную
current_track_number_str = str(current_track_number) #преобразуем номер в тип str для добавления параметра в URL

#получение заказа по номеру отслеживания
get_order_by_number = requests.get(configuration.URL_SERVICE + configuration.RECEIVE_ORDER_BY_NUMBER_PATH + \
                                       "?t=" + current_track_number_str)