#-----------Question 1


def hello_username(username):
    """Print's a greeting to a specific user"""
    print(f'"hello_{username.upper()}"')

hello_username('username')

#-----------Question 2

def first_odds():
    """When called prints a list of every odd number 1-100"""
    for num in range(1,101):
        if num % 2 != 0:
            print(num)

first_odds()

#-----------Question 3

def max_num_in_list(a_list):
    """Finds the highest number in a given list and returns that number"""
    max_num = max(a_list)
    return max_num

#Test
my_list = [1,3,4,14,85,25,35,42]
print(max_num_in_list(my_list))

#-----------Question 4

def is_leap_year(a_year):
    if a_year % 100 != 0 or a_year % 400 == 0:
        if a_year % 4 == 0:
            return True
        else:
            return False
    else:
        return False

#Test
print(is_leap_year(2000))

#-----------Question 5

def is_consectutive(a_list):
    check = 0
    for index in range(len(a_list)):
        if index != max(range(len(a_list))):
            if a_list[index]+1 != a_list[index+1]:
                check += 1
    if check >= 1:
        return False
    else:
        return True


test_list = [1,2,3,4,5,6,7,8]
print(is_consectutive(test_list))
        
        

