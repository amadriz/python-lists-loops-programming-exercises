par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}
#your code go here:

def count_char(letra):
    letra = letra.lower()
    for i in letra:
        keys = counts.keys()
        if i != " ":
            if i in keys:
                counts[i] += 1
            else:
                counts[i] = 1
    return counts

print(count_char(par))

