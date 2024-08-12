# Write a python function to remove a given word from a list and strip it at same time

# def rem(l ,word):
#    n = []
#    for item in l:
#       if not(item == word):
#        n.append(item.strip(word))
#       return n
# l = ["Harry", "Arijit", "Rohan", "Subham"]

# print(rem(l, "an"))



def remove(l, word):
    n = []
    for item in l:
            if not(item == word):
               n.append(item.strip(word))        
    return n
    

list = ["Arijit", "Soumik", "Rick"]

print(remove(list, "k"))