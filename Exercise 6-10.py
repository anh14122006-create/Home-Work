# 6. Viết một chương trình Python để thêm 'ing' vào cuối một chuỗi cho trước (độ dài chuỗi phải ít nhất là 3).
# Nếu chuỗi đã cho trước đã kết thúc bằng 'ing', hãy thêm 'ly'. Nếu độ dài chuỗi của chuỗi đã cho nhỏ hơn 3, giữ nguyên.
a = input('Nhập chuỗi:')
if len(a) < 3:
    print(a)
elif a[-3:] == 'ing':
    a += 'ly'
    print(a)
else:
    a += 'ing'
    print(a)
# 7. Viết một chương trình Python để tìm lần xuất hiện đầu tiên của các chuỗi con 'not' và 'poor' trong một chuỗi cho trước.
# Nếu 'not' theo sau 'poor', hãy thay thế toàn bộ chuỗi con 'not'...'poor' bằng 'good'. Trả về chuỗi kết quả.
b = input('Nhập chuỗi:')
pos_not = -1
for i in range(len(b) - 2):
    if b[i:i + 3] == 'not':
        pos_not = i
        break
pos_poor = -1
for i in range(len(b) - 3):
    if b[i:i + 4] == 'poor':
        pos_poor = i
        break
if pos_not != -1 and pos_poor != -1 and pos_poor > pos_not:
    b = b[:pos_not] + 'good' + b[pos_poor + 4:]
else:
    b
print('Kết quả:', b)
# 8. Viết một hàm Python nhận một danh sách các từ và trả về từ dài nhất cùng độ dài của từ dài nhất.
c = input('Nhập các từ:')
words = c.split()
longest_word = ""
max_length = 0
for word in words:
    if len(word) > max_length:
        longest_word = word
        max_length = len(word)
print('Từ dài nhất:', longest_word)
print('Độ dài:', max_length)
# 9.Viết một chương trình Python để xóa ký tự chỉ mục thứ n khỏi một chuỗi không rỗng
d = input('Nhập chuỗi:')
n = int(input('Nhập vị trí ký tự cần xóa:'))
d = d[:n] + d[n + 1:]
print('Kết quả:', d)
# 10.Viết một chương trình Python để chuyển một chuỗi đã cho thành một chuỗi mới, trong đó ký tự đầu tiên và ký tự cuối cùng đã được hoán đổi.
e = input('Nhập chuỗi:')
if len(e) <= 1:
    result = e
else:
    first = e[0]
    last = e[-1]
    middle = e[1:-1]
    result = last + middle + first
print(result)
