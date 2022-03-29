

def  is_whole_number(my_number):
    if my_number % 1 == 0 and my_number > 0:
        return True
    else:
        return False

def is_even_number(my_number):
    if my_number % 2 == 0:
        return True
    else:
        return False

my_numbers = [1,2,3,5,7,9]
def  is_natural_number(my_numbers):
    for my_number in my_numbers:
        return my_number

print(is_natural_number(my_number)):


my_number = 5

print(is_whole_number(my_number))
print(is_even_number(my_number))