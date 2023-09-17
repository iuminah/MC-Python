from ulti import formatCurrency, rerunProgram


def calcSalary():
    workedHours = float(input("Nhập số giờ làm mỗi tuần : "))
    criteriaSalary = float(input("Nhập thù lao trên mỗi giờ tiêu chuẩn : "))
    criteriaHours = 40

    if type(workedHours) == float and type(criteriaSalary) == float:
        salaryOT = float(criteriaSalary) * 1.5
        hoursOT = float(workedHours) - 40
        netIncome = float(criteriaSalary) * float(workedHours)

        if hoursOT > 0:
            incomeWithOT = (float(criteriaSalary) * criteriaHours) + \
                (hoursOT * salaryOT)
            formatCurrency(incomeWithOT)
        else:
            formatCurrency(netIncome)
    else:
        rerunProgram(calcSalary)
