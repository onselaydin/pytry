def double(x):
    return x * 2
#map(double,[1,2,3,4,5,6]) #double fonksiyonunu arraydeki her eleman için çalıştırır.
a = list(map(double,[1,2,3,4,5,6])) 
print(a)

b = list(map(lambda x : x ** 2,[1,2,3,4,5,6]))
print(b)

liste1 = [1,2,3,4,5]
liste2 = [2,4,6,8,10]
c = list(map(lambda x, y : x * y, liste1, liste2)) #liste1 deki elemanları sırayla liste2 deki elemanlarla çarptık.
print(c)

