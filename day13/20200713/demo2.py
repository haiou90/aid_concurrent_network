import multiprocessing

a = 1

def fun():
    print('这是让那个进程执行的功能')
    global a
    a = 10

p = multiprocessing.Process(target = fun,args=(),kwargs={})
p.start()

p.join()
print(a)