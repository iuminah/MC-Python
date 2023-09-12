from ulti import getRange, checkContinue


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
