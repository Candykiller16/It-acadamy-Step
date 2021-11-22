from collections import Counter

def convertToNumbers(myList):
    newList = []
    for i in myList:
        newList.append(int(i))
    return newList

def readFile(filename):
    myList = []
    with open(filename) as f:
        for line in f:
            line = line.strip().split()  # избавляемся от знака \n и дробим по пробелам
            lst = convertToNumbers(line)
            myList.extend(lst)
    return myList


readFile('input.txt')

def tas1_to_task_5():
    listOne = readFile('input.txt')
    sumList = sum(listOne)
    minList = min(listOne)
    maxList = max(listOne)
    count_unical_numbers = len(set(listOne))
    c = Counter(listOne)

    result_string = ''
    for k, v in c.items():
        result_string += str(k) + '\t' + str(v) + '\n'

    with open('result.txt', 'w') as f:
        f.write('Сумма всех чисел в списке -> ' + str(sumList) + '\n')
        f.write('Максимальное = ' + str(maxList) + ' и минимальное = ' + str(minList) + ' числа в списке' + '\n')
        f.write('Cколько всего уникальных чисел содержится в списке -> ' + str(count_unical_numbers) + '\n')
        f.write(result_string)

tas1_to_task_5()


def task_6():
    b = set(readFile('input_1.txt'))
    a = set(readFile('input.txt'))
    with open('result1.txt', 'w') as f:
        for e in list(a.difference(b)):
            f.write(str(e) + '\n')

    with open('result2.txt', 'w') as f:
        for el in list(b.difference(a)):
            f.write(str(el) + '\n')

    with open('result3.txt', 'w') as f:
        for ele in list(a.union(b)):
            f.write(str(ele) + '\n')

    with open('results4.txt', 'w') as f:
        for elem in list(a.intersection(b)):
            f.write(str(elem) + '\n')

task_6()