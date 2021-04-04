chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
    new_chunk_combine = []
    for i in chunk_one:
        new_chunk_combine.append(i)
    for x in chunk_two:
        new_chunk_combine.append(x)
    return(new_chunk_combine)
print(merge_list(chunk_one, chunk_two))
