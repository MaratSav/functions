calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):


def is_contains(string, list_to_search):


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)