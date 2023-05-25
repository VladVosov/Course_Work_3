import functions

operations = functions.open_operations("operations.json")  # Достаем список операций из json

complated_opetations = functions.examination(operations)  # Убираем из списка операций несостоявшиеся операции

sorted_by_date = functions.sorted_operations(complated_opetations)  # Сортируем список операций по дате (по убыванию)

last_five_operations = functions.last_five_operations(sorted_by_date)  # Отсеиваем пять последних успешных операций

# Выводим на экран пять последник транзакций
for operations in last_five_operations:
    print(functions.date_and_purpose(operations))
    print(functions.transaction(operations))
    print(functions.amount(operations))
    print('\n')
