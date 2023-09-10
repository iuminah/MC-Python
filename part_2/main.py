from ulti import checkContinue, getRange, checkParterm, isLeapYear
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
        check = input(
            "!-- Chưa nhập đúng định dạng, Bạn muốn thử lại không (y/n) : ")
        if check == "y" or check == "Y":
            caclAge()


def sortAlphabet():
    inputString = input("Nhập một chuỗi các từ tách biệt bởi khoảng trắng : ")

    arrString = ["dab, bc, ab, ab"]

    arrString.sort()

    print(arrString)


def allProgram():
    findNumbersWithConditional()
    findMuliples()
    caclAge()
    # sortAlphabet()


def showListProgram():
    print("1 : Tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5, nằm trong đoạn")
    print("2 : Tạo ra 1 chuỗi là bội số của chúng và in ra kết quả dạng list")
    print("3 : Tính tuổi từ ngày tháng năm sinh và cho biết năm sinh có phải năm nhuận không")
    print("0 : Chạy lần lượt từng chương trình")


def selectProgram(selected):
    switcher = {
        1: findNumbersWithConditional,
        2: findMuliples,
        3: caclAge,
        0: allProgram
    }
    switcher.get((selected), lambda: print("Done"))()

    rerun = input("Bạn có muốn chạy chương trình khác không (y/n) : ")
    if rerun == "y" or rerun == "Y":
        selectAgain = int(input("Chọn chương trình bạn muốn chạy : "))
        showListProgram()
        selectProgram(selectAgain)


if __name__ == "__main__":
    showListProgram()
    selected = int(input("Chọn chương trình bạn muốn chạy : "))
    selectProgram(selected)
