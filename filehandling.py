"""
f = open('essay.txt', 'r')
print(f.read())
f.close()


with open('essay.txt', 'r') as f:
    for line in f:
        print(line, end='')

with open('test.txt', 'w') as f:
    f.write("The Data Science process: \n 1) Predictive causal analysis \n 2) Prescription analysis \n"
            "3) Machine learning to make predictions ")
"""
#read a data and append a file into another file
'''with open('essay.txt', 'r') as readFile:
    for line in readFile:
        if line.startswith('points') is True:
            with open('process.txt', 'a') as appendFile:
                appendFile.write(line)'''

#access file in different path
import os

print(os.getcwd())
os.chdir('C:/Users/SR COM/PycharmProjects/pythonProject/.venv')
print(os.getcwd())

with open('points.txt', 'r') as f:
    for line in f:
        print(line, end='')

#C:\Users\SR COM\PycharmProjects\pythonProject
#C:/Users/SR COM/PycharmProjects/pythonProject/.venv
