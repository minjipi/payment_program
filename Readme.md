## 임금 관리 프로그램


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
