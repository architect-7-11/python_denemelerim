
def mukemmel_mi(func):
    def ekstra(sayilar):
        toplamlar = list()
        i = 1
        while i < sayilar:
            if sayilar % i == 0:
                toplamlar.append(i)
                i +=1
            else:
                i +=1

        if sum(toplamlar) == sayilar:
            print(sayilar)

        func(sayilar)

    return ekstra



@mukemmel_mi
def asal_mi(sayi):
    durum = True
    for i in range(2,sayi):
        if sayi % i == 0:
            durum = False
    if durum :
        print("mükemmel")
    else:
        print("mükemmel değil")



print(asal_mi(13))

