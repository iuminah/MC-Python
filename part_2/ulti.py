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


def showListProgram():
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print("| 1 : Tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5, nằm trong đoạn                                                   |")
    print("| 2 : Tạo ra 1 chuỗi là bội số của chúng và in ra kết quả dạng list                                                                    |")
    print("| 3 : Tính tuổi từ ngày tháng năm sinh và cho biết năm sinh có phải năm nhuận không                                                    |")
    print("| 4 : Đầu vào là một chuỗi các từ tách biệt bởi khoảng trắng, loại bỏ các từ trùng lặp, sắp xếp theo thứ tự bảng chữ cái, rồi in chúng |")
    print("| 5 : Tìm số chẵn nằm trong đoạn                                                                                                       |")
    print("| 6 : Tính số tiền thực lĩnh. Biết số giờ tiêu chuẩn mỗi tuần là 40 giờ và mỗi giờ vượt chuẩn được trả gấp rưỡi so với giờ làm chuẩn   |")
    print("| 0 : Chạy lần lượt từng chương trình trên                                                                                             |")
    print("----------------------------------------------------------------------------------------------------------------------------------------")


def formatCurrency(amount):
    currencyFormated = "{:,.0f} đ".format(amount)
    print(f"6./ Số tiền thực lĩnh của nhân viên là : {currencyFormated}")


def rerunProgram(program):
    rerun = input(
        "Giá trị vừa nhập không hợp lệ, Bạn muốn thử lại không (y/n) : ")
    if rerun == "y" or rerun == "Y":
        program()
    else:
        print("Done")
