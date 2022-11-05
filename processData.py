import datetime
import creds

def convertDate(line):
    date = line.split(" ")[1]
    date = date.strip("\n")
    date = datetime.datetime.strptime(date, "%d.%m.%Y").strftime("%Y-%m-%d")
    print(date)
    return date

line = ""
with open("infosOfTheDay.txt") as f:
    for line in f:
        print(line)


with open("infosOfTomorrow.txt") as f:
    line = f.readline()
    if "" != line:
        date = convertDate()
    line = f.readline()