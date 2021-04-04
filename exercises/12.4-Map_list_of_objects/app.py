  
import datetime


people = [
	{ "name": 'Joe', "birthDate": datetime.datetime(1987,10,24) }, 
	{ "name": 'Bob', "birthDate": datetime.datetime(1976,5,24) },   
	{ "name": 'Erika', "birthDate": datetime.datetime(1990,6,12) }, 
	{ "name": 'Dylan', "birthDate": datetime.datetime(2000,12,14) },    
	{ "name": 'Steve', "birthDate": datetime.datetime(2004,4,24) }  
]

def calculateAge(birthDate):
    today = datetime.date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

name_list = list(map(lambda person:  (person["name"],calculateAge(person["birthDate"])) , people))
new_list = []
for person in name_list:
    x = "Hello, my name is "+person[0]+" and I am "+str(person[1])+" years old"
    new_list.append(x)
print(new_list)