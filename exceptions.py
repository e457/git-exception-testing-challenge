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
    pass


# ValueError
def produce_value_error():
    pass


# ZeroDivisionError
def produce_zero_division_error():
    pass


# OverflowError
def produce_overflow_error():
    pass


# FileNotFoundError
def produce_file_not_found_error():
    pass


# UnicodeEncodeError
def produce_unicode_encode_error():
    pass


# ModuleNotFoundError
def produce_module_not_found_error():
    pass


# ImportError
def produce_import_error():
    pass
