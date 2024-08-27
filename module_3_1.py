calls = 0


def count_calls ():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    a = (len(string), string.upper(), string.lower())
    print(a)


def  is_contains (string, list_to_search):
    count_calls()
    list_to_search_upper = [i.upper() for i in list_to_search]
    if string.upper() in list_to_search_upper:
        return True
    else:
        return False


string_info('Capybara')
string_info('Armageddon')
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
