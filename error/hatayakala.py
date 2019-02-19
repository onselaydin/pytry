try:
    a = int("1234abcd")
    print(a)
except:
    print("Bir hata oluştu")
finally:
    print("Hata olsada olmasada çalış")