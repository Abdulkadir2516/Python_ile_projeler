import xlsxwriter

real_data = [[],[],[]]
real_data[0] = ["k_ad","şifre","ad","soyad","tel"]
real_data[1] = ["greenrock","2516","Abdulkadir","Yeşilkaya","5459727734"]
real_data[2] = ["deneme","1234","test","dene","555125354"]

workbook = xlsxwriter.Workbook('users.xlsx')

worksheet = workbook.add_worksheet()

for i in range(len(real_data)):
    for j in range(len(real_data[i])):
        worksheet.write(i, j, real_data[i][j])

workbook.close()

"""


"""