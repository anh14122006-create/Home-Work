# 21. Viết một hàm Python để chuyển đổi một chuỗi ký tự thành chữ hoa nếu nó chứa ít nhất 2 ký tự viết hoa trong 4 ký tự đầu tiên.
a1=input('Nhập chuỗi:')
count=0
for ch in a1[:4]:
    if ch.isupper():
        count += 1
if count>=2:
    ketqua21=a1.upper()
else:
    ketqua21=a1
print(ketqua21)
# 22. Viết một chương trình Python để sắp xếp một chuỗi ký tự theo thứ tự từ điển.
a2=input('Nhập chuỗi:')
chars=list(a2)
chars.sort()
ketqua22=''.join(chars)
print(ketqua22)
# 23. Viết một chương trình Python để xóa một dòng mới trong Python.
a3=input('Nhp chuỗi:')
ketqua23=a3.strip()
print(ketqua23)
# 24. Viết một chương trình Python để kiểm tra xem một chuỗi ký tự có bắt đầu bằng các ký tự được chỉ định hay không.
a4=input('Nhập chuỗi:')
chi_dinh=input('Nhập ký tự hoặc chuỗi được chỉ định:')
if a4[:len(chi_dinh)]==chi_dinh:
    print('Chuỗi bắt đầu bằng,', chi_dinh)
else:
    print('Chuỗi không bắt đầu bằng:', chi_dinh)
# 25. Viết một chương trình Python để tạo mã hóa Caesar.
a5=input('Nhập văn bản cần mã hóa:')
so_buoc=int(input('Nhập số bước dịch chuyển:'))
ketqua25=''
for char in a5:
    if char.isupper():
        ketqua25+=chr((ord(char)-65+so_buoc)%26+65)
    elif char.islower():
        ketqua25+=chr((ord(char)-97+so_buoc)%26+97)
    else:
        ketqua25+=char
print('Văn bản sau khi mã hóa Caesar:',ketqua25)
# 26. Viết một chương trình Python để hiển thị văn bản đã định dạng (chiều rộng = 50) dưới dạng đầu ra.
import textwrap
a6=input('Nhập văn bản:')
ketqua26=textwrap.fill(a6,width=50)
print('Văn bản sau khi định dạng:')
print(ketqua26)
# 27. Viết một chương trình Python để xóa thụt lề hiện có khỏi tất cả các dòng trong một văn bản cho trước.
print('Nhập văn bản (gõ enter 2 lần để kết thúc):')
lines=[]
while True:
    line=input()
    if line =='':
        break
    lines.append(line.lstrip())
print('Văn bản sau khi xóa thụt lề:')
for line in lines:
    print(line)
# 28. Viết một chương trình Python để thêm tiền tố văn bản vào tất cả các dòng trong một chuỗi.
print('Nhập văn bản (gõ enter 2 lần để kết thúc):')
Dong=[]
while True:
    dong=input()
    if dong =='':
        break
    Dong.append(dong)
tien_to=input('Nhập tiền tố:')
dong_moi=[]
for dong in Dong:
    dong_moi.append(tien_to+dong)
print('Văn bản sau khi thêm tiền tố:')
for dong in dong_moi:
    print(dong)
# 29. Viết một chương trình Python để thiết lập thụt lề cho dòng đầu tiên.
print('Nhập văn bản (gõ enter 2 lần để kết thúc):')
Dong1=[]
while True:
    dong1=input()
    if dong1 =='':
        break
    Dong1.append(dong1)
if Dong1:
    Dong1[0]=Dong1[0].lstrip()
print('Thụt lề dòng 1:')
for dong1 in Dong1:
    print(dong1)
# 30. Viết một chương trình Python để in các số sau với tối đa 2 chữ số thập phân.
numbers=input('Nhập các số:')
for n in numbers:
    num=float(n)
    print('{:.2f}'.format(num))