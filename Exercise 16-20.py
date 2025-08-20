# 16. Viết một hàm Python để chèn một chuỗi vào giữa một chuỗi.
a1 = input('Nhập chuỗi gốc:')
a2 = input('Nhập chuỗi cần chèn:')
mid = len(a1) // 2
a = a1[:mid] + a2 + a1[mid:]
print(a)
# 17. Viết một hàm Python để lấy một chuỗi được tạo thành từ 4 bản sao của hai ký tự cuối cùng của một chuỗi được chỉ định (độ dài phải ít nhất là 2).
b = input('Nhập chuỗi (ít nhất 2 ký tự):')
if len(b) < 2:
    print('Chuỗi lỗi')
else:
    last = b[-2:]
    b = last * 4
    print(b)
# 18. Viết một hàm Python để lấy một chuỗi được tạo thành từ ba ký tự đầu tiên của một chuỗi được chỉ định.
# Nếu độ dài của chuỗi nhỏ hơn 3, hãy trả về chuỗi ban đầu
c = input('Nhập chuỗi:')
if len(c) < 3:
    result = c
else:
    result = c[:3]
print(result)
# 19. Viết một chương trình Python để lấy phần cuối của một chuỗi trước một ký tự được chỉ định.
d = input('Nhập chuỗi:')
kytu = input('Nhập ký tự cần tách:')
pos = d.find(kytu)
if pos != -1:
    ket_qua = d[:pos]
else:
    ket_qua = d
print(ket_qua)
# 20. Viết một hàm Python để đảo ngược một chuỗi nếu độ dài của nó là bội số của 4.
e = input('Nhập chuỗi:')
if len(e) % 4 == 0:
    ketqua = e[::-1]
else:
    ketqua = e
print(ketqua)
