#Question 1
#prints "hello_USERNAME!""
def hello_name(user_name):
    print(f"hello_{user_name}!")

hello_name("USERNAME")

#Question 2
#function that prints odd numbers from 1-100
#and returns nothing
def first_odds(num):
    while num <= 100:
        num += 1
        if num % 2 == 1:
            print(num)
        elif num == 100:
            break
        else:
            continue
num=0
first_odds(num)

#Question 3
#function that returns max number from a list
def max_num_in_list(a_list):
    a_list.sort()
    max= a_list[-1]
    return(max)
    
a_list = [1, 4, 2, 70, 95, 3]
print(max_num_in_list(a_list))

#Quetion 4
#function that returns if a year is a leap year
#leap year = divisible by 4 but not by 100 unless by 400
def is_leap_year(a_year):
    if a_year % 4 == 0 & a_year % 100 != 0:
        return(True)
    elif a_year % 4 == 0 & a_year % 400 == 0:
        return(True)
    else:
        return(False)
a_year = 2004
print(is_leap_year(a_year))

#Question 5
#function that checks whether a list is consecutive or not
def is_consecutive(a_list):
    sorted_list = sorted(a_list)
    if a_list == sorted_list:
        return(True)
    else:
        return(False)
a_list= [3,6,5,4,2]
print(is_consecutive(a_list))
