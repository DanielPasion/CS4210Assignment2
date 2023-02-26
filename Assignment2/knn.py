#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []

#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
global wrong
wrong = 0
#loop your data to allow each instance to be your test set
for i in range(len(db)):

    #add the training features to the 2D array X removing the instance that will be used for testing in this iteration. For instance, X = [[1, 3], [2, 1,], ...]]. Convert each feature value to
    # float to avoid warning messages
    #--> add your Python code here
    db = []
    p = 0
    with open('binary_points.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for p, row in enumerate(reader):
            if p> 0: #skipping the header
                db.append (row)
    actual = (db[i][2])
    if actual == "-":
        actual = float(2)
    else:
        actual = float(1)
    testSample = [float(db[i][0]),float(db[i][1])]

    db = []
    p = 0
    with open('binary_points.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for p, row in enumerate(reader):
            if p> 0: #skipping the header
                db.append (row)
                
    X = []
    for item in db:
        X.append(item)
    for colm in range(len(db)):
        for row in range(len(db[0])-1):
            if colm != i:
                X[colm][row] = float(db[colm][row])
    #transform the original training classes to numbers and add to the vector Y removing the instance that will be used for testing in this iteration. For instance, Y = [1, 2, ,...]. Convert each
    #  feature value to float to avoid warning messages
    #--> add your Python code here
    #1 is pos, 2 is neg
    Y =[]
    for r in range(len(db)):
        if r != i:
            if db[r][2] == "+":
                Y.append(float(1))
            else:
                Y.append(float(2))

    for v in range(len(X)):
        X[v].pop(2)
    #Y.pop(i)
    
    for colm in range(len(X)):
        for row in range(len(X[0])):
                X[colm][row] = float(X[colm][row])
    for q in range(len(Y)):
        Y[q] = float(Y[q])

    X.pop(i)
    #store the test sample of this iteration in the vector testSample
    #--> add your Python code here
    #I moved this up higher to line 29

    #fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    #use your test sample in this iteration to make the class prediction. For instance:
    class_predicted = clf.predict([testSample])[0]
    #--> add your Python code here

    #compare the prediction with the true label of the test instance to start calculating the error rate.
    #--> add your Python code here
    if int(class_predicted) != int(actual):
        wrong += 1
#print the error rate
#--> add your Python code here
errorRate = wrong/10
print("error rate:")
print(errorRate)
print()






