def peace_list(list_one,list_two,list_one_name,list_two_name):
    peace = []
    #list_one_name = input('第一个集合的昵称为: ')
    #list_two_name = input('第二个集合的昵称为: ')

    for the in list_one:
        if the in list_two:
            o = int(the)
            peace.append(o)
            list_two.remove(the)
            print('元素' + str(the) + '迁移成功!')

        else:
            print('元素' + str(the) + '不在集合[' + list_two_name + ']中! 已跳过.')
    print('所有元素已迁移完成!')
    
    return peace

#A = peace_list([1,2,3],[2,3,4])
#print(A)

def seve_list(name):
    ones = []
    print('这是一个依次输入元素以创建集合的程序.')
    chose = input("如果为单元素集合请输入'E',如果是多元素集合请输入'L'")

    if chose == 'E':
        input("你是大傻子吗,老子出的题里横是一个单元素集合都没有.")
        input("没有返回程序,你重开吧")
        while True:
            print("笨蛋!")

    elif chose == 'L':
        print("好的,接下来请依次输入集合中的元素,如果输入完毕后按'q'后回车")
        while True:
            one = input("请输入元素后回车(输入'q'停止添加):")
            if one != 'q':
                ones.append(one)
                print('\n元素 [' + str(one) + '] 添加完成!\n')

            elif one == 'q':
                break
    else:
        input("让你输入'E'或者'L',你输了个什么玩意.你没救了 重开吧")
        while True:
            print("笨蛋!")
    print("\n集合 [" + name + "] 创建完毕!\n")
    return ones
    

#C = seve_list('C')
#print(C)

def draw_list(list_one,list_two,list_one_name,list_two_name,list_between='list_between'):
    venn = {}
    venn[list_one_name] = [list_one]
    venn[list_two_name] = [list_two]
    venn[list_between] = []
    same = ""
    
    for the in list_one:
        for thes in list_two:
            if the == thes:
                venn[list_between].append(the)
            #else:
                #venn[list_one_name].append(the)
    #for thee in list_two:
        #for thees in list_one:
            #if thee == thees:
                #venn[list_two_name].append(thee)
    if venn[list_between] == []:
        same = "没有交集 图像为两个离婚的圆圈"
    elif venn[list_between] == venn[list_one_name]:
        same = "所得交集和集合" + list_one_name + "一致,图像为父子圆圈"
    elif venn[list_between] == venn[list_two_name]:
        same = "所得交集和集合" + list_two_name + "一致,图像为母子圆圈"
    else:
        same = "所得交集和其他两个集合都不一致 图像为相亲相爱一家人"

    print("集合分类完成!")
    down = input("可按'W'查看结果")
    if down == 'W':
        print(venn)
        print("结果为:")
        print(same)
    else:
        print("行吧 这就是我的一生了 sad... EMO TIME")

#W = draw_list([1,2,4],[2,4,6],'D','F')

def list_len(list):
    print("开始执行元素个数获取程序")
    num = len(list)
    print("完成!")

    return num

def zero_one(num,list_print):
    print("开始执行字符转换程序.")
    num_list = []
    
    for a in range(0,int(num)):
        num_list.append(0)
    print("已创建"+str(num)+"个0组成的集合")
    #print(num_list)
    for one in list_print:
        num_list[int(one)-1] = 1
        print("元素["+str(one)+"]转换完成!")
    print("\n已完成所有转换工作!")

    return num_list

#print(zero_one(5,[2,3,4,5]))
