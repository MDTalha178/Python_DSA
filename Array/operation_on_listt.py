# Decalare a list 
li = [1,2,3,4 ,'Talha']

# append method
""""
append we use used to insert a element in the list .but by default it will be
insert at the end of the list
"""
li.append(80)
print(li , "append operation perform")

# insert method
"""
insert we use to insert a element in the list .but when we want insert at the particular 
index
"""
li.insert(2,91)
print(li ,  "insert operation perform")

# extend method
"""extend method we use when we want want insert a multiple element
   at one time
"""
ex_li = [0,9,'from_extend']
li.extend(ex_li)
print(li, 'extend operation perform')

# remove method
"""remove method we use when we want to remove
   a elemnet from a list
"""
li.remove(9)
print(li, "remove operation perform")

# pop method
"""pop method we use when we want to delete an elemnet from a list through a method
   an index
"""
li.pop(2)
print(li, "pop operation perform")

# looping on list
"""looping on list using range function
   by defult for loop start with 0
"""
for i in range(len(li)):
    print(li[i])
print("by using range function")

# another method looping on list
"""looping on a list directly through list 
"""
for i in li:
    print(i)
print("by using direct list")

# another method looping on list
"""we cal also print by using slicing list
"""
for i in li[:len(li)]:
    print(i)
print("by using slicing list")