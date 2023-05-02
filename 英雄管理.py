def create_hero():
  name = input("请输入英雄的名称：")
  blood = input("请输入英雄的血量：")
  power = input("请输入英雄的攻击力：")
  hero = dict(name=name, blood=blood, power=power)
  li_hero.append(hero)
  print("创建成功")
def query_hero():
  name1 = input("请输入需要查询的英雄信息: ")
  ff = False
  for j in li_hero:

    if name1 == j.get('name'):
      ff = True
      print("英雄 %s 的信息为" % name1)
      print(j)
  if ff == False:
    print("没有英雄 %s 的信息" % name1)
def update_hero():
  name3 = input("请问你要修改哪个英雄的血量 ")
  ff = False
  for j in li_hero:

    if name3 == j.get('name'):
      li_hero.pop(li_hero.index(j))
      blood1 = input("请问你要将血量修改为多少？ ")
      j['blood'] = blood1;
      li_hero.append(j)
      ff = True
      print("更新之后的结果为")
      print(li_hero)
      break
  if ff == False:
    print("更新之后的结果为没有找到。")
def delete_hero():
  name2 = input("请问你要删除哪个英雄？ ")
  ff = False
  for j in li_hero:
    if name2 == j.get('name'):
      li_hero.remove(j)
      ff = True
      print("删除之后所有的英雄的数据信息为 ")
      print(li_hero)
  if ff == False:
    print("更新之后的结果为没有找到。")
Str_1="1. **创建英雄** 当前游戏中，创建英雄角色，定义好对应英雄的血量及其攻击力。"
Str_2="2. **查看英雄信息** 查看当前游戏中所有的英雄信息。"
Str_3="3. **修改英雄信息** 修改英雄的血量。"
Str_4="4. **删除英雄** 英雄太弱，不需要，删除掉。"
Str_5="5. **退出系统** 结束程序。"
print(Str_1+"\n"+Str_2+"\n"+Str_3+"\n"+Str_4+"\n"+Str_5)

li_input = ["1","2","3","4","5"]
li_hero=[]
i="1"


while i in li_input:
  i = input("请输入数字，选择需要完成的操作：")
  if i == "1":
    create_hero()
    continue
  if i == "2":
    query_hero()
    continue
  if i == "3":
    update_hero()
    continue
  if i == "4":
    delete_hero()
    continue
  if i == "5":
    break
print("退出系统")