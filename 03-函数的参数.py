# 例题1：
# def my_day(tv, sleep1, game, sleep2):  # 形参
#     print('早上起床')
#     print('吃早餐')
#     print('看电视{}'.format(str(tv) + '小时'))
#     print('吃午餐')
#     print('午睡{}'.format(str(sleep1) + '小时'))
#     print('吃晚餐')
#     print('玩游戏{}'.format(str(game) + '小时'))
#     print('睡觉{}'.format(str(sleep2) + '小时'))
#     print('快乐的一天结束')


# my_day(3, 1, 2, 8)  # 实参

# 例题2：
# 关键字参数
# my_day(tv=3, sleep1=1, game=2, sleep2=8)
# my_day(game=2, sleep2=8, tv=3, sleep1=1)

# 例题3：
# 位置参数和关键字参数混合使用
# my_day(3, 1, game=2, sleep2=8)

# 例题4：
def my_day(tv, sleep1, game, sleep2=8):  # 形参
    print('早上起床')
    print('吃早餐')
    print('看电视{}'.format(str(tv) + '小时'))
    print('吃午餐')
    print('午睡{}'.format(str(sleep1) + '小时'))
    print('吃晚餐')
    print('玩游戏{}'.format(str(game) + '小时'))
    print('睡觉{}'.format(str(sleep2) + '小时'))
    print('快乐的一天结束')

my_day(3, 1, 2)
my_day(3, 1, game=2, sleep2=10)

# 参数:　在函数执行的时候给函数传递的信息
# 形参:　在函数声明的位置，声明出来变量
# 实参:　在函数调用的时候，实际你给函数传递的值　
# 函数的参数个数是没有要求，但是在运行的时候，形参和实参要匹配，按照位置把实参赋值给形参
# 参数的分类:
#   站在实参的角度:
#       1. 位置参数
#       2. 关键字参数
#       3. 混合参数，注意顺序：先写位置参数，然后写关键字参数，否则会报错
#   站在形参的角度:
#       1. 位置参数
#       2. 默认值参数
#       3. 默认值参数和位置参数混合使用，顺序: 先写位置参数，然后在写默认值参数
