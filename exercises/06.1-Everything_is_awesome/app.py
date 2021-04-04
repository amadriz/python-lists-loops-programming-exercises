my_list = [ 1, 0, 0, 0, 1, 0, 0, 0, 1, 1 ]

def my_function(numbers):
    new_list = []
    for num in numbers:
    #The magic go here:
        if num == 1:
           new_list.append(1)
        elif num == 0:
           new_list.append("Yahoo")    
    return new_list
print(my_function(my_list))


