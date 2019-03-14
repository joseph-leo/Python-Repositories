"""
fileInput = open('poem.txt', 'r')
for line in fileInput:
    print(line, end='')
fileInput.close()
"""


"""
with open('poem.txt', 'r') as fileInput:
    for line in fileInput:
        print(line, end='')
"""


"""
fileInput = open('poem.txt', 'r')
fileOutput = open('output.txt', 'w')
for line in fileInput.readlines():
    fileOutput.write(line)
fileInput.close()
fileOutput.close()
"""


"""
with open('poem.txt', 'r') as inputFile, open('output.txt', 'w') as outputFile:
    for line in inputFile.readlines():
        outputFile.write(line)
"""


"""
with open('output.txt', 'a') as file:
    line = '\nA little something extra'
    file.write(line)
"""
