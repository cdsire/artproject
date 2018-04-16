# coding:utf-8
'''
   ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
'''
mlist = []
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i != j and i != k and j !=k:
                print(i*100+j*10+k)
                mlist.append(i*100+j*10+k)
print(len(mlist))

# print("%s is a good boy." % ("he","she"))

f = 'hello {0} i am {1}'.format
print(f('Kevin','Tom'))

print('hello {0:>{1}} '.format('Kevin',50))
