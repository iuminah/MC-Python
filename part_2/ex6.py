from ulti import formatCurrency, rerunProgram


def calcSalary():
    workingHours = input("Nhập số giờ làm mỗi tuần : ")
    criteriaSalary = input("Nhập thù lao trên mỗi giờ tiêu chuẩn : ")
    criteriaHours = 40

    if type(workingHours) == float and type(criteriaSalary) == float:
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
