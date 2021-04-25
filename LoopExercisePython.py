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