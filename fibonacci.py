sayi1=input("sayi1 :")
sayi2=input("sayi2 :")
a=int(sayi1)
b=int(sayi2)
c=0
i=0

lst=[a,b]

while True:

    c=lst[i]+lst[i+1]
    lst.append(c) 
    i=i+1
    if i==10:
        break
    print(lst)