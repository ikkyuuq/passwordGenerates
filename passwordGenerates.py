import random
import string

levels = {'Easy':6, 'Normal':8, 'Hard':12, 'Extream':20} #จัดหมวดหมู่ ระดับความปลอดภัยในรูปแบบ Dictionary

print('Password generate started!')
print('Levels of the stregth are Easy, Normal, Hard, and Extream')
user_input = input('How stregth of the password: ') #ให้ user input ระดับความปลอดภัยที่ต้องการ

def passwordGenerate():
  if user_input in levels: #ถ้า user input อยู่ใน Vairiables levels ที่เป้น dictionary
    N = levels.get(user_input) #ให้ N ดึงค่า value มาจาก dict ที่ตรงกับ user_input
    generatePass = ''.join(random.choices(string.ascii_letters + string.digits, k=N)) #สุ่มตัวเลขและตัวอักษรตามจำนวน N
    print('Your password is: '+ generatePass)
  else: print('Incorrect Commands.') #หาก user input ไม่อยู่ใน dict levels

passwordGenerate()

#ขก.
while True: 
  user_command = input('Do you want to generate password again? (Y/N)')
  if user_command == 'Y':
    user_input = input('How stregth of the password: ')
    N = levels.get(user_input)
    passwordGenerate()
    continue
  else: break
