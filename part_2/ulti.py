
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
