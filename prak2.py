a = float (input("masukan angka pertama:"))
b = float (input("masukan angka kedua:"))
c = float (input("masukan angka ketiga:"))

if a >= b and a >= c:
    largest = a
elif b >= a and b >=c:
    largest = b
elif c >= a and c >=b:
    largest = c

else:
    print ("tidak adaa nilai terbesar")

print ("angka terbesar adalah:",largest)