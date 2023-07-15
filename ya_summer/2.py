if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s1, s2 = input(), input()
        p1, p2 = [], []
        letters1, letters2 = {}, {}
        counter1, counter2 = 0, 0
        for c1, c2 in zip(s1, s2):
            if letters1.get(c1) is None:
                letters1[c1] = [counter1]
            else:
                letters1[c1].append(counter1)
            counter1 += 1
            if letters2.get(c2) is None:
                letters2[c2] = [counter2]
            else:
                letters2[c2].append(counter2)
            counter2 += 1
        p1.append(list(letters1.values()))
        p2.append(list(letters2.values()))
        if p1.__eq__(p2):
            print('YES')
        else:
            print('NO')
