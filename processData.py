import datetime
import creds

def convertDate(line):
    date = line.split(" ")[2]
    date = date.strip("\n")
    date = datetime.datetime.strptime(date, "%d.%m.%Y").strftime("%Y-%m-%d")
    print(date)
    return date

def convertTeachers(line):
    teacherScore = list()
    line = line.replace("\n", "")
    line = line.replace(",", "")
    itemList = line.split(" ")
    teacherList = itemList[2:]
    for teacher in teacherList:
        if teacher.find("(") != -1:
            indexOfTeacher = teacherList.index(teacher)
            teacher = teacher.split("(")[1]
            teacher = teacher.replace(")", "")
            score = (eval(teacher) * -0.1 ) + 0.1
            teacherScore.append(score)
            teacherList[indexOfTeacher] = teacherList[indexOfTeacher].replace("(" + str(teacher) + ")", "")
        else:
            teacherScore.append(1)
    print(line)
    return teacherList, teacherScore

def pushIntoDatabase(date, teacherList, teacherScore):
    print()
    #TODO: add server connection


line = ""
with open("infosOfTheDay.txt") as f:
    line = f.readline()
    if "" != line:
        date = convertDate(line)
    line = f.readline()
    if "" != line:
        teacherList, teacherScore = convertTeachers(line)
print(teacherList, teacherScore)
with open("infosOfTomorrow.txt") as f:
    line = f.readline()
    if "" != line:
        date = convertDate(line)
    line = f.readline()
    if "" != line:
        teacherList, teacherScore = convertTeachers(line)
print(teacherList, teacherScore)

