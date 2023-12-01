monkey0 = [89, 73, 66, 57, 64, 80]
monkey1 = [83, 78, 81, 55, 81, 59, 69]
monkey2 = [76, 91, 58, 85]
monkey3 = [71, 72, 74, 76, 68]
monkey4 = [98, 85, 84]
monkey5 = [78]
monkey6 = [86, 70, 60, 88, 88, 78, 74, 83]
monkey7 = [81, 58]


def monkey_0():
    counter = 0
    while monkey0:
        new = monkey0[0] * 3
        new = new // 3
        if new % 13 == 0:
            monkey6.append(new)
        else:
            monkey2.append(new)
        monkey0.pop(0)
        counter += 1
    return counter


def monkey_1():
    counter = 0
    while monkey1:
        new = monkey1[0] + 1
        new = new // 3
        if new % 3 == 0:
            monkey7.append(new)
        else:
            monkey4.append(new)
        monkey1.pop(0)
        counter += 1
    return counter


def monkey_2():
    counter = 0
    while monkey2:
        new = monkey2[0] * 13
        new = new // 3
        if new % 7 == 0:
            monkey1.append(new)
        else:
            monkey4.append(new)
        monkey2.pop(0)
        counter += 1
    return counter


def monkey_3():
    counter = 0
    while monkey3:
        new = monkey3[0] ** 2
        new = new // 3
        if new % 2 == 0:
            monkey6.append(new)
        else:
            monkey0.append(new)
        monkey3.pop(0)
        counter += 1
    return counter


def monkey_4():
    counter = 0
    while monkey4:
        new = monkey4[0] + 7
        new = new // 3
        if new % 19 == 0:
            monkey5.append(new)
        else:
            monkey7.append(new)
        monkey4.pop(0)
        counter += 1
    return counter


def monkey_5():
    counter = 0
    while monkey5:
        new = monkey5[0] + 8
        new = new // 3
        if new % 5 == 0:
            monkey3.append(new)
        else:
            monkey0.append(new)
        monkey5.pop(0)
        counter += 1
    return counter


def monkey_6():
    counter = 0
    while monkey6:
        new = monkey6[0] + 4
        new = new // 3
        if new % 11 == 0:
            monkey1.append(new)
        else:
            monkey2.append(new)
        monkey6.pop(0)
        counter += 1
    return counter


def monkey_7():
    counter = 0
    while monkey7:
        new = monkey7[0] + 5
        new = new // 3
        if new % 17 == 0:
            monkey3.append(new)
        else:
            monkey5.append(new)
        monkey7.pop(0)
        counter += 1
    return counter


summen = [0, 0, 0, 0, 0, 0, 0, 0]

for i in range(20):
    summen[0] += monkey_0()
    summen[1] += monkey_1()
    summen[2] += monkey_2()
    summen[3] += monkey_3()
    summen[4] += monkey_4()
    summen[5] += monkey_5()
    summen[6] += monkey_6()
    summen[7] += monkey_7()

print(summen)
summen.sort()

print(summen[-1] * summen[-2])