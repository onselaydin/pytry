def terscevir(s):
    if(type(s) != str):
        raise ValueError("Lütfen metin giriniz")
    else:
        return s[::-1] #ters çevir