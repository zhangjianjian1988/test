# isalpha() 是否是字母  isdigit() 是否是数字

s = 'abcd1234'
result = s.isalpha()
print(result)

s = '888999'
result = s.isdigit()
print(result)



sum = 0
i = 1

while i <= 3:
    num = input('请输入数字：')
    if num.isdigit():
        num = int(num)
        sum += num
        print('第{}个数字累加成功！'.format(i))
        i += 1
    else:
        print('不是数字。。。')
print('sum=',sum)


# join  将abc用-连接构成一个新的字符串   可以指定符号的拼接  比 + 内容丰富

new_str = '-'.join('abc')

print(new_str)

# python 列表 list = ['a','b','c']  类似于数组

list1 = ['a','b','c']
print(list1)
result = ''.join(list1)
print(result)


s = '   hello   ' # strip  去掉字符串（截取字符串）
s = s.lstrip()
print(s+'8')

s = s.rstrip()
print(s+'8')

# split  分割字符串 将分割后的字符串保存在列表中

s = 'hello world hello kitty'

result = s.split(' ',2) # 表示按照空格作为分隔符， 分割字符串2次
print(result)


n = s.count(' ')  #count(args) 求字符串中指定args的个数  
print('个数',n)   

# 求s中有几个s
# s = 'dsfsgssfawdewqds'
# n = s.count('s')
# print(n)
# 添加一行做个测试
