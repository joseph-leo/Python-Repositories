myInputFile = open('hello.txt', 'r')
print('Line 0 (first line):', myInputFile.readline())

myInputFile.seek(0)
print('Line 0 again:', myInputFile.readline())
print('Line 1:', myInputFile.readline())

myInputFile.seek(8)
print('Line 0 (starting at 9th character):', myInputFile.readline())

myInputFile.seek(10, 0)
print('Line 1 (starting at 11th character):', myInputFile.readline())

myInputFile.close()
      
