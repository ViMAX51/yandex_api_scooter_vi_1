import configuration
import data
import requests
import sender_stand_request


# Виталий Максимов, 15-я когорта — Финальный проект. Инженер по тестированию плюс

# ф-я получения трек номер из созданного заказа
def getting_the_track_number_of_the_order_from_the_order():
    track = sender_stand_request.creating_a_new_order(data.body).json()
    t = track['track']
    return t


# ф-я для проверки, что по треку заказа можно получить данные о заказе
def positive_assert():
    t = getting_the_track_number_of_the_order_from_the_order()
    order_response = sender_stand_request.receiving_an_order_by_the_order_track(t)
    assert order_response.status_code == 200


# ф-я запуска автотеста проверки, что по треку заказа можно получить данные о заказе
def test_the_response_code_200_sending_request_order_information_by_order_number():
    positive_assert()
