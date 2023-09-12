def sortAlphabet():
    inputString = input("Nhập một chuỗi các từ tách biệt bởi khoảng trắng : ")
    inputlist = inputString.split()
    res = list(set(inputlist))
    res.sort()

    print(f"4./ Các từ sau khi loại bỏ trùng lặp và sắp xếp lại : {res}")
