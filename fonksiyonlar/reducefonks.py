from functools import reduce

def topla(x, y):
    return x + y

a = reduce(topla,[12, 18, 20, 10]) #önce 12 18 toplanır, çıkan sonuç 20 ile ve en son 10 ile toplanır. üst üste eklemeli.
print(a)

def maksimum(x, y):
    if(x > y):
        return x
    else:
        return y
print(maksimum(5,10))
b = reduce(maksimum,[-2,3,1,4])
print(b)