
total = 0
print('TEST 1')
print('-------------')


try:
    pts = 3
    from F1 import f1
    assert f1(4,8,5) == True
    assert f1(2,9,2) == False
    assert f1(1,3,3) == False
    total += pts
    print('F1 ok:', pts, 'pts')
except:
    pass


try:
    pts = 4
    from F2 import f2
    x1,x2=0,0
    for i in range(1000):
        x = f2()
        assert x in ["tak","nie"]
        x1 += 1 if x=="tak" else 0
        x2 += 1 if x=="nie" else 0
    assert x1>0 and x2>0
    total += pts
    print('F2 ok:', pts, 'pts')
except:
    pass


try:
    pts = 4
    from F3 import f3
    assert f3(39126) == 21
    assert f3(27) == 9
    assert f3(8888888888) == 80
    total += pts
    print('F3 ok:', pts, 'pts')
except:
    pass


try:
    pts = 4
    from F4 import f4
    assert f4(7,4,9) == 5
    assert f4(3,2,1) == 2
    assert f4(9,8,9) == 1
    total += pts
    print('F4 ok:', pts, 'pts')
except:
    pass


try:
    pts = 4
    from F5 import f5
    assert f5(11) == "1234567891011"
    assert f5(4) == "1234"
    assert f5(7) == "1234567"
    total += pts
    print('F5 ok:', pts, 'pts')
except:
    pass


try:
    pts = 5
    from F6 import f6
    assert f6(2,8) == 15
    assert f6(3,4) == 19
    assert f6(5,5) == 41
    total += pts
    print('F6 ok:', pts, 'pts')
except:
    pass


try:
    pts = 6
    from F7 import f7
    assert f7(1) == 2
    assert f7(5) == 11
    assert f7(15) == 47
    total += pts
    print('F7 ok:', pts, 'pts')
except:
    pass


print('TOTAL:', total, 'pts')

