def sortAlphabet():
    inputString = input("Nhập một chuỗi các từ tách biệt bởi khoảng trắng : ")
    inputlist = inputString.split()
    filteredList = list(set(inputlist))
    filteredList.sort()

    res = ', '.join(str(i) for i in filteredList)
    print(f"4./ Các từ sau khi loại bỏ trùng lặp và sắp xếp lại : {res}")
