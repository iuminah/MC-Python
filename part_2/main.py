from ulti import showListProgram, rerunProgram
from ex1 import findNumbersWithConditional
from ex2 import findMuliples    
from ex3 import caclAge
from ex4 import sortAlphabet
from ex5 import findEvenNumber
from ex6 import calcSalary


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
    else:
        print("Done")


def runFile():
    showListProgram()
    selected = input("Chọn chương trình bạn muốn chạy : ")
    if type(selected) == int:
        selectProgram(selected)
    else:
        rerunProgram(runFile)


runFile()
