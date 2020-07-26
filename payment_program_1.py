class Person:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def get_id(self):
        return self.__id

    def set_id(self, value):
        self.__id = value

        # name get,set

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value


class Admin(Person):
    def __init__(self, id, name):
        Person.__init__(self, id, name)

    def __str__(self):
        # return "name = %s, pay=%d" % (self.get_id())
        return


class Employee(Person):
    def __init__(self, id, name, pay, deduction, salary, bonus):
        Person.__init__(self, id, name)
        self.__pay = pay
        self.__deduction = deduction
        self.__salary = salary
        self.__bonus = bonus

    # def get_admin(self):
    #     return self.__admin  # 관리자는 set 없음.!

    # pay get,set
    def get_pay(self):
        return self.__pay

    def set_pay(self, value):
        self.__pay = value

    # deduction get, set
    def get_deduction(self):
        return self.__deduction

    def set_deduction(self, value):
        self.__deduction = value

    def get_realpay(self):
        return self.__pay - self.__deduction + self.__bonus

    # salary get,set
    # bonus get,set
    def __str__(self):
        # return 'name = %s, age = %d' % (self.name, self.age)
        # return str(self.__id)
        return "이름 = %s, 월급=%d, 공제액=%d, 보너스=%d, || 실수령액='%d'입니다." % (
            self.get_name(), self.__pay, self.__deduction, self.__bonus, self.get_realpay())


persons = [
    Employee(1997, "문상태", 200, 50, 150, 20),  # False 는 그냥 안넣어도 댐
    Admin(0000, "고문영"),
    Employee(1991, "임행태", 400, 50, 350, 20)
]


def show_all():
    for person in persons:
        if type(person) is Employee:
            print(person)


# id 검색
def find_id(id):
    for i in persons:
        if id == i.get_id():
            return i


##############
who_ru = int(input("사번을 입력하세요: "))
searched = find_id(who_ru)

if type(searched) is Employee:
    print(searched)
else:
    show_all()

# print(employees[0])
# find_id(1991)
