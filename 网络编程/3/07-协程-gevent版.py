import gevent


def f(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        #模拟睡眠时间，当一个协程不执行的时候，就会把执行权交给下一个协程（耗时操作）
        gevent.sleep(1)

if __name__ == '__main__':
    #创建3个协程
    g1 = gevent.spawn(f, 5)
    g2 = gevent.spawn(f, 5)
    g3 = gevent.spawn(f, 5)

    g1.join()
    g2.join()
    g3.join()