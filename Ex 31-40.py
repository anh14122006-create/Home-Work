# 31. Viết một chương trình Python để in các số sau đây, tối đa 2 chữ số thập phân, có dấu.
a1 = float(input('Nhập 1 số:'))
print('{:+.2f}'.format(a1))
# 32. Viết một chương trình Python để in các số dương và số âm sau đây, không có chữ số thập phân.
a2 = float(input('Nhập 1 số:'))
print(int(a2))
# 33. Viết một chương trình Python để in các số nguyên sau đây với số 0 nằm bên trái chiều rộng được chỉ định.
a3 = int(input('Nhập số nguyên:'))
rong = int(input('Chiều rộng:'))
print(f'{a3:0{rong}d}')
# 34. Viết một chương trình Python để in các số nguyên sau đây với dấu '*' nằm bên phải chiều rộng được chỉ định.
a4 = int(input('Nhập số nguyên:'))
chieu_rong = int(input('Chiều rộng:'))
print(f'{a4:*<{chieu_rong}d}')
# 35. Viết một chương trình Python để hiển thị một số với dấu phẩy phân cách.
a5 = int(input('Nhập số nguyên:'))
print(f'{a5:,}')
# 36. Viết một chương trình Python để định dạng một số với phần trăm.
a6 = float(input('Nhập số (0-1):'))
print('{:,2%}'.format(a6))
# 37. Viết một chương trình Python để hiển thị một số được căn trái, phải và giữa với chiều rộng là 10.
a7 = input('Nhập chuỗi:')
print('Căn trái:', f'{a7:<10}')
print('Căn phải:', f'{a7:>10}')
print('Căn giữa:', f'{a7:^10}')
# 38. Viết một chương trình Python để đếm số lần xuất hiện của một chuỗi con trong một chuỗi.
a8 = input('Nhập chuỗi:')
chuoi_con = input('Nhập chuỗi con cần đếm:')
count = a8.count(chuoi_con)
print(f"Số lần xuất hiện của '{chuoi_con}':{count}")
# 39. Viết một chương trình Python để đảo ngược một chuỗi.
a9 = input('Nhập chuỗi:')
print('Chuỗi đảo ngược:', a9[::-1])
# 40. Viết một chương trình Python để đảo ngược các từ trong một chuỗi.
a10 = input('Nhập chuỗi:')
words = a10.split()
reversed_words = words[::-1]
print(' '.join(reversed_words))
