start = int(input("Enter start number: "))
Stop = int(input("Enter Stop number:"))

skip = int(input("Enter Skip number"))

for i in range(start,Stop):
    if i == skip:
        continue;
    print(i)