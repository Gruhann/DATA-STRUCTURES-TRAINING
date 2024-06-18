n = int(input())
m = []
for i in range(n):
    m.append(list(map(int, input().split())))

row, col = map(int, input().split())

def check(i, j):
    if i >= 0 and i < n and j >= 0 and j < n and m[i][j] == 1:
        m[i][j] = 2
        check(i+1, j)
        check(i-1, j)
        check(i, j+1)
        check(i, j-1)

check(row-1, col-1)
# print(m)
tree_count = 0
for i in range(n):
    for j in range(n):
        if m[i][j] == 1:
            tree_count += 1

print(m)
print(tree_count)


# op:
# 6
# 0 1 1 1 0 1
# 0 1 0 1 0 0
# 1 0 1 1 0 0
# 0 0 0 1 1 1
# 1 1 0 0 0 1
# 1 1 1 0 1 0
# # # 4
# 6




