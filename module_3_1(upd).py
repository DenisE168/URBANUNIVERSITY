calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(strings):
    stroka = str(strings)
    results = (len(stroka),stroka.upper(),stroka.lower())
    count_calls()
    return results
def is_contains(string, list_to_search):
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    result = False
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            result = True
            break
    return result
print(string_info('Piroshok'))
print(string_info('Forest'))
print(string_info('Quadrobober'))
print(is_contains('Bike',['motor','snow','auto']))
print(is_contains('BiKE',['bike','snow','motor','auto']))