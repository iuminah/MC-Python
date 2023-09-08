import re
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def findNumbersWithConditional():

    condition = True
    customRange = []
    result = []

    def getRange():
        start, end = [int(x) for x in input(
            "Nhập giá trị bắt đầu và kết thúc để tạo dẫy số (Hai giá trị được phân biệt bởi dấu cách): ").split()
        ]
        return start, end

    def satisfyCondition():
        for x in customRange:
            if (x % 7 == 0) and (x % 5 != 0):
                result.append(x)

    while condition:
        try:
            start, end = getRange()
            customRange = list(range(start, end + 1))
            satisfyCondition()
            break
        except ValueError as res:
            if bool(res):
                print("!-- Bạn chưa nhập đúng định dạng")
                check = input("Bạn có muốn nhập lại không (y/n) ? : ")
                if check == "y" or check == "Y":
                    condition = True
                else:
                    condition = False

    if len(result) != 0:
        print(
            f"Các số chia hết cho 7 và không chia hết cho 5 trong đoạn {start} và {end} là :")
        print(", ".join(map(str, result)))


findNumbersWithConditional()
