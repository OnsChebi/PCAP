birthday=input("enter your birthday in format YYYYMMDD ")
while len(birthday)>1:
    digitlife=0
    for i in  range(len(birthday)):
        digitlife+=int(birthday[i])
    birthday=str(digitlife)
print("your digit of life :",digitlife)
