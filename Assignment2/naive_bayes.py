#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: naive_bayes.py
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: 1 hour
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

#reading the training data in a csv file
#--> add your Python code here
training = []
with open('weather_training.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         training.append (row)

#transform the original training features to numbers and add them to the 4D array X.
#For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
X = training
for i in range(len(training)):
    for j in range(len(training[0])):
        if training[i][j] == "Sunny":
            training[i][j] = float(1)
        elif training[i][j] == "Overcast":
            training[i][j] = float(2)
        elif training[i][j] == "Rain":
            training[i][j] = float(3)
        elif training[i][j] == "Mild":
            training[i][j] = float(1)
        elif training[i][j] == "Hot":
            training[i][j] = float(2)
        elif training[i][j] == "Cool":
            training[i][j] = float(3)
        elif training[i][j] == "High":
            training[i][j] = float(2)
        elif training[i][j] == "Normal":
            training[i][j] = float(1)
        elif training[i][j] == "Strong":
            training[i][j] = float(2)
        elif training[i][j] == "Weak":
            training[i][j] = float(1)
            

#transform the original training classes to numbers and add them to the vector Y.
#For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
Y = []
for k in range(len(training)):
    Y.append(training[k][5])
    if Y[k] == "Yes":
        Y[k] = float(1)
    else:
        Y[k] = float(2)

for v in range(len(X)):
        X[v].pop(0)
        X[v].pop(4)

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the test data in a csv file
#--> add your Python code here
test = []
with open('weather_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            test.append(row)
print(test)
for i in range(len(test)):
    for j in range(len(test[0])):
        if test[i][j] == "Sunny":
            test[i][j] = float(1)
        elif test[i][j] == "Overcast":
            test[i][j] = float(2)
        elif test[i][j] == "Rain":
            test[i][j] = float(3)
        elif test[i][j] == "Mild":
            test[i][j] = float(1)
        elif test[i][j] == "Hot":
            test[i][j] = float(2)
        elif test[i][j] == "Cool":
            test[i][j] = float(3)
        elif test[i][j] == "High":
            test[i][j] = float(2)
        elif test[i][j] == "Normal":
            test[i][j] = float(1)
        elif test[i][j] == "Strong":
            test[i][j] = float(2)
        elif test[i][j] == "Weak":
            test[i][j] = float(1)

#printing the header os the solution
#--> add your Python code here
#use your test samples to make probabilistic predictions. For instance: clf.predict_proba([[3, 1, 2, 1]])[0]
#--> add your Python code here
yesNoColumn = ["PlayTennis"]
confidenceColumn = ["Confidence C"]
print(test)
for p in range(len(test)):
    print(test[p].pop(0))
    test[p].pop(4)
    print(test[p])
    playTennis = clf.predict_proba([test[p]])[0]
    print(playTennis)

    if playTennis[0] > playTennis[1]:
        yesNoColumn.append("Yes")
        if playTennis[0] >= .75:
            confidenceColumn.append(playTennis[0])
        else:
            confidenceColumn.append("")
    else:
        yesNoColumn.append("No")
        if playTennis[1] >= .75:
            confidenceColumn.append(playTennis[1])
        else:
            confidenceColumn.append("")

newFile = []
with open('weather_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            newFile.append(row)
X = newFile
for v in range(len(X)):
    X[v].pop(5)
for i in range(len(yesNoColumn)-1):
    X[i].append(yesNoColumn[i])
    X[i].append(confidenceColumn[i])
    print(X)

with open("weather_test_solution.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(X)