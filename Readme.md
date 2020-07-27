# 임금 관리 프로그램


###  동작 순서
1.사번 입력.

2.입력된 사번이 관리자일 때:
  사원들의 모든 정보 리스트를 열람.(관리자 정보는 제외)
  
3.입력된 사번이 일반 사원일 때:
  자신의 임금 정보만 확인 가능.
  
#### 'Person' 클래스

    class Person:
        def __init__(self, id, name):
            self.__id = id
            self.__name = name
            
        # id get,set
        def get_id(self):
            return self.__id

        def set_id(self, value):
            self.__id = value

        # name get,set
        def get_name(self):
            return self.__name

        def set_name(self, value):
            self.__name = value
            
-'Person' 클래스를 상속받는 'Admin' 클래스.
    class Admin(Person):
        def __init__(self, id, name):
            Person.__init__(self, id, name)

        def __str__(self): #문자열로 리턴
            return

-'Person' 클래스를 상속받는 'Employee' 클래스.

    class Employee(Person):
    def __init__(self, id, name, position, pay, deduction, bonus):
        Person.__init__(self, id, name)
        self.__position = position
        self.__pay = pay
        self.__deduction = deduction
        self.__bonus = bonus
            
#### 함수 구현

    # def get_admin(self):
    #     return self.__admin  -> 관리자는 set 없음. 있어서는 안되므로..

    # positon get,set
    def get_position(self):
        return self.__position

    def set_position(self, value):
        self.__position = value
        
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

    def get_realpay(self):  #realpay:실수령액
        return self.__pay - self.__deduction + self.__bonus

    # bonus get,set
    def __str__(self):
        # return 'name = %s, age = %d' % (self.name, self.age)
        # return str(self.__id)
        return "이름: %s, 직급: %s, || 월급:%d, 공제액:%d, 보너스:%d, || 실수령액:'%d'입니다." % (
            self.get_name(), self.get_position(), self.__pay, self.__deduction, self.__bonus, self.get_realpay())


#### 직원, 관리자 정보. '모든 사람 리스트':

    persons = [
    Employee(1997, "문상태", "대리", 200, 50, 20),  # False 는 그냥 안넣어도 댐
    Admin(0000, "고문영"),
    Employee(1991, "임행태", "팀장", 400, 50, 20)
]


#### 관리자용 모든 리스트 볼 수 있는 함수:

    def show_all():
        for person in persons:
            if type(person) is Employee:
                print(person)

#### id 찾는 함수:

    # id 검색
    def find_id(id):
        for i in persons:
            if id == i.get_id():
                return i


#### 메인 부분:

    who_ru = int(input("사번을 입력하세요: "))
    searched = find_id(who_ru)

    if type(searched) is Employee:
        print(searched)
    else:
        show_all()


-------------------------
+ 참고자료:
+ 클래스 상속
<https://stackoverflow.com/questions/4935587/python-getting-baseclass-values-from-derived-class>

+ toString() 객체 문자열로 출력
  __str__ 를 이용한다.

    class Person(object):

        name = ''
        age = 0
        def __init__(self, name='', age=0):

                self.name = name
                self.age = age

        def __str__(self):
                return 'name = %s, age = %d'%(self.name, self.age)

     k = Person( 'kim', '22' )
     print k
<https://codeng.tistory.com/60>

+ 파이썬 클래스
<https://wikidocs.net/16071>
