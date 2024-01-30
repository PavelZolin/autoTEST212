import sender_stand_request
import data


# Функция для изменения значения в параметре name  kit_body в теле запроса
def get_kits_body(name):
    # Копируется словарь с телом запроса из файла data
    current_body = data.kits_body.copy()
    # Изменение значения в поле name
    current_body["name"] = name
    # Возвращается новый словарь с нужным значением Name
    return current_body


def positive_assert(name):
    #В переменную body_kits сохраняется обновлённое тело запроса
    kits_body = get_kits_body(name)
    # В переменную kits_response сохраняется результат запроса на создание пользователя:
    kits_response = sender_stand_request.post_new_client_kits(kits_body)
    # Проверяется, что код ответа равен 201
    assert kits_response.status_code == 201

#Допустимое количество символов (1) Код ответа — 201:
def test_create_body_kits_1_letter_in_name_get_success_response():
    positive_assert("a")

# Допустимое количество символов (511) Код ответа — 201:
def test_create_body_kits_511_letter_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

#Разрешены английские буквы Код ответа — 201:
def test_create_body_kits_english_letter_in_name_get_success_response():
    positive_assert("QWErty")

#Разрешены русские буквы Код ответа — 201:
def test_create_body_kits_russian_letter_in_name_get_success_response():
    positive_assert("Мария")

#Разрешены спецсимволы Код ответа — 201:
def test_create_body_kits_has_space_in_name_get_success_response():
    positive_assert("№%@,")

#Разрешены пробелы Код ответа — 201:
def test_create_body_kits_has_space_in_name_get_success_response():
    positive_assert(" Человек и КО ")

#Разрешены цифры Код ответа — 201:
def test_create_body_kits_3_letter_in_name_get_success_response():
    positive_assert("123")



def negative_assert(name):
    #В переменную body_kits сохраняется обновлённое тело запроса
    kits_body = get_kits_body(name)
    # В переменную kits_response сохраняется результат запроса на создание пользователя:
    kits_response = sender_stand_request.post_new_client_kits(kits_body)
    # Проверяется, что код ответа равен 400
    assert kits_response.status_code == 400

#Параметр не передан в запросе Код ответа — 400:
def test_create_body_kits_null_letter_in_name_get_error_response():
    # Копируется словарь с телом запроса из файла data в переменную user_body
    # Иначе можно потерять данные из исходного словаря
    kits_body = data.kits_body.copy()
    # Удаление параметра name из запроса
    kits_body.pop("name")
    kits_response = sender_stand_request.post_new_client_kits(kits_body)
    # Проверяется, что код ответа равен 400
    assert kits_response.status_code == 400

#Передан другой тип параметра (число) Код ответа — 400:
def test_create_body_kits_has_number_in_name_get_error_response():
    negative_assert (123)

#Количество символов меньше допустимого (0) Код ответа — 400:
def test_create_body_kits_0_letter_in_name_get_error_response():
    negative_assert("")

# Количество символов больше допустимого (512) Код ответа — 400:
def test_create_body_kits_512_letter_in_name_get_error_response():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


