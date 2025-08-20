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
