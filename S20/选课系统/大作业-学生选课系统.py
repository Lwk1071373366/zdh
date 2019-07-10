import sys
import hashlib
import pickle
import os
class Course:
    def __init__(self,name,price,period,teacher):
        self.name = name
        self.price = price
        self.period = period
        self.teacher = teacher
class User(object):
    def show_courses(self):
        with open('course_info','rb') as f :
            count = 1
            while True:
                try:
                    course = pickle.load(f)
                    print('%s %s,%s,%s,%s'%(count,course.name,course.price,course.period,course.teacher))
                    count += 1
                except EOFError:
                    print()
                    break
class Manager(User):   # 管理员用户
    opt_lst = [('创建课程','create_course'),('给学生创建账号','create_student'),
               ('查看所有课程','show_courses'),('查看所有学生','show_students'),
               ('查看所有学生的选课情况','show_students_courses'),('退出','quit')]
    def __init__(self,name):
        self.name  = name
    def create_course(self):  # 创建课程
        print('in Manager create_course')
        course_name = input('课程名：')
        price = input('课程价格：')
        period = input('课程周期：')
        teacher = input('授课老师：')
        course = Course(course_name,price,period,teacher)
        with open('course_info','ab') as f :
            pickle.dump(course,f)
        print('创建%s课程成功\n'%course_name)
    def create_student(self): # 给学生创建账号
        print('in Manager create_student')
        username = input('用户名：')
        password = input('密码：')
        with open('userinfo','a',encoding='utf-8') as f :
            f.write('%s|%s|Student\n'%(username,get_md5(username,password)))
        stu = Student(username)
        with open('student_info','ab') as f :
            pickle.dump(stu,f)
        print('创建%s学生账号成功\n'%username)

    def show_students(self): # 查看所有学生
        print('in Manager show_students')
        with open('student_info','rb') as f :
            count = 1
            while True:
                try:
                    student = pickle.load(f)
                    print('%s %s'%(count,student.name))
                    count += 1
                except EOFError:
                    print()
                    break

    def show_students_courses(self): # 查看所有学生的选课情况
        print('in Manager show_students_courses')
        with open('studtnt_info','rb') as f :
            count = 1
            while True:
                try:
                    stu = pickle.load(f)
                    name_lst = [course.name for course in stu.courses]
                    print('%s %s: %s'%(count,stu.name,','.join(name_lst)))
                    count +=1
                except EOFError:
                    break
    @classmethod
    def init(cls,username):
        managet = cls(username)
        return managet
    def quit(self):
        exit()

class Student(User):
    opt_lst = [('查看所有课程','show_courses'), ('查看已选课程','show_selected_course'),
               ('选择课程','choose_course'), ('退出','quit')]
    def __init__(self,name):
        self.name  = name
        self.courses = []

    def show_selected_course(self):  # 查看已选课程
        print('in Student show_selected_course')
        for index,course in enumerate(self.courses,1):
            print('%s %s,%s,%s,%s'%(index,course.name,course.price,course.period,course.teacher))

    def choose_course(self):         # 选择课程
        print('in Student choose_course')
        flag = False
        self.show_courses()
        num = int(input('请输入课程序号：'))
        with open('course_info','rb') as f :
            count = 1
            while True:
                try:
                    obj = pickle.load(f)
                    if count == num:
                        self.courses.append(obj)
                        flag = True
                        break
                    count += 1
                except EOFError:
                    print('请输入有效的课程编号：')
                    break
        if flag:
            print('选择%s课程成功'% obj.name)
            with  open('student_info','rb') as f1 ,open('student_info.bak','wb') as f2:
                while True:
                    try:
                        obj = pickle.load(f1)
                        if obj.name ==self.name:
                            pickle.dump(self,f2)
                        else:
                            pickle.dump(obj,f2)
                    except EOFError:
                        break
            os.remove('student_info')
            os.rename('student_info.bak','student_info')
    @staticmethod
    def init(name):
        with open('student_info','rb') as f :
            while True:
                try:
                    stu = pickle.load(f)
                    if stu.name == name:
                        return stu
                except EOFError:
                    break
    def quit(self):
        exit()


def get_md5(usr,pwd):
    md5 = hashlib.md5(usr.encode('utf-8'))
    md5.update(pwd.encode('utf-8'))
    return md5.hexdigest()

def login(usr,pwd):
    with open('userinfo',encoding='utf-8') as f:
        for line in f:
            username,password,ident = line.strip().split('|')
            if usr == username and get_md5(usr,pwd) == password:
                return {'result':True,'identify':ident,'username':usr}
        else: return {'result':False}

def auth():
    opt_lst1 = ['登录','退出']
    while True:
        for index,opt in enumerate(opt_lst1,1):
            print(index,opt)
        num = int(input('请输入你要做的操作 :'))
        if num == 1:
            usr = input('username :')
            pwd = input('password :')
            ret = login(usr,pwd)
            if ret['result']:
                print('登录成功')
                return ret
            else:
                print('登录失败')
        elif num == 2:
            exit()


ret = auth()
print(ret)
if ret['result']:
    if hasattr(sys.modules[__name__],ret['identify']):
        # sys.modules[__name__]表示找到的当前文件所在的内存空间
        # ret['identify']只能是'Manager','Student'
        # hasattr(sys.modules[__name__],ret['identify'])判断当前的空间中有没有Student或者Manager这个名字
        cls = getattr(sys.modules[__name__],ret['identify'])
        obj = cls(ret['username'])
        # cls 要么 == Student类的内存地址,要么 == Manager类的内存地址
        while True:
            for index,opt in enumerate(cls.opt_lst,1):
                print(index,opt[0])
            num = int(input('请选择您要操作的序号 :'))
            if hasattr(obj,cls.opt_lst[num-1][1]):
                getattr(obj,cls.opt_lst[num-1][1])()

