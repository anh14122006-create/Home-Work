# 1. Write a Python program to calculate the length of a string.
a = input('Nhập chuỗi để tính độ dài chuỗi đó:')
print(len(a))
# 2. Write a Python program to count the number of characters (character frequency) in a string.
b = input('Nhập chuỗi đếm tần suất ký tự:')
print('Kết quả:', end="")
check = ''
for ch in b:
    if ch not in check:
        count = 0
        for c in b:
            if c == ch:
                count += 1
        print(f"'{ch}':{count},", end="")
        check += ch
print('')
# 3. Write a Python program to get a string made of the first 2 and last 2 characters of a given
c = input('Nhập chuỗi lấy 2 kí tự đầu và 2 ký tự cuối:')
if len(c) < 2:
    print('Chuỗi rỗng')
else:
    two_first = c[:2]
    two_last = c[-2:]
    print('Kết quả:', two_first + two_last)
# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
d = input('Nhập chuỗi tất cả ký tự đầu đổi thành $, ngoại trừ ký tự đầu tiên:')
ky_tu_dau = d[0]
ket_qua = ky_tu_dau
for char in d[1:]:
    if char == ky_tu_dau:
        ket_qua += '$'
    else:
        ket_qua += char
print('Kết quả:', ket_qua)
# 5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
e1 = input('Nhập chuỗi 1:')
e2 = input('Nhập chuỗi 2:')
e1_first = e1[:2]
e2_first = e2[:2]
e1_rest = e1[2:]
e2_rest = e2[2:]
e3 = e2_first + e1_rest
e4 = e1_first + e2_rest
result = e3 + ' ' + e4
print('Kết quả:', result)
# 6. Viết một chương trình Python để thêm 'ing' vào cuối một chuỗi cho trước (độ dài chuỗi phải ít nhất là 3).
# Nếu chuỗi đã cho trước đã kết thúc bằng 'ing', hãy thêm 'ly'. Nếu độ dài chuỗi của chuỗi đã cho nhỏ hơn 3, giữ nguyên.
f = input('Nhập chuỗi:')
if len(f) < 3:
    print(f)
elif f[-3:] == 'ing':
    f += 'ly'
    print(f)
else:
    f += 'ing'
    print(f)
# 7. Viết một chương trình Python để tìm lần xuất hiện đầu tiên của các chuỗi con 'not' và 'poor' trong một chuỗi cho trước.
# Nếu 'not' theo sau 'poor', hãy thay thế toàn bộ chuỗi con 'not'...'poor' bằng 'good'. Trả về chuỗi kết quả.
g = input('Nhập chuỗi:')
pos_not = -1
for i in range(len(g) - 2):
    if g[i:i + 3] == 'not':
        pos_not = i
        break
pos_poor = -1
for i in range(len(g) - 3):
    if g[i:i + 4] == 'poor':
        pos_poor = i
        break
if pos_not != -1 and pos_poor != -1 and pos_poor > pos_not:
    ketqua7 = g[:pos_not] + 'good' + g[pos_poor + 4:]
else:
    ketqua7 = g
print('Kết quả:', ketqua7)
# 8. Viết một hàm Python nhận một danh sách các từ và trả về từ dài nhất cùng độ dài của từ dài nhất.
h = input('Nhập các từ:')
words = h.split()
longest_word = ""
max_length = 0
for word in words:
    if len(word) > max_length:
        longest_word = word
        max_length = len(word)
print('Từ dài nhất:', longest_word)
print('Độ dài:', max_length)
# 9.Viết một chương trình Python để xóa ký tự chỉ mục thứ n khỏi một chuỗi không rỗng
j = input('Nhập chuỗi:')
n = int(input('Nhập vị trí ký tự cần xóa:'))
j = j[:n] + j[n + 1:]
print('Kết quả:', j)
# 10.Viết một chương trình Python để chuyển một chuỗi đã cho thành một chuỗi mới, trong đó ký tự đầu tiên và ký tự cuối cùng đã được hoán đổi.
k = input('Nhập chuỗi:')
if len(k) <= 1:
    ketqua10 = k
else:
    ketqua10 = k[-1] + k[1:-1] + k[0]
print(ketqua10)
