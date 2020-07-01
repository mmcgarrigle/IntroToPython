file = open("teams.txt", "w")
for n in range(1):
    Teams = "Liverpool" + "\n" + "Manchester City" + "\n" + "Chelsea" + "\n" + "Manchester United" + "\n" + "Spurs"
    file.write(Teams)

file = open("teams.txt", "r")
print("1st: " + file.readline())
file.readline()
file.readline()
print("4th: " + file.readline())

file.close()