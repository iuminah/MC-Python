from ulti import checkParterm, isLeapYear, rerunProgram
from datetime import datetime


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
