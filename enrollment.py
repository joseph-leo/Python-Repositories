universities = [
    ['Cal Tech', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['MIT', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(colleges):
    students = []
    tuition = []
    for i in range(len(colleges)):
        students.append(colleges[i][1])
        tuition.append(colleges[i][2])
    return students, tuition
                    
def mean(stats):
    total = 0
    for i in range(len(stats)):
        total += stats[i]
    total = total / len(stats)
    return int(total)
        
def median(stats):
    sortedList = sorted(stats)
    for i in range(len(stats)):
        if i % 2 != 0:
            listMedian = sortedList[int(len(stats) / 2)] + sortedList[int(len(stats) / 2)] / 2 
            return listMedian
        else:
            average = sortedList[int(len(stats) / 2)]
            return average
            
        
        

def totals(colleges):
    totalStudents = 0
    totalTuition = 0
    for i in range(len(colleges)):
        totalStudents += colleges[i][1]
        totalTuition += colleges[i][2]
    return totalStudents, totalTuition

stats = enrollment_stats(universities)

studMean = mean(stats[0])
studMedian = median(stats[0])

tuitionMean = mean(stats[1])
tuitionMedian = median(stats[1])

totals = totals(universities)
studTotal = totals[0]
tuitionTotal = totals[1]

print("""
Total students:  {}
Total tuition: {}

Student mean: {}
Student median: {}

Tuition mean: {}
Tuition median: {}
""".format(studTotal, tuitionTotal, studMean, studMedian, tuitionMean, tuitionMedian))



            
