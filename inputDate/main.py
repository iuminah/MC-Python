import re
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

print("Nhập ngày theo định dạng (dd/mm/yyyy) : ")
day1 = input()
currentDate = datetime.strptime(day1, "%d/%m/%Y")
print("Nhập ngày muốn tính khoảng cách (dd/mm/yyyy) : ")
day2 = input()
diffDay = datetime.strptime(day2, "%d/%m/%Y")

def checkParterm(str):
  parterm = re.match(r"\d{2}/\d{2}/\d{4}", str)
  return bool(parterm)

listStr = day1.split("/")

def newFormatString():
  res = currentDate.strftime("%Y-%m-%d")
  print(f'1/ Kết quả in ra màn hình là: "{res}"')

def next90day():
  res = (currentDate + timedelta(days=90)).strftime("%d/%m/%Y")
  print(f'2/ Ngày thứ 90 trong tương lai là ngày: "{res}"')

def back31Date():
  res = (currentDate - timedelta(days=31)).strftime("%d/%m/%Y")
  print(f'3/ Ngày thứ 31 trong quá khứ là ngày: "{res}"')

def subtract2Months():
  res = (currentDate - relativedelta(months=2)).strftime("%Y-%m-%d")
  print(f'4/ Trừ 2 tháng, thành: "{res}"')

def isLeapYear(year):
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f'5/ Từ source ở trên, năm "{year}" Có phải là năm nhuận')
  else:
    print(f'5/ Từ source ở trên, năm "{year}" Không phải là năm nhuận')

def splitDayMonthYear():
  year = f'Năm: {currentDate.year}'
  month = f'Tháng: {currentDate.month:02}'
  day = f'Ngày: {currentDate.day:02}'
  print(f"6/ Bóc tách chuỗi, từ đề bài, thành:\n{year}\n{month}\n{day}")

def getWeekDay(str):
  currentWeekDay = currentDate.strftime("%A")
  switcher = {
    "Monday": "Thứ hai",
    "Tuesday": "Thứ ba",
    "Wednesday": "Thứ tư",
    "Thursday": "Thứ năm",
    "Friday": "Thứ sáu",
    "Saturday": "Thứ bẩy",
    "Sunday": "Chủ nhật",
  }
  res = switcher.get(currentWeekDay)
  print(f'7/ Ngày "{str}" là "{res}"')

def distance2days():
  res = (diffDay - currentDate).days
  print(f'8/ Khoảng cách giữa ngày "{day1}" và ngày "{day2}" là: {abs(res)} ngày')

def sumOfString(str):
  arr = []
  for x in str:
    if x != "/": arr.append(int(x))
  res = sum(arr)
  print(f"9/ Print ra màn hình tổng các số trong chuỗi : {res}")

if checkParterm(day1) and checkParterm(day2):
  newFormatString()
  next90day()
  back31Date()
  subtract2Months()
  isLeapYear(currentDate.year)
  splitDayMonthYear()
  getWeekDay(day1)
  distance2days()
  sumOfString(day1)
elif checkParterm(day1) != True:
  print("Định dạng ngày không hợp lệ")
else:
  print("Định dạng ngày muốn tính khoảng cách không hợp lệ")