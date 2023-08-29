import re
input = input("Nhập ngày theo định dạng (dd/mm/yyyy) : ")

parterm = re.match(r"\d{2}/\d{2}/\d{4}", input)

str = input.split("/")

def newFormatString(str):
  res = f'"{str[2]}-{str[1]}-{str[0]}"'
  print(f"1/ Kết quả in ra màn hình là: {res}")

