def max_min(num_list):
    '''
    Finds the maximum and minimum in a list of numbers.
    INPUT: A string of space separated numbers. 
    OUTPUT: A list containing the minimum and maximum from the list provided. 
    '''
    # Set local variables
    min_num = num_list[0]  # Treat first number as minimum
    max_num = num_list[0]  # Treat first number as maximum
    result = []
    # Iterate through list
    for num in num_list:
        if num < min_num:  # Update when new minimum is found
            min_num = num
        if num > max_num:  # Update when new maximum is found
            max_num = num

    result.append(min_num)  # Update list with min
    result.append(max_num)  # Update list with max
    print(result)


user_input = input("Enter numbers separated by spaces")  # Request numbers
input_list = [int(n) for n in user_input.split()]  # creates list

max_min(input_list)
