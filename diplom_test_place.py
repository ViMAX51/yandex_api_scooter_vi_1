import configuration
import data
import requests
import json

# Виталий Максимов, 15-я когорта — Финальный проект. Инженер по тестированию плюс
def create_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=data.body)


def take_t_new_order():
    track = create_new_order(data.body).json()
    t = track['track']
    return t


def take_order_on_number(t):
    return requests.get(configuration.URL_SERVICE + configuration.TAKE_ORDERS + '?t=' + str(t))


def positive_assert():
    t = take_t_new_order()
    order_response = take_order_on_number(t)
    assert order_response.status_code == 200


def test_code_200():
    positive_assert()
