from ulti import getRange, checkContinue


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
