coll = set()
coll.add(1)
coll.add(2)
coll.add(2)
print(coll)
coll.remove(1)
print(coll)
set.clear(coll)#clears the entire set
print(coll)
print("----End of add and remove set function-----")

'''Union set function'''
print("------starting of Union set function------")
set1 = {1,2,3}
set2 = {2,3,4}
print(set1)
print(set2)
print(set1.union(set2))
print("------End of Union set function------")

'''intersection set function'''
print("------Start of intersection set function------")
print(set1.intersection(set2))