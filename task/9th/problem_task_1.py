class Department:
    def __init__(self, name):
        self.name = name
        self.course_list = {}

    def add_course(self, course_name, credit, lecturer):
        course = Course(course_name, credit, lecturer)
        self.course_list[course.name] = course
        return course

    def del_course(self, course):
        if course.name not in self.course_list:
            print("error: %s course가 존재하지 않습니다." % course)
            return
        if self.course_list[course.name].del_course():
            self.course_list.pop(course.name)
        else:
            print("교과목이 삭제되지 않았습니다.")


class Course:
    def __init__(self, name, credit, lecturer):
        self.name = name
        self.credit = credit
        self.lecturer = lecturer
        self.student_list = []

    def __str__(self):
        return 'Course Name: "%s" and Credit: %s' % (self.name, self.credit)

    def add_student(self, student):
        self.student_list.append(student)

    def del_student(self, student):
        if student not in self.student_list:
            print("error: %s 학생이 존재하지 않습니다." % student.name)
            return
        if (
            input(
                "%s 학생을 제명하시겠습니까? 맞다면 1을 입력해주세요 : " % student.name
            )
            == "1"
        ):
            student.course_list.remove(self)
            self.student_list.remove(student)
        else:
            print("삭제가 취소되었습니다.")

    def del_course(self):
        if (
            input("%s 코스를 삭제하시겠습니까? 맞다면 1을 입력해주세요 : " % self.name)
            == "1"
        ):
            for student in self.student_list:
                student.course_list.remove(self)
            self.student_list.clear()
            return True
        else:
            print("삭제가 취소되었습니다.")
            return False

    def print_student_list(self):
        for student in self.student_list:
            print("%s" % student.name)


class Student:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.course_list = []

    def enroll(self, course):
        self.course_list.append(course)
        course.add_student(self)

    def del_course(self, course):
        if course not in self.course_list:
            print("error: %s 코스가 등록되지 않았습니다." % course.name)
            return
        if (
            input(
                "%s 코스를 등록 취소하시겠습니까? 맞다면 1을 입력해주세요 : "
                % course.name
            )
            == "1"
        ):
            course.student_list.remove(self)
            self.course_list.remove(course)
        else:
            print("등록 취소가 취소되었습니다")

    def print_course_list(self):
        for course in self.course_list:
            print("%s" % course.name)


def main():
    dept = Department("Dept. of Computer Eng.")

    math1 = dept.add_course("Math for Engineering", 3, "Kim")
    math2 = dept.add_course("Discrete math", 2, "Lee")
    math3 = dept.add_course("Concrete math", 3, "Han")

    print("Dept. of %s has such below courses" % dept.name)
    for c in dept.course_list.values():
        print(c)
    print()

    std = {}
    std[2020001] = Student("Kim", 2020001)
    std[2020007] = Student("Lee", 2020007)
    std[2020010] = Student("Park", 2020010)

    std[2020001].enroll(math1)
    std[2020001].enroll(math3)

    std[2020007].enroll(math2)
    std[2020007].enroll(math1)

    std[2020010].enroll(math1)
    std[2020010].enroll(math2)
    std[2020010].enroll(math3)

    print("\n===== Student Course List =====")
    for k, v in std.items():
        print("ID %d registered courses:" % k)
        v.print_course_list()
        print()

    print("\n===== Course Student List =====")
    for c in dept.course_list.values():
        print("Course:", c.name)
        c.print_student_list()
        print()

    print("\n===== Delete Test =====")
    print("- Student 2020007 drops Discrete math")
    std[2020007].del_course(math2)

    print("\nAfter deletion")
    print("Student 2020007 Course List")
    std[2020007].print_course_list()

    print("\nCourse Discrete Math Student List")
    math2.print_student_list()


if __name__ == "__main__":
    main()
