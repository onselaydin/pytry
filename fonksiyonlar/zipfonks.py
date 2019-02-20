list1 = [1,2,3,4,5]
list2 = [3,6,9,12,15]
a = list(zip(list1,list2)) #iki listenin elemanlarını gruplamak için kullanılır.
print(a)


list3 = [1,2,3,4]
list4 = ["python","c#","java","javascript"]
for i,j in zip(list3,list4):
    print(i,j)

