import os
"""
Dosya kipleri:
x dosya olluşturmak için
w sıfırdan yazmak için
a devamından yazmak için
r okumak için

"""


file = open("log.txt", "w" , encoding="utf-8")

for i in range(25):
    file.write(str(i) + ",")

file = open("log.txt", "r" , encoding="utf-8")

print(file.read())


with open("log.txt", "a") as f:
    f.write("\n")

    for i in range(25):
        f.write(str(i))


