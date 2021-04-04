people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    #Your code go here:
    delete_new_list = []
    for i in people:
        if i != person_name:
           delete_new_list.append(i)
    return(delete_new_list)

print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))