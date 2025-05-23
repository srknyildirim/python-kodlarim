sayi = int(input("Faktöriyeli hesaplanacak sayiyi girin: "))
faktoriyel=1

if sayi<0:
    print("Negatif sayilarin faktöriyeli hesaplanamaz")
elif sayi == 0:
    print(sayi,"!= "+"1")
else:
    
    for i in range(1,sayi+1):
        faktoriyel*=i

    print(sayi,"!= " ,faktoriyel)