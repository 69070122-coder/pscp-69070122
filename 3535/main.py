'''main'''
data = {}

while True:
    student_id = input()
    if student_id == "END":
        break

    year = student_id[:2]
    faculty = int(student_id[2:4])

    if year not in data:
        data[year] = {}
    if faculty not in data[year]:
        data[year][faculty] = 0

    data[year][faculty] += 1

for year in sorted(data, reverse=True):
    faculties = sorted(data[year])

    for i, faculty in enumerate(faculties):
        if i == 0:
            print(year, faculty, data[year][faculty])
        else:
            print("--", faculty, data[year][faculty])
