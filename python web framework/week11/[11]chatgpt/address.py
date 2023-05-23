from faker import Faker
import openpyxl

fake = Faker('ko_KR')

# 엑셀 파일 생성
wb = openpyxl.Workbook()

# 시트 생성
ws = wb.active

# 헤더 정보 입력
ws.append(['이름', '이메일', '주소', '전화번호'])

# 레코드 생성
for i in range(10):
    name = fake.name()
    email = fake.email()
    address = fake.address()
    phone_number = fake.phone_number()
    
    ws.append([name, email, address, phone_number])

# 엑셀 파일 저장
wb.save('korean_address_book.xlsx')