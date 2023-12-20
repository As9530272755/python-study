'''
1.显示功能界面
2.用户输入功能序号
3.按照用户输入的功能序号，执行不同的功能(函数)
'''
class_info = []

# 1.定义功能界面函数
def info_print():
    """
    功能界面
    """
    print("请选择功能--------------")
    print("1.添加学员")
    print("2.删除学员")
    print("3.修改学员信息")
    print("4.查询学员信息")
    print("5.显示所有学员")
    print("6.退出系统")
    print("-"*30)

# 4.实现添加学员功能函数
def add_student():
    """
    注释信息：通过 help 查看
    添加学员函数
    """
    
    new_id = input("输入学号:")
    new_name = input("输入姓名:")
    new_tel = input("输入手机号:")

    # 声明 class_info 为全局变量
    global class_info

    # 遍历取出列表单个数据，应为单个数据为字典，这通过 name key 与 new_name 做判断是否相同
    for i in class_info:
        if new_name == i["name"]:
            print(f"{new_name}该用户已经存在")
            return
        
    # 创建 student_dict 字典来接收不存的新学员信息
    student_dict = {}

    # 将用户输入的数据追加至 student_dict
    student_dict['id'] = new_id
    student_dict['name'] = new_name
    student_dict['tel'] = new_tel

    # 通过 append 将学员信息追加至 class_info
    class_info.append(student_dict)

    print(class_info)

def del_student():
    """
    注释信息：通过 help 查看
    删除学员函数
    """

    del_name = input("请输入需要删除的学员名称：")

    global class_info
    for i in class_info:
        if del_name == i["name"]:
            class_info.remove(i)
            print(del_name,"学员删除成功!")
            break
    else:
        print(del_name,"学员未注册")
        print(class_info)
    print(class_info)

# 修改函数
def modify_student():
    """
    注释信息：通过 help 查看
    修改学员信息函数
    """

    # 查找学员接收用户输入数据
    modify_name = input("输入需要修改的学员：")

    global class_info

    # for 循环判断用户是否存在
    for i in class_info:
        if modify_name == i["name"]:
            # 直接通过 input 获取数据，并赋值
            i['tel'] = print("请输入修改手机号：")

            # 修改了上述条件之后终止循环
            break
    else:
        print("用户名输入有误")

    print(class_info)

# 查询函数
def query_student():
    """
    该函数通过输入用户名实现查询
    """

    query_name = input("请输入需要查询的姓名：")
    global class_info

    for i in class_info:
        if query_name == i["name"]:
            print(f"学员查询结果学号：{i['id']},姓名：{i['name']},手机号：{i['tel']}")
            break
    else:
        print("查询用户有误!")

# 查询所有信息
def query_all():
    """
    查看所有学员信息
    """
    print('学员\t姓名\t手机号\t')
    for i in class_info:
        print(f'{i["id"]}\t{i["name"]}\t{i["tel"]}')



# 系统功能需要循环使用，直到用户输入 6 才退出系统
# 通过 while true 实现无限循环
while True:
    info_print()

    # 2.用户输入功能序号
    # 由于 input 会将用户输入的内容转换为 str 类型，所以通过 int 转换数据类型
    select_num = int(input("请输入功能序号:"))

    # 3.根据用户输入的功能序列号，执行不同的功能通过函数实现
    if select_num == 1:
        add_student()
    elif select_num == 2:
        del_student()
    elif select_num == 3:
        modify_student()
    elif select_num == 4:
        query_student()
    elif select_num == 5:
        query_all()
    elif select_num == 6:
        exit_flag = input("是否退出程序:(yes or no)")
        if exit_flag == "yes" :
            # break 退出循环并实现退出程序
            break
    else:
        # 因为在功能中只有 1-6 这几个功能，所以当用户输入其他数字的时候就提示功能有误
        print("输入功能序号有误,请重新选择!")
