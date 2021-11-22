from statistics import mean


class Book:
    def __init__(self, name, author, publ, genre, pub_year):
        self.name = name
        self.author = author
        self.publishing = publ
        self.genre = genre
        self.pub_year = pub_year


class Student:
    def __init__(self, surname='', name='', age='', number='', group='', semester='', budg_or_plat=''):
        self.__surname = surname  # фамилия студента
        self.__name = name  # имя студента
        self.__age = age  # возраст студента
        self.__number = number  # телефон
        self.__group = group  # номер группы
        self.__semester = semester  # номер семестра
        self.__BudgOrPlat = budg_or_plat  # форма обучения (бюджетная или платная)
        self.__subj_and_marks = {}  # данные о сданных предметах и оценках за них

    def setInfo(self):  # заполняет поля объекта данными, введенными из консоли
        self.__surname = input('Введите имя студента: ')
        self.__name = input('Введите фамилию студента: ')
        self.__age = int(input('Введите возраст студента: '))
        self.__number = input('Введите номер студента: ')
        self.__group = input('Введите номер группы студента: ')
        self.__semester = input('Введите номер семестра студента: ')
        self.__BudgOrPlat = input('Введите форму обучения студента(бюджет или платная): ')
        self.__subj_and_marks = {input('Введите предмет: '): int(input('Введите оценку: '))}
        for i in range(3):
            self.__subj_and_marks[input('Введите предмет который хотите добавить: ')] = int(
                input('Введите оценку по предмету, которую хотите '
                      'добавить: '))

    def getRating(self):  # возвращает информацию про средний балл студента
        return mean(self.__subj_and_marks[k] for k in self.__subj_and_marks)

    def getCourseList(self):  # возвращает список предметов, по которым полученый балл выше указанного
        lst = []
        k = int(input('Введите число, чтобы получить список предметов: '))
        for key, value in self.__subj_and_marks.items():
            if value > k:
                lst.append(key)
        return lst

    def printInfo(self):  # выводит информацию о студенте на консоль
        return self.__surname, self.__name, self.__age, self.__number, self.__group, self.__semester, \
               self.__BudgOrPlat, self.__subj_and_marks

    def getBudgOrPlat(self):
        return self.__BudgOrPlat

    def getSurname(self):
        return self.__surname


# st1  = Student()
# st1.printInfo()
# st1.setInfo()
# print(st1.printInfo())
# print(st1.getRating())
# print(st1.getCourseList())


# Дополнительное задание
st1 = Student('Архипов', 'Антон', '20', '+3754548184', 'M115', '4', 'бюджет')
st2 = Student('Ялтов', 'Алексей', '25', '+37544116549', 'У115', '3', 'платная')
st3 = Student('Громов', 'Артем', '45', '+37525648919', 'Р115', '5', 'платная')
st4 = Student('Длтов', 'Роман', '89', '+37525984989', 'П115', '5', 'платная')

my_list = [st1, st2, st3, st4]


def findForm(form):
    for st in my_list:
        if st.getBudgOrPlat() == form:
            print(st.printInfo())


# findForm('платная')


def sortBySurname(st):
    return st.getSurname()


def studentBySurname():
    my_list.sort(key=sortBySurname)
    for i in my_list:
        print(i.printInfo())

# studentBySurname()
