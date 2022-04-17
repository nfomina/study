n = int(input())

ips = []
for _ in range(n):
    ips.append(list(map(int, input().split('.'))))

for ip in sorted(ips):
    print('.'.join([str(int) for int in ip]))
