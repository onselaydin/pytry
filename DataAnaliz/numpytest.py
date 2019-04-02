import numpy as np
arr2 = np.array([[10,11,12],[13,14,15],[16,17,18]])
#arr3 = np.array([1,2,3,4,5])
arr = np.arange(1,10) # 1 ile 10 
arr4 = np.arange(1,21)
#print(arr3)
#print(arr3[0])
"""
#https://docs.scipy.org/doc/numpy/
print(arr2[2,2]) # bu matrisde 0,1,2 gibi gidiyor.3 satır 3 sütunu aldık.
print(np.arange(10,20)) # 10 ile 20 arasındakileri sayıları listeler.
print(np.arange(0,100,3)) # 0 ile 100 arasını 3 er 3 er listeler
print(np.zeros(10)) # 10 0 basar.
print(np.ones(10)) # 10 tane biri basar 
print(np.zeros((2,2))) # 2 ye 2 matrisli 0 lar basar
print(np.linspace(0,100,5)) # 0 ile 100 5 eşit parçaya böler
print(np.eye(6)) # 6 ya 6 matris oluşturur. diyagonalleri(köşegenlerde) 1 yapar.
print(np.random.randint(0,10))
print(np.random.randint(1,10,5)) #random 5 elemanlı bir array oluşturur.
print(np.random.randn(5)) # Gauss Distribution
"""
"""
print(arr2.max())
print(arr2.min())
print(arr2.sum())
print(arr2.mean()) # ortalama alır.
print(arr2.argmax()) # en büyük sayının indisini verir.
"""

"""
print(arr[1])
print(arr[1:5])  # arraydaki 1 ile 5 arasındakileri verir.
print(arr[:4]) # arraydaki 0 ile 4. arasındakileri verir.
"""

"""
arr4 = arr4.reshape(5,4) # arr4 isimli arrayimizi 5'e 4 matrixe çevirdi.
print(arr4)
print(arr4[:,:2]) # ilk 2 sütunun çıktısını verir.virgulden öncekiler satır(hepsi al diyoruz) virgülün sağındakiler sütun
print(arr4[:3,:3]) #ilk üç satır ve üç sutun
"""
#array filtreler
print(arr[arr > 3]) # 3 den büyükleri listeler.

print(arr - 2) # arrayin her elemanından 2 çıkartır.

#iki aynı boyutlu arraylerde örneğin arr1 * arr2 her elaman birbiri ile çarpılabilir.

print(np.sqrt(arr)) # her bir elemanın karesini alır.

# https://nbviewer.jupyter.org/github/mustafamuratcoskun/Data-Analiz-Notebooklar/blob/master/Numpy%20%C3%96dev/Numpy%20%C3%96dev%20%C3%87%C3%B6z%C3%BCmleri.ipynb