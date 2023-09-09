import re
from ulti import checkContinue, getRange
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def findNumbersWithConditional():
    condition = True
    customRange = []
    result = []

    def toSatisfyCondition():
        for x in customRange:
            if (x % 7 == 0) and (x % 5 != 0):
                result.append(x)

    while condition:
        try:
            startValue, endValue = getRange()
            customRange = list(range(startValue, endValue + 1))
            toSatisfyCondition()
            break
        except ValueError as response:
            if bool(response):
                condition = checkContinue()

    if len(result) != 0:
        print(
            f"1./ Các số chia hết cho 7 và không chia hết cho 5 trong đoạn '{startValue}' và '{endValue}' là : " + ", ".join(
                map(str, result)),
        )
        print(f"Tổng số : {len(result)}")


def findMuliples():

    condition = True
    customRange = []
    obj = {}

    while condition:
        try:
            startValue, endValue = getRange()
            customRange = list(range(startValue, endValue + 1))
            break
        except ValueError as response:
            if bool(response):
                condition = checkContinue()

    if len(customRange) != 0:
        for i in customRange:
            obj[i] = i*i
        print(
            f"2./ Có 1 chuỗi từ {startValue} đến {endValue} tạo ra 1 chuỗi là bội số của chúng là :"
        )
        print(obj)


findNumbersWithConditional()
findMuliples()
