# BROAD REASONS WHY YOU MIGHT GET AN EXCEPTION
# (1) Trying to refer to something that doesn't exist
# (2) Using a value that is inappropriate in some way

# CORE EXAMPLES OF EXCEPTIONS IN THIS FILE
# AttributeError (1)
# KeyError (1)
# IndexError (1)
# NameError (1)
# UnboundLocalError (1)
# TypeError (2)
# ValueError (2)
# ZeroDivisionError (2)
# OverflowError (2)
# FileNotFoundError (1)
# UnicodeEncodeError (2)
# ModuleNotFoundError (1)
# ImportError (1)

# BONUS EXAMPLES YOU CAN TRY IF YOU WISH
# PermissionError (2)
# IsADirectoryError (2)


# AttributeError - EXAMPLE
import math
import os

def produce_attribute_error():
    # print(1.234.upper())
    pass

# KeyError
def produce_key_error():
    ages = {'Jim': 30, 'Pam': 28, 'Kevin': 33}
    ages['Michael']

# IndexError
def produce_index_error():
    letters = ["A", "B"]
    print(letters[2])

# NameError
def produce_name_error():
    print(raspberry['cherry'])

# UnboundLocalError
def produce_unbound_local_error():
    lst += [5]

# TypeError
def produce_type_error():
    4 + '3'

# ValueError
def produce_value_error():
    import math
    print(math.sqrt(-1))

# ZeroDivisionError
def produce_zero_division_error():
    a = 8
    b = 0
    c = a / b
    print(c)

# OverflowError
def produce_overflow_error():
    import math
    print("A ridiculous number is ")
    print(math.exp(1000))

# FileNotFoundError
def produce_file_not_found_error():
    with open('song.txt', 'r') as file:
        text = file.read()

# UnicodeEncodeError
def produce_unicode_encode_error():
    a = 'ê'
    print("ASCII Representation of ê: ", a.encode('ascii'))

# ModuleNotFoundError
def produce_module_not_found_error():
    import me
    print (me.find())

# ImportError
def produce_import_error():
    from something import nothing

# PermissionError
def produce_permission_error():
        file = open("/Users/eloisephelps/Dev/git-exception-testing-challenge/naughty.txt", "w+")
        content = file.read()
        print(content)
        file.close()
        pass

#     leslie's -  C:\Users\Leslie\PycharmProjects\cfg-python

def produce_is_a_directory_error():
    open("/Users/eloisephelps/Dev/git-exception-testing-challenge/.pytest_cache", "w")
