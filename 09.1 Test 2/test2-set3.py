
total = 0
pts = 5
print('TEST 2')
print('-------------')


try:
    from F1 import f1
    assert f1(["sun","moon","sand"],"n") == 3
    assert f1(["book","moon","poetry","footbal"],"o") == 7
    total += pts
    print('F1:', pts, 'pts')
except:
    print('F1:', 0, 'pts')


try:
    from F2 import f2
    assert f2([10,20,38],[14,9,10,31,20]) == "**"
    assert f2([8,5,5,4,6],[3,2,5,7,4,1,4,6]) == "****"
    total += pts
    print('F2:', pts, 'pts')
except:
    print('F2:', 0, 'pts')


try:
    from F3 import f3
    assert f3("450+3=453") == True
    assert f3("4+2229=2233") == True
    assert f3("5000+801=5802") == False
    total += pts
    print('F3:', pts, 'pts')
except:
    print('F3:', 0, 'pts')


try:
    from F4 import f4
    assert f4([{"name":"Peter","age":30},{"name":"Ann","age":22},{"name":"Mark","age":28}],25) == 2
    assert f4([{"name":"Peter","age":16},{"name":"Ann","age":18}],17) == 1
    total += pts
    print('F4:', pts, 'pts')
except:
    print('F4:', 0, 'pts')


try:
    from F5 import f5
    assert f5("s",3) == True
    assert f5("o",22) == True
    assert f5("1",11) == False
    assert f5("A",30) == False
    total += pts
    print('F5:', pts, 'pts')
except:
    print('F5:', 0, 'pts')


try:
    from F6 import f6
    assert f6("Poland",2) == 33
    assert f6("Germany",1) == 4
    total += pts
    print('F6:', pts, 'pts')
except:
    print('F6:', 0, 'pts')




print('TOTAL:', total, 'pts')

