import numpy as np
import pandas as pd
from numpy.random import randn

labels_list = ["Önsel","Yağmur","Şennur","Ege","Pınar","Polat","Meriç"]
data_list = [10, 20, 30, 40, 50, 60, 70]
final_list = pd.Series(data_list, labels_list)
#print(final_list)
data_dict = {"Önsel":30,"Yağmur":40,"Şennur":50} # data dictionery
#print(pd.Series(data_dict))
#NaN not a number
ser2017 = pd.Series([5,10,14,20],["Buğday","Mısır","Kiraz","Erik"])
ser2018 = pd.Series([2,12,12,6],["Buğday","Mısır","Çilek","Erik"])
#print(ser2017 + ser2018)
total = ser2017 + ser2018
#print(total["Erik"])

#Dataframe ve filtreler
df = pd.DataFrame(randn(4,3),["A","B","C","D"],["Col1","Col2","Col3"])
#print(df > -1)
#booleanDf = df > 0
#print(df[booleanDf])
#print(df[df > -2])
#print(df[(df["Col1"] > 0) & (df["Col2"] > 0)]) # iki kolona göre AND li filtreleme
#print(df[(df["Col1"] > 0) | (df["Col2"] > 0)]) # iki kolona göre OR li filtreleme
#df["Col4"] = ["one","two","tree","four"]  # yeni sütun eklemek
#print(df)

#pre process nan(not a number) ile başa çıkma
arr = np.array([[10,20,np.nan],[5,np.nan,np.nan],[21,np.nan,10]])
#print(arr)
df = pd.DataFrame(arr,index = ["id1","id2","id3"],columns=["Col1","Col2","Col3"])
#print(df)
#df.dropna() # Bunu printlersek hiçbir veri elimizde kalmayacak. her satıra bakıyor nan varsa siliyor.
#df.dropna(axis = 1) # sadece 1.sütuna bakacak ve nan varsa silecek.
#df.dropna(thresh = 2) # satıra 2 adet number veri varsa silmeyecek.
#print(df.sum()) # satırlardaki sayılrı toplar.
#print(df.sum().sum()) 
#print(df.size) # veri sayımızı verir.
#print(df.isnull().sum()) # sütunlarda sadece nan olanları sayar
"""
def calculateMean(df):
    totalSum = df.sum().sum()
    totalNum = df.size - df.isnull().sum().sum()
    return totalSum / totalNum

print(df.fillna(value = calculateMean(df)))
"""

"""
dataset = {
    "Departman":["Bilişim","İnsan Kaynakları", "Üretim","Üretim","Bilişim","İnsan Kaynakları"],
    "Çalışan":["Mustafa","Jale","Kadir","Zeynep","Murat","Ahmet"],
    "Maaş":[3000,3500,2500,4500,4000,2000]
}
df = pd.DataFrame(dataset)
print(df)
print(df.groupby("Departman").sum()) # gruplanmışların maaşlarının toplamı.
print(df.groupby("Departman").sum().loc["Bilişim"]) # Sadece bilişim gurubunun toplam maaşları.
print(int(df.groupby("Departman").sum().loc["Bilişim"])) # sadece integer değerini verdi.
print(df.groupby("Departman").count()) # her departmandaki çalışan sayısı.
print(df.groupby("Departman").min()) # en az maaş alanlar. max ilede en çok maaş alanlar döner.
print(df.groupby("Departman").min()["Maaş"]["Bilişim"]) # sadece maaş sütunu en az rakamla döner.
#mean ile ortalama maaşları bulabiliriz. 
"""

"""
# concatenation, join, merge
dataset1 = {
    "A": ["A1","A2","A3","A4"],
    "B": ["B1","B2","B3","B4"],
    "C": ["C1","C2","C3","C4"]
}
dataset2 = {
    "A": ["A5","A6","A7","A8"],
    "B": ["B5","B6","B7","B8"],
    "C": ["C5","C6","C7","C8"]
}

df1 = pd.DataFrame(dataset1,index = [1,2,3,4])
df2 = pd.DataFrame(dataset2,index = [5,6,7,8])
#print(df1)
print(pd.concat([df1,df2])) # iki tabloyu birleştirdik.

"""

"""
df = pd.DataFrame({
    "Col1":[1,2,3,4,5,6],
    "Col2":[100,100,200,300,300,100],
    "Col3":["Ali","Veli","Hasan","Ayşe","Fatma","Hasan"]
})
print(df.head(n=3)) # ilk 3 kaydı getirir.
print(df["Col2"].unique()) # sql deki distinct gibi.

def times3(x):
    return x * 3
print(df["Col2"].apply(times3)) # times3 fonnsiyonunu her rakam için çağırır ve çarpma işlemini getirir.

onsel = lambda x : x * 2
print(onsel(4))

print(df["Col2"].apply(lambda x : x * 2))

print(df.columns) #sütunları listeler
print(len(df.index)) # satır sayısını verir
print(df.sort_values("Col2",ascending=False)) #Col2 ye göre sıralar
"""

#pivot table
df = pd.DataFrame({
    "Ay":["Mart","Nisan","Mayıs","Mart","Nisan","Mayıs","Mart","Nisan","Mayıs"],
    "Şehir":["Ankara","Ankara","Ankara","İstanbul","İstanbul","İstanbul","İzmir","İzmir","İzmir"],
    "Nem":[10,25,50,21,67,80,30,70,75]
})
print(df)
print(df.pivot_table(index="Ay",columns="Şehir",values="Nem"))