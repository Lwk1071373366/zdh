import os
import pickle
from core.log import log
from core.auth import Authentic
from core.course import Course
from conf.settings import userinfo,course_info,student_info

class User(object):
    @staticmethod
    def load_obj(file_path):
        with open(file_path, 'rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    yield obj
                except EOFError:
                    break

    @staticmethod
    def dump_obj(file_path, obj):
        with open(file_path, 'ab') as f:
            pickle.dump(obj, f)

    def show_courses(self):  # 查看所有课程
        for count, course in enumerate(self.load_obj(course_info), 1):
            print('%s %s' % (count, course))
        print()


class Manager(User):  # 管理员用户
    opt_lst = [('创建课程', 'create_course'), ('给学生创建账号', 'create_student'),
               ('查看所有课程', 'show_courses'), ('查看所有学生', 'show_students'),
               ('查看所有学生的选课情况', 'show_students_courses'), ('退出', 'quit')]

    def __init__(self, name):
        self.name = name

    def create_course(self):  # 创建课程
        print('in Manager create_course')
        course_name = input('课程名 :')
        price = input('课程价格 :')
        period = input('课程周期 :')
        teacher = input('授课老师 :')
        course = Course(course_name, price, period, teacher)
        # 将课程对象记录到文件
        self.dump_obj(course_info, course)
        print('创建%s课程成功\n' % course_name)
        log.logger.info('%s创建%r课程成功' % (self.name, course))

    def create_student(self):  # 给学生创建账号
        print('in Manager create_student')
        username = input('用户名 :')
        password = input('密码 :')
        with open(userinfo, 'a', encoding='utf-8') as f:
            f.write('%s|%s|Student\n' % (username, Authentic(username, password).get_md5()))
        stu = Student(username)
        self.dump_obj(student_info, stu)
        print('创建%s学生账号成功.\n' % username)
        log.logger.info('%s创建%s学生成功' % (self.name, stu))

    def show_students(self):  # 查看所有学生
        print('in Manager show_students')
        for count, stu in enumerate(self.load_obj(student_info), 1):
            print('%s %s' % (count, stu))
        print()

    def show_students_courses(self):  # 查看所有学生的选课情况
        print('in Manager show_students_courses')
        for count, stu in enumerate(self.load_obj(student_info), 1):
            name_lst = [course.name for course in stu.courses]
            print('%s %s : %s' % (count, stu, ','.join(name_lst)))
        print()

    @classmethod
    def init(cls, username):
        manager = cls(username)
        return manager

    def quit(self):
        exit()


class Student(User):
    opt_lst = [('查看所有课程', 'show_courses'), ('查看已选课程', 'show_selected_course'),
               ('选择课程', 'choose_course'), ('退出', 'quit')]

    def __init__(self, name):
        self.name = name
        self.courses = []

    def __str__(self):
        return self.name

    def show_selected_course(self):  # 查看已选课程
        for index, course in enumerate(self.courses, 1):
            print('%s %s' % (index, course))

    def choose_course(self):  # 选择课程
        flag = False
        self.show_courses()  # 1. PYTHON    2.LINUX
        num = int(input('请输入课程的序号'))  # 1
        for index, course in enumerate(self.load_obj(course_info), 1):
            if index == num:
                self.courses.append(course)
                flag = True
                break
        else:
            print('请输入有效的序号')
        if flag:
            print('选课%r成功' % course)
            with open('student_info.bak', 'wb') as f2:
                for stu in self.load_obj(student_info):
                    if stu.name == self.name:
                        pickle.dump(self, f2)
                    else:
                        pickle.dump(stu, f2)
            os.remove(student_info)
            os.rename('student_info.bak', student_info)
            log.logger.info('%s选择%r课程成功' % (self.name, course))

    @classmethod
    def init(cls, name):
        for stu in cls.load_obj(student_info):
            if stu.name == name:
                return stu

    def quit(self):
        exit()

