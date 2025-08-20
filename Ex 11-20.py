# 11. Viết một chương trình Python để loại bỏ các ký tự có giá trị chỉ mục lẻ trong một chuỗi cho trước.
a = input('Nhập chuỗi:')
ketqua11 = ''
for i in range(len(a)):
    if i % 2 == 0:
        ketqua11 += a[i]
print(ketqua11)
# 12. Viết một chương trình Python để đếm số lần xuất hiện của mỗi từ trong một câu cho trước.
b = input('Nhập 1 câu:')
words = b.split()
word_count = {}
for w in words:
    if w in word_count:
        word_count[w] += 1
    else:
        word_count[w] = 1
print(word_count)
# 13. Viết một tập lệnh Python nhận dữ liệu đầu vào từ người dùng và hiển thị dữ liệu đầu vào đó bằng cả chữ hoa và chữ thường.
c = input('Nhập chuỗi:')
print('Chữ hoa', c.upper())
print('Chữ thường', c.lower())
# 14. Viết một chương trình Python nhận một chuỗi các từ được phân tách bằng dấu phẩy làm đầu vào và in ra các từ riêng biệt theo dạng đã được sắp xếp (theo chữ và số).
d = input('Nhập các từ, cách nhau bằng dấu phẩy:')
tu = d.split(',')
tu.sort()
print(','.join(tu))
# 15. Viết một hàm Python để tạo một chuỗi HTML với các thẻ bao quanh từ.
tag = input('Nhập thẻ:')
text = input('Nhập nội dung:')
e = '<' + tag + '>' + text + '<' + tag + '>'
print(e)
# 16. Viết một hàm Python để chèn một chuỗi vào giữa một chuỗi.
f1 = input('Nhập chuỗi gốc:')
f2 = input('Nhập chuỗi cần chèn:')
mid = len(f1) // 2
ketqua16 = f1[:mid] + f2 + f1[mid:]
print(ketqua16)
# 17. Viết một hàm Python để lấy một chuỗi được tạo thành từ 4 bản sao của hai ký tự cuối cùng của một chuỗi được chỉ định (độ dài phải ít nhất là 2).
g = input('Nhập chuỗi (ít nhất 2 ký tự):')
if len(g) < 2:
    print('Chuỗi lỗi')
else:
    last = g[-2:]
    g = last * 4
    print(g)
# 18. Viết một hàm Python để lấy một chuỗi được tạo thành từ ba ký tự đầu tiên của một chuỗi được chỉ định.
# Nếu độ dài của chuỗi nhỏ hơn 3, hãy trả về chuỗi ban đầu
h = input('Nhập chuỗi:')
if len(h) < 3:
    ketqua18 = h
else:
    ketqua18 = h[:3]
print(ketqua18)
# 19. Viết một chương trình Python để lấy phần cuối của một chuỗi trước một ký tự được chỉ định.
j = input('Nhập chuỗi:')
kytu = input('Nhập ký tự cần tách:')
pos = j.find(kytu)
if pos != -1:
    ketqua19 = j[:pos]
else:
    ketqua19 = j
print(ketqua19)
# 20. Viết một hàm Python để đảo ngược một chuỗi nếu độ dài của nó là bội số của 4.
l = input('Nhập chuỗi:')
if len(l) % 4 == 0:
    ketqua20 = l[::-1]
else:
    ketqua20 = l
print(ketqua20)