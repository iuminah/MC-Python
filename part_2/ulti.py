import re


def checkContinue():
    check = input(
        "!-- Chưa nhập đúng định dạng, bạn có muốn thử lại không (y/n) ? : ")
    if check == "y" or check == "Y":
        return True
    else:
        return False


def getRange():
    startValue, endValue = [
        int(i) for i in input(
            "Nhập giá trị bắt đầu và kết thúc để tạo dẫy số (Hai giá trị được phân biệt bởi dấu cách): ").split()
    ]
    return startValue, endValue


def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f'Năm "{year}" Có phải là năm nhuận')
    else:
        print(f'Năm "{year}" Không phải là năm nhuận')


def checkParterm(str):
    parterm = re.match(r"\d{4}/\d{2}/\d{2}", str)
    return bool(parterm)
