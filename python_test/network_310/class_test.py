from math import sqrt


class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.getter
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def show(self):
        if self._age < 10:
            print('小学生')
        else:
            print('中学生')


class Student(Person):

    def __init__(self, name, age, grade):
        super(Student, self).__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self):
        if self._grade > 3:
            print('study math')
        else:
            print('study english')


class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) *
                    (half - self._b) * (half - self._c))


def io_test():
    file_name = ('a.txt', 'b.txt', 'c.txt')
    file_open = []

    try:
        for name in file_name:
            fw = open(name, 'w', encoding='utf-8')
            file_open.append(fw)
        for number in range(1, 10000):
            if number < 500:
                file_open[0].write(str(number) + ' ')
            elif number < 5000:
                file_open[1].write(str(number) + ' ')
            else:
                file_open[2].write(str(number) + ' ')

    except IOError as er:
        print(er)
        print('write error')

    finally:
        for fw in file_open:
            fw.close()


def main():
    per = Person('jpf', 18)
    print('name : ' + f'{per.name}')
    per.show()
    per.age = 9
    per.show()

    stu = Student('zjx', 13, 4)
    stu.show()
    stu.study()
    stu.grade = 2
    stu.show()
    stu.study()

    if Triangle.is_valid(3, 4, 5):
        tri = Triangle(3, 4, 5)
        area = tri.area()
        print('the tri\'s area is ' + f'{area}')

    # io_test()


if __name__ == '__main__':
    main()
