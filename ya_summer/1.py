from datetime import timedelta

if __name__ == '__main__':
    n = int(input())
    times_s = []
    for i in range(n):
        times_s.append(input())

    hh, mm, ss = [0] * n, [0] * n, [0] * n
    times = []
    for i in range(n):
        hh[i], mm[i], ss[i] = times_s[i].split(":")
        hh[i], mm[i], ss[i] = int(hh[i]), int(mm[i]), int(ss[i])
        times.append(timedelta(hours=hh[i], minutes=mm[i], seconds=ss[i]))

    count = 1
    for i in range(1, n):
        if times[i] <= times[i - 1]:
            count += 1
    print(count)
