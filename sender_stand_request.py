import configuration
import data
import requests


# ф-я создания нового заказа

def creating_a_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=data.body)


# ф-я получения заказа по его треку заказа
def receiving_an_order_by_the_order_track(t):
    return requests.get(configuration.URL_SERVICE + configuration.TAKE_ORDERS + '?t=' + str(t))
