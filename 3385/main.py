'''main'''
p = int(input())
n = int(input())

bus = []
answer = 0

for i in range(n):
    data = input().split()
    stop = int(data[0])
    # ให้คนที่ถึงป้ายนี้ลงจากรถ
    new_bus = []

    for destination in bus:
        if destination != stop:
            new_bus.append(destination)

    bus = new_bus

    # ให้ผู้โดยสารขึ้นตามลำดับคิว
    for j in range(1, len(data)):
        destination = int(data[j])
        if destination > stop and len(bus) < p:
            bus.append(destination)
            answer += 1
print(answer)
