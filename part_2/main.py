from ulti import checkContinue, getRange, checkParterm, isLeapYear, showListProgram, formatCurrency, rerunProgram
from datetime import datetime


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


def caclAge():
    curentYear = int(datetime.now().strftime("%Y"))
    inputDob = input(
        "Nhập ngày, tháng, năm sinh theo định dạng (yyyy/mm/dd) : ")

    userDob = int(inputDob[:4])

    validateInput = checkParterm(inputDob)

    if validateInput:
        age = curentYear - userDob
        print(f"3./ Tuổi của người này là : {age}", end=". ")
        isLeapYear(userDob)
    else:
        rerunProgram(caclAge)


def sortAlphabet():
    inputString = input("Nhập một chuỗi các từ tách biệt bởi khoảng trắng : ")
    inputlist = inputString.split()
    res = list(set(inputlist))
    res.sort()

    print(f"4./ Các từ sau khi loại bỏ trùng lặp và sắp xếp lại : {res}")


def findEvenNumber():

    start, end = getRange()
    arr = list(range(start, end + 1))

    res = []
    for i in arr:
        if i % 2 == 0:
            res.append(i)
    print(f'5./ Các số chẵn trong đoạn "{start}" và "{end}" là : {res}')
    print(f"Tổng số : {len(res)}")


def calcSalary():
    workingHours = input("Nhập số giờ làm mỗi tuần : ")
    criteriaSalary = input("Nhập thù lao trên mỗi giờ tiêu chuẩn : ")
    criteriaHours = 40

    if type(float(workingHours)) is float and type(float(criteriaSalary)) is float:
        salaryOT = float(criteriaSalary) * 1.5
        hoursOT = float(workingHours) - 40
        netIncome = float(criteriaSalary) * float(workingHours)

        if hoursOT > 0:
            incomeWithOT = (float(criteriaSalary) * criteriaHours) + \
                (hoursOT * salaryOT)
            formatCurrency(incomeWithOT)
        else:
            formatCurrency(netIncome)
    else:
        rerunProgram(calcSalary)


def allProgram():
    findNumbersWithConditional()
    findMuliples()
    caclAge()
    sortAlphabet()
    findEvenNumber()
    calcSalary()


def selectProgram(selected):
    switcher = {
        1: findNumbersWithConditional,
        2: findMuliples,
        3: caclAge,
        4: sortAlphabet,
        5: findEvenNumber,
        6: calcSalary,
        0: allProgram
    }

    switcher.get(int(selected), lambda: print("Chưa có chương trình này."))()

    rerun = input("Bạn có muốn chạy chương trình khác không (y/n) : ")
    if rerun == "y" or rerun == "Y":
        showListProgram()
        selectAgain = int(input("Chọn chương trình bạn muốn chạy : "))
        selectProgram(selectAgain)


def runFile():
    showListProgram()
    selected = input("Chọn chương trình bạn muốn chạy : ")
    if type(int(selected)) is int:
        selectProgram(selected)
    else:
        rerunProgram(runFile)


runFile()
