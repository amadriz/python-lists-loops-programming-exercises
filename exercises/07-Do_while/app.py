
#Your code go here:
i = 20

while i >= 0:
    if i % 5 == 0:
        # el sep es para borrar espacios
        print(i,"!", sep="")
    else:
        print(i)
    i -= 1
print("LIFTOFF")