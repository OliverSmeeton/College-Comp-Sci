import csv
highScore = 0
lowScore = 100
cumulativeMarks = 0
noCanidates = 0
topMarks = []
bottomMarks = []
with open('File Handling\Marks.csv', 'r') as csvFile:
    fileData = csv.DictReader(csvFile)
    for line in fileData:
        try:
            score = int(line['marks'])
        except:
            continue
        
        noCanidates += 1

        name = f"Name: {line['first_name']} {line['last_name']} Score: {score}"
        if score > highScore:
            topMarks = [name]
            highScore = score
        elif score < lowScore:
            bottomMarks = [name]
            lowScore = score
        elif score == highScore:
            topMarks.append(name)
        elif score == lowScore:
            bottomMarks.append(name)
        
        cumulativeMarks += score

avgMark = cumulativeMarks/noCanidates
print(f"Top Marks Goes to {topMarks} \n")
print(f"Bottom Marks Goes to {bottomMarks} \n")
print(f"Mean Marks is {avgMark}")
