from main import draw_list,seve_list,peace_list,list_len,zero_one

print("现在我将一步步引导你使用这个程序\n")
input("按任意键继续:")
print("按'e'开始创建集合")
down = input(' ')
if down == 'e':
    lists = {}
    print("开始运行集合创建程序")
    while True:
        name = input("请为即将出生的集合起个名字\n")
        names = seve_list(name)
        lists[name] = names
        active = input("还想多生几个就按'e',不想生了就按'q'")
        if active == 'q':
            print("集合创建完毕.")
            print("你共创建了以下集合:")
            for k,v in lists.items():
                print("集合"+ str(k) + "="+ str(v))
            break
else:
    input("不是让你输'e'吗 你输入了个什么玩意")
    input("对对对 你打开这程序不是为了创建集合")
    input("就是玩对吧   就是想试试输别的会发生什么对吧")
    input("这是数学课奥 我希望你认真对待")
    input("现在 停止一切活动 把我关掉 重新打开 并输入'e' 做个听话的好孩子")
    input("没听懂吗?? 关掉我!")
    input("行吧 屡教不改 你纯纯的找骂  那我就成全你")
    while True:
        print("笨蛋!")

input("\n现在你已经完成了集合的创建")
input("虽然不知道你生了几个集合")
input("但我目前只用得到两个")
input("因为我想求她们的交集 :) ")
input("输入任意键运行求交集程序 :)\n ")
list_one_name = input('第一个集合的昵称为(别输错了!): ')
list_two_name = input('第二个集合的昵称为(别输错了!): ')
#print(lists[list_two_name])
peace_list = peace_list(lists[list_one_name],lists[list_two_name],list_one_name,list_two_name)
print("所得交集为:\n")
print(peace_list)
