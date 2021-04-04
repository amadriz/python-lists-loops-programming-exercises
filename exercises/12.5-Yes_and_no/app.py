theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:
def wiki (items):
    if items == 1:
        return "wiki"
    else:
        return "woko"

new_list = list(map(wiki, theBools))
print(new_list)

