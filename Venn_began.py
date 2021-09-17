"""from main import Question

questions = 'file/questions.txt'
answers = 'file/nswers.txt'
choices = 'file/choices.txt'
one = Question(questions,answers,choices)
one.get_anything()
one.show_hello()
input("找个人来上来做\n")
while one.active:
    try:
        one.pop_up()
        one.show_question()
        one.check_choice()
    except IndexError:
        one.active = False
one.check_print_mistake()
one.show_grade()
"""



qulist = ["1.(不定项)已知集合A= { 1, 3, 5 }, 集合B= { X | X**2-X-6＜0, XEN* },U={ 1, 2, 3, 4, 5}, 则Cu(AnB) = ___?(E=属于)",
               "2.(单选)已知第一题的条件,且U的子集可表示成由0,1组成的五位字符串,如{ 2, 4 }表示自左向右的第二个字符和第四个是 1 ,其余均为0,即{ 2, 4 }表示为01010,则10010的真子集个数为____?",
               "3.(多选)已知第一题和第二题的条件,且集合C=Cu(AnB),集合D={X | X=a/2},若CnD=D,则下列正确的是?"]
chlist = ["A: { 2, 3, 4 }  B: { 1, 3, 4 }  C: { 2, 3, 4, 5}  D: CuA U CuB",
          "A: 1个  B: 2个  C: 3个 D: 0个(傻子都不选)",
          "A: a可以是2  B: a可以是4  C:集合D是C的子集  D: 数学老师是漂亮小姐姐(掂量着来奥)"]
anlist = ["cd","c","bcd"]
qudlis = []
andlis = []
chdlis = []
mistakes = []
grade = 0  #分数
sumer = 99999  #总分
index = 0  #索引
indexs = 0
active = True
print("我一共给你们准备了3道题 总分是: " + str(sumer) + "\n")
input("找个人上来做")
input("哥们说开始咱就开始 随便按个啥咱就开")
while active:
    try:
        q = qulist.pop(index)
        a = anlist.pop(index)
        c = chlist.pop(index)
        index + 1
        indexs += 1
        print(q)
        print(c)
        usput = input('这题你决定选什么(多选就按顺序一次性把选项打齐): \n')
        if usput.lower() == a.rstrip():
            grade += 33333
            qudlis.append(q)
            andlis.append(a)
            chdlis.append(c)
        else:
            mistakes.append(indexs)
            andlis.append(a)
            chdlis.append(c)
    except IndexError:
            active = False
input("恭喜你做完了,看看你做的咋样吧\n")
if mistakes:
    print("恭喜你个屎蛋 没全对才能看到我 赶紧看看你哪道题错了! : ")
    input("你先自己预测下哪道错了")
    for mistake in mistakes:
        print('\t第'+str(mistake) + "题")
else:
    print("还挺牛逼 全部正确 恭喜你! 祝你拿到下次数学考试第一名!\n")
print("\n好了好了 题就出到这里了 这位幸运儿最后的总分是 :" + str(grade))
input("感谢你的测试  接下来是yyz time!")
input("按任意键退出")
