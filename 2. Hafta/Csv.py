import csv

file = open("log.csv", "w")

for i in range(30):
    file.write(str(i) + ",")

for i in range(30):
    file.write(str(i) + "\n")

file = open("log.csv", "r")

okuyucu = csv.reader(file)

a = list(okuyucu)

for i in range(20):
    print(a[i])

carp = []
x = []
for i in range(10):
    x.clear()
    for j in range(10):
       x.append(i*j)
    carp.append(x)

print(carp)
"""
with open("create.csv", mode="w") as f:
    yaz = csv.writer(f)
    yaz.writerows(x)
"""


csv_f = csv.writer(open("create.csv", mode="w"))

csv_f.writerows(carp)

csv_f = open("create.csv", "r")

okuyucu = list(csv.reader(csv_f))

print(okuyucu)


real_data = [[],[],[]]
real_data[0] = ["k_ad","şifre","ad","soyad","tel"]
real_data[1] = ["greenrock","2516","Abdulkadir","Yeşilkaya","5459727734"]
real_data[2] = ["deneme","1234","test","dene","555125354"]

print(real_data)

with open("users.csv", mode="w", encoding="utf-8") as user:
    write = csv.writer(user)
    for i in real_data:
        write.writerow(i)

dosya = open("users.csv", mode="r", encoding="utf-8")

dizi = list(csv.reader(dosya))

print(dizi)




