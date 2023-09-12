from ulti import getRange


def findEvenNumber():

    start, end = getRange()
    arr = list(range(start, end + 1))

    res = []
    for i in arr:
        if i % 2 == 0:
            res.append(i)
    print(f'5./ Các số chẵn trong đoạn "{start}" và "{end}" là : {res}')
    print(f"Tổng số : {len(res)}")
