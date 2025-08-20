# 11. Viết một chương trình Python để loại bỏ các ký tự có giá trị chỉ mục lẻ trong một chuỗi cho trước.
a = input('Nhập chuỗi:')
result = ''
for i in range(len(a)):
    if i % 2 == 0:
        result += a[i]
print(result)
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
