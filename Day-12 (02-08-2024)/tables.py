start = 2
end = 39
count = 0;

def padL(n, l):
    r = str(n)
    for i in range(len(r), l):
        r = " "+r
    return r

for i in range(start, end, 5):
    for j in range(1, 11):
        for k in range(i, i+5):
            if k>end:
                break
            print(padL(k,2), "x", padL(j,2), "=", padL((i*j),3), end="    ")

        print()
    print()
print()
