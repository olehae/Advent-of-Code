monkey0 = [63, 84, 80, 83, 84, 53, 88, 72]
monkey1 = [67, 56, 92, 88, 84]
monkey2 = [52]
monkey3 = [59, 53, 60, 92, 69, 72]
monkey4 = [61, 52, 55, 61]
monkey5 = [79, 53]
monkey6 = [59, 86, 67, 95, 92, 77, 91]
monkey7 = [58, 83, 89]

modulo_trick = 13*11*2*5*7*3*19*17


def monkey_0():
    counter = 0
    while monkey0:
        new = monkey0[0] * 11
        new = new % modulo_trick
        if new % 13 == 0:
            monkey4.append(new)
        else:
            monkey7.append(new)
        monkey0.pop(0)
        counter += 1
    return counter


def monkey_1():
    counter = 0
    while monkey1:
        new = monkey1[0] + 4
        new = new % modulo_trick
        if new % 11 == 0:
            monkey5.append(new)
        else:
            monkey3.append(new)
        monkey1.pop(0)
        counter += 1
    return counter


def monkey_2():
    counter = 0
    while monkey2:
        new = monkey2[0] ** 2
        new = new % modulo_trick
        if new % 2 == 0:
            monkey3.append(new)
        else:
            monkey1.append(new)
        monkey2.pop(0)
        counter += 1
    return counter


def monkey_3():
    counter = 0
    while monkey3:
        new = monkey3[0] + 2
        new = new % modulo_trick
        if new % 5 == 0:
            monkey5.append(new)
        else:
            monkey6.append(new)
        monkey3.pop(0)
        counter += 1
    return counter


def monkey_4():
    counter = 0
    while monkey4:
        new = monkey4[0] + 3
        new = new % modulo_trick
        if new % 7 == 0:
            monkey7.append(new)
        else:
            monkey2.append(new)
        monkey4.pop(0)
        counter += 1
    return counter


def monkey_5():
    counter = 0
    while monkey5:
        new = monkey5[0] + 1
        new = new % modulo_trick
        if new % 3 == 0:
            monkey0.append(new)
        else:
            monkey6.append(new)
        monkey5.pop(0)
        counter += 1
    return counter


def monkey_6():
    counter = 0
    while monkey6:
        new = monkey6[0] + 5
        new = new % modulo_trick
        if new % 19 == 0:
            monkey4.append(new)
        else:
            monkey0.append(new)
        monkey6.pop(0)
        counter += 1
    return counter


def monkey_7():
    counter = 0
    while monkey7:
        new = monkey7[0] * 19
        new = new % modulo_trick
        if new % 17 == 0:
            monkey2.append(new)
        else:
            monkey1.append(new)
        monkey7.pop(0)
        counter += 1
    return counter


summen = [0, 0, 0, 0, 0, 0, 0, 0]

for i in range(10000):
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
