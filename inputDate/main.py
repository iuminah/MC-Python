import re
import datetime

input = input("Nhập ngày theo định dạng (dd/mm/yyyy) : ")

parterm = re.match(r"\d{2}/\d{2}/\d{4}", input)

listStr = input.split("/")

listInt = []

for i in listStr:
  listInt.append(int(i))


def newFormatString(str):
  res = f'"{str[2]}-{str[1]}-{str[0]}"'
  print(f"1/ Kết quả in ra màn hình là: {res}")

def splitDayMonthYear(str):
  year = f"Năm: {str[2]}"
  month = f"Tháng: {str[1]}"
  day = f"Ngày: {str[0]}"
  print(f"6/ Bóc tách chuỗi, từ đề bài, thành:\n{year}\n{month}\n{day}")

def getWeekDay(input):
  currentWeekDay = (datetime.datetime(input[2], input[1], input[0])).strftime("%A")
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
  print(f'7/ Ngày "2023-08-29" là {res}')

# newFormatString(listStr)
# splitDayMonthYear(listStr)

getWeekDay(listInt)