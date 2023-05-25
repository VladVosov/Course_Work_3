import json


def open_operations(file_json):
    """Достает список операций из .json"""
    with open(file_json, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def examination(operations):
    """Удаляет несостоявшиеся операции из списка"""
    first = operations
    complated_opetations = []
    for i in first:
        if i == {}:
            continue
        else:
            complated_opetations.append(i)
    return complated_opetations


def sorted_operations(operations):
    """Сортирует операции по дате (от последней к первой)"""
    operations_sorted = sorted(operations, key=lambda sort_oper: sort_oper['date'], reverse=True)
    return operations_sorted


def last_five_operations(operations):
    """Сортирует 5 успешных операций"""
    five_operations = []
    for f in operations:
        if f['state'] == "EXECUTED":
            five_operations.append(f)
        else:
            continue

        if len(five_operations) == 5:
            break
    return five_operations


def date_and_purpose(operation):
    """Возвращает из словаря дату и цель операции"""
    date_format = operation['date'].split('T')
    date_reformat = date_format[0].split('-')
    date_and_description = f"{date_reformat[2]}.{date_reformat[1]}.{date_reformat[0]} {operation['description']}"
    return date_and_description


def transaction(operation):
    """Выводит откуда и куда совершена транзакция"""
    key_card = 'from'
    key_card_pecipient = 'to'

    # Откуда совершена транзакция
    if key_card in operation:
        stage_1 = operation[key_card].split(' ')
        number_sender = stage_1[-1]
        if len(number_sender) > 16:
            last_number_check = number_sender[-4:]
            sender_check = f"{stage_1[0]} **{last_number_check}"
        else:
            if len(stage_1) > 2:
                sender_check = f"{stage_1[0]} {stage_1[1]} {number_sender[:4]} {number_sender[4:6]}** **** {number_sender[-4:]}"
            else:
                sender_check = f"{stage_1[0]} {number_sender[:4]} {number_sender[4:6]}** **** {number_sender[-4:]}"
    else:
        sender_check = 'Bank'

    # Куда совершена транзакция
    stage_2 = operation[key_card_pecipient].split(' ')
    number_pecipient = stage_2[-1]
    if len(number_pecipient) > 16:
        last_number_check = number_pecipient[-4:]
        pecipient_check = f"{stage_2[0]} **{last_number_check}"
    else:
        if len(stage_1) > 2:
            pecipient_check = f"{stage_2[0]} {stage_1[1]} {number_pecipient[:4]} {number_pecipient[4:6]}** **** {number_pecipient[-4:]}"
        else:
            pecipient_check = f"{stage_2[0]} {number_pecipient[:4]} {number_pecipient[4:6]}** **** {number_pecipient[-4:]}"

    return f"{sender_check} -> {pecipient_check}"


def amount(operation):
    """Выводит сумму перевода и валюту"""
    return f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}"








