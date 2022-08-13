
# from os import device_encoding
# from typing_extensions import Self




from distutils.log import error
from re import X
from tokenize import Special


ip =(input("enter your ip :"))

n=ip.split("/")
fulnum=n[0]
oct=fulnum.split(".")
mask=n[1]
length=len(fulnum)
oct1=int(oct[0])
oct2=int(oct[1])
oct3=int(oct[2])
oct4=int(oct[3])


# 0<= (oct2,oct3,oct4) <=255:


if  0<= oct1 <=127 and 0<= oct2 <=255 and 0<= oct3 <=255 and 0<= oct4 <=255  :
    if oct1 == 10 :
        print('class A : private ip range')
    elif oct1 == 127:
        print('class A : Special ip range')
    else:
       print('class A : public ip range')

elif 128<= oct1 <=191 and 0<= oct2 <=255 and 0<= oct3 <=255 and 0<= oct4 <=255  :
    if oct1 == 172 and 16<= (oct2) <=31 :
        print('class B : private ip range')
    else:
        print('class B : public ip range')

elif 192<= oct1 <=223 and 0<= oct2 <=255 and 0<= oct3 <=255 and 0<= oct4 <=255 :
    if oct1 == 192 and  (oct2) ==168 :
        print('class C : private ip range')
    else:   
        print('class C : public ip range')

elif 124<= oct1 <=239 and 0<= oct2 <=255 and 0<= oct3 <=255 and 0<= oct4 <=255 :
    print('class D : special')
elif 124<= oct1 <=239 and 0<= oct2 <=255 and 0<= oct3 <=255 and 0<= oct4 <=255 :
    print('class E : public ip range')

else:
    print("error")

