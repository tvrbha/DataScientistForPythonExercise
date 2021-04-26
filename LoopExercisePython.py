'''
1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
'''

def divisibleby7_multipleby5(range_from:int=1500, range_to:int=2700):
    my_assigned_list = list()
    index_value_list = 0
    for current_value in range(range_from, range_to+1):
        if(current_value % 7 == 0 and current_value % 5 == 0):
            my_assigned_list.append(current_value)
            # print("Inside Function")
    for value_in_list in my_assigned_list:
        index_value_list = index_value_list+1
        if index_value_list < len(my_assigned_list):
            print(value_in_list, end=',')
        else:
            print(value_in_list)

print("Exercise 1:")
divisibleby7_multipleby5()

'''2. Write a Python program to construct the following pattern, using a nested for loop.'''

def pretty_pattern(count:int=5,pattern:str="*"):
    for current_count in range(count):
        # print(pattern*current_count)
        text = ""
        for inner_count in range(current_count):
            text = text + pattern
        print(text)
    for current_count in range(count,0,-1):
        # print(pattern*current_count)
        text = ""
        for inner_count in range(current_count):
            text = text + pattern
        print(text)
    # for current_count in range(count, 0,-1):
        # print(pattern * current_count)

print("Exercise 2: Output")
pretty_pattern()


'''3. Write a Python program to count the number of even and odd numbers from a series of numbers.'''

def odd_even_series(my_odd_even_find_list:list=[101,102,103,104,105]):
    odd_count=0
    even_count=0
    for current_value in my_odd_even_find_list:
        if current_value%2==0:
            even_count=even_count+1
        else:
            odd_count=odd_count+1
    print("Odd Count : ",odd_count," Even Count : ",even_count)

print("Exercise 3: Output")
odd_even_series()

'''4. Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. 
The numbers obtained should be printed in a comma-separated sequence.'''

def even_in_digit(range_start:int=100,range_end:int=400):
    my_find_list=list()
    for current_value in range(range_start,range_end+1):
        for curr_val_str in str(current_value):
            if(int(curr_val_str)%2!=0):
                break
        else:
            my_find_list.append(current_value)
    print(my_find_list)


print("Exercise 4: Output")
even_in_digit()


def calculate_dog_years(human_years):
    dog_years=0
    if human_years <=2 and human_years !=0:
      for years in range(1,human_years+1):
        dog_years=dog_years+10.5
    elif human_years>2:
         dog_years=21
         for years in range(3,human_years+1):
             dog_years=dog_years+4
    print(f"The dog's age in dog's years is {dog_years}")

print("Exercise 5: Output")
human_years=int(input("Input a dog's age in human years: "))
calculate_dog_years(human_years)

print("Exercise 6: Output to test")
def find_max_number(number_list:list):
    max_number=number_list[0]
    for value_check in number_list:
        if value_check>max_number:
            max_number=value_check
    else:
        print('max_number :',max_number)

my_num_list=[-7,-4,-6]
find_max_number(my_num_list)


"""## 7. Write a Python function that takes a number as a parameter and check the number is prime or not."""
def chk_prime_or_not(prime_number_chk):
    prime_number=True
    if prime_number_chk>=2 and prime_number_chk<=3:
        prime_number = True
    elif prime_number_chk==1:
        prime_number = False
    elif prime_number_chk > 3:
        for chk_value in range(2,prime_number_chk):
            if prime_number_chk%chk_value==0:
                prime_number=False
                break
    return prime_number



prime_number_chk=int(input('Enter the Number to Check Prime or No : '))
if chk_prime_or_not(prime_number_chk):
    print(f'{prime_number_chk} : IS A PRIME')
else:
    print(f'{prime_number_chk} : IS NOT PRIME')

"""# 8 Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. Go to the editor"""
#97 to 122 lower cases 65 to 91 uppercase
def uppercase_lowercase_count(string_to_calculate):

    dict_count=dict()
    for char in string_to_calculate:
        if ord(char)>=97 and ord(char)<=122:
            dict_count.update({'LOWER_CASE_COUNT':dict_count.get('LOWER_CASE_COUNT',0)+1})
        elif ord(char)>=65 and ord(char)<=91:
            dict_count.update({'UPPER_CASE_COUNT':dict_count.get('LOWER_CASE_COUNT',0)+1})
            #dict_count.update('UPPER CASE COUNT', uppercase_count)
    print (dict_count)
    #print(f'{string_to_calculate} uppercase letters count : ',uppercase_count,'lower case count : ',lowercase_count)

string_to_calculate=input('Enter The String : ')
uppercase_lowercase_count(string_to_calculate)

"""## 9. Write a Python program to reverse a string. and palindrome"""
def reverse_given_string(string_to_be_revered):
    #for char in reversed(string_to_be_revereda):
    reverse_string=""
    for char in range(len(string_to_be_revered)-1,-1,-1):
        reverse_string=reverse_string+string_to_be_revered[char]
    print (reverse_string)
    if reverse_string==string_to_be_revered:
        print('Palindrome : ',string_to_be_revered,'Reversed String: ',reverse_string)
    else:
        print('Not Palindrome : ', string_to_be_revered, 'Reversed String: ', reverse_string)


string_to_be_reversed=input('Enter The String :  ')
reverse_given_string(string_to_be_reversed)

""" 10. Write a Python program to find  the greatest common divisor (gcd) of two integers."""

def find_greatest_common_divisor(first_number:int=30,second_number:int=36):
    max_number=0
    div_number=2
    while div_number<=first_number and div_number<=second_number:
        if first_number%div_number==0 and second_number%div_number==0:
            if div_number > max_number:
                max_number=div_number
        div_number=div_number+1
    print('gcd : ',max_number)

find_greatest_common_divisor()