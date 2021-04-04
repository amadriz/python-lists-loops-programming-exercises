list_of_numbers = [4,	80,	85,	59,	37,25,	5,	64,	66,	81,20,	64,	41,	22,	76,76,	55,	96,	2,	68]


#Your code here:
def merge_two_list (list_of_numbers):
    new_list = []
    even = []
    odd = []
    for i in list_of_numbers:
        if i % 2 != 0:
            even.append(i)
        else:
            odd.append(i)
    new_list.append(even)
    new_list.append(odd)
    return new_list

print(merge_two_list(list_of_numbers))

