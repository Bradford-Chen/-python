# 例题2：
# def my_day():
#     print('早上起床')
#     print('吃早餐')
#     print('看电视')
#     print('吃午餐')
#     print('午睡')
#     print('吃晚餐')
#     print('玩游戏')
#     print('睡觉')
#     print('快乐的一天结束')
#     return '快乐的一天'
#
#
# ret = my_day()
# print(ret)


# 　只要函数执行到return 函数就会停止执行
# 1. 如果函数不写return，默认返回None
# 2. 也可以只写一个return，也是返回None，停止函数的执行
# 3. return 一个返回值，你在调用方能接受到一个返回值
# 4. return 多个返回值，多个值需要用,隔开，接收的是元组


# 例题2：多值返回
def my_day():
    print('早上起床')
    print('吃早餐')
    print('看电视')
    print('吃午餐')
    print('午睡')
    print('吃晚餐')
    print('玩游戏')
    print('睡觉')
    print('快乐的一天结束')
    return '看电视', '玩游戏', '睡觉'

# ret = my_day()
# print(ret)

# a, b, c = my_day()
# print(a)
# print(b)
# print(c)