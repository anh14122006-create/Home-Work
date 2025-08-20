# 41. Viết một chương trình Python để tách một tập hợp các ký tự khỏi một chuỗi.
a1 = input('Nhập chuỗi:')
duy_nhat = set(a1)
print('Các ký tự duy nhất:', duy_nhat)
# 42. Viết một chương trình Python để đếm các ký tự lặp lại trong một chuỗi.
a2 = input('Nhập chuỗi:')
lap_lai = {}
for char in a2:
    if a2.count(char) > 1:
        lap_lai[char] = a2.count(char)
print('Các ký tự lặp lại và số lần xuất hiện:', lap_lai)
# 43. Viết một chương trình Python để in ra các ký hiệu hình vuông và hình lập phương trong diện tích của một hình chữ nhật và thể tích của một hình trụ.
# Hình chữ nhật
dai = float(input('Chiều dài:'))
rong = float(input('Chiều rộng:'))
dien_tích_hcn = dai * rong
print('Diện tích hình chữ nhật là:', dien_tích_hcn, '\u2B1B')
# Hình trụ
import math

r = float(input('Bán kính hình trụ:'))
cao = float(input('Chiều cao hình trụ:'))
the_tich_tru = math.pi * pow(r, 2) * cao
print('Thể tích hình trụ:', the_tich_tru, '\U0001F7E6')
# 44. Viết một chương trình Python để in ra chỉ số của một ký tự trong một chuỗi.
a4 = input('Nhập chuỗi:')
ky_tu = input('Nhập ký tự cần tìm:')
if ky_tu in a4:
    print(f"Chỉ số của '{ky_tu}'là:", a4.index(ky_tu))
else:
    print('Không tìm thấy ký tự trong chuỗi')
# 45. Viết một chương trình Python để kiểm tra xem một chuỗi có chứa tất cả các chữ cái trong bảng chữ cái hay không.
import string

a5 = input('Nhập chuỗi:').lower()
alphabet = set(string.ascii_lowercase)
if alphabet.issubset(set(a5)):
    print('Chuỗi chứa tất cả chữ cái trong bảng chữ cái')
else:
    print('Chuỗi không chứa tất cả các chữ cái trong bảng chữ cái')
# 46. Viết một chương trình Python để chuyển đổi một chuỗi đã cho thành một danh sách các từ.
a6 = input('Nhập chuỗi:')
words = a6.split()
print('Danh sách các từ:', words)
# 47. Viết một chương trình Python để viết thường n ký tự đầu tiên trong một chuỗi.
a7 = input('Nhập chuỗi:')
n = int(input('Nhập số ký tự đầu tiên viết thường:'))
ketqua47 = a7[:n].lower() + a7[n:]
print(ketqua47)
# 48. Viết chương trình Python để hoán đổi dấu phẩy và dấu chấm trong một chuỗi.
a8 = input('Nhập chuỗi:')
a8 = a8.replace(',', 'temp').replace('.', ',').replace('temp', '.')
print(a8)
# 49. Viết chương trình Python để đếm và hiển thị nguyên âm trong văn bản.
a9 = input('Nhập văn bản:').lower()
nguyen_am = 'aeiou'
count = 0
for char in a9:
    if char in nguyen_am:
        count += 1
print('Số lượng nguyên âm:', count)
# 50. Viết chương trình Python để tách một chuỗi theo lần xuất hiện cuối cùng của dấu phân cách.
a10 = input('Nhập chuỗi:')
sep = input('Nhập ký tự phân cách:')
if sep in a10:
    index = a10.rfind(sep)
    part1 = a10[:index]
    part2 = a10[index + 1:]
    print('Phần trước dấu phân cách cuối cùng:', part1)
    print('Phần sau dấu phân cách cuối cùng:', part2)
else:
    print('Không tìm thấy ký tự phân cách')
