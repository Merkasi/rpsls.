"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：杨敬升
日期：2020/11/15
"""
import random
def name_to_number(name):
    if name=='石头' :
        name=0
    if name=='史波克' :
        name=1
    if name=='纸' :
        name=2
    if name=='蜥蜴' :
        name=3
    if name=='剪刀' :
        name=4
    return name
def number_to_name(number):
    if number==0 :
        number='石头'
    if number==1 :
        number='史波克'
    if number==2 :
        number='纸'
    if number==3 :
        number='蜥蜴'
    if number==4 :
        number='剪刀'
    return number
def rpsls(player_choice):
    y=random.randrange(0,4)
    player_choice=choice_name
    player_choice_number=name_to_number(player_choice)
    while player_choice_number==name_to_number('石头') :
         print('您出的是'+number_to_name(0)+'，'+'计算机出的是'+number_to_name(y))
         if y==3 or y==4 :
             print('您赢了')
         if player_choice_number == y:
             print('您和计算机出的一样呢')
         if y==1 or y==2 :
             print('计算机赢了')
         break
    while player_choice_number==name_to_number('史波克') :
        print('您出的是' + number_to_name(1) +'，'+ '计算机出的是' + number_to_name(y))
        if y==4 or y==0 :
            print('您赢了')
        if player_choice_number==y :
            print('您和计算机出的一样呢')
        if y== 2 or y==3 :
            print('计算机赢了')
        break
    while player_choice_number==name_to_number('纸') :
        print('您出的是' + number_to_name(2) +'，'+ '计算机出的是' + number_to_name(y))
        if y==1 or y==0 :
            print('您赢了')
        if player_choice_number==y :
            print('您和计算机出的一样呢')
        if y==3 or y==4 :
            print('计算机赢了')
        break
    while player_choice_number==name_to_number('蜥蜴') :
        print('您出的是' + number_to_name(3) +'，'+ '计算机出的是' + number_to_name(y))
        if y==1 or y==2 :
            print('您赢了')
        if player_choice_number==y :
            print('您和计算机出的一样呢')
        if y==0 or y==4 :
            print('计算机赢了')
        break
    while player_choice_number==name_to_number('剪刀') :
        print('您出的是' + number_to_name(4) +'，'+ '计算机出的是' + number_to_name(y))
        if y==2 or y==3 :
            print('您赢了')
        if player_choice_number==y :
            print('您和计算机出的一样呢')
        if y==0 or y==1 :
            print('计算机赢了')
        break
    return player_choice_number
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
if choice_name != '石头' and choice_name !='剪刀' and choice_name !='纸' and choice_name !='蜥蜴' and choice_name !='史波克' :
    print('Error: No Correct Name')

rpsls(choice_name)