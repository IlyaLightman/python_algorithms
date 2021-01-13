def gcs(a, b):
    n = len(a)
    m = len(b)
    f = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                f[i][j] = f[i - 1][j - 1] + 1
            else:
                f[i][j] = max(f[i - 1][j], f[i][j - 1])
    return f[n][m]


def gcs_path(a, b):
    n = len(a)
    m = len(b)
    f = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                f[i][j] = f[i - 1][j - 1] + 1
            else:
                f[i][j] = max(f[i - 1][j], f[i][j - 1])
    ans = ''
    i = n
    j = m
    while f[i][j] > 0:
        if f[i][j] == f[i - 1][j]:
            i -= 1
        elif f[i][j] == f[i][j - 1]:
            j -= 1
        else:
            ans = a[i - 1] + ans
            i -= 1
            j -= 1
    return ans


print(gcs('baccbca', 'abcabaac'))
print(gcs_path('baccbca', 'abcabaac'))


def levenstein(a, b):
    n = len(a)
    m = len(b)
    f = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                f[i][j] = f[i - 1][j - 1]
            else:
                f[i][j] = min(f[i - 1][j - 1] + 1, f[i - 1][j] + 1, f[i][j - 1] + 1)
    return f[n][m]


print(levenstein('задач', 'здаача'))
