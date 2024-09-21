calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    string_info = (len(string), str.upper(string), str.lower(string))
    count_calls()
    return string_info

def is_contains(string, list_to_search):
        count_calls()
        string = str.upper(string)
        for i in range(len(list_to_search)):
            list_to_search[i] = list_to_search[i].upper()
        if string in list_to_search:
            return True
        else:
            return False


print(string_info("Capybara"))
print(string_info("Armageddon"))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)