#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []

    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)

    #transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
    # so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here
    #transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> add your Python code here
    # Y =
    X = dbTraining
    for i in range(len(dbTraining)):
        for j in range(len(dbTraining[0])):
            if j == 4:
                Y.append(dbTraining[i][j])   
            elif dbTraining[i][j] == "Young":
                X[i][j] = 1
            elif dbTraining[i][j] == "Prepresbyopic":
                X[i][j] = 2
            elif dbTraining[i][j] == "Presbyopic":
                X[i][j] = 3
            elif dbTraining[i][j] == "Myope":
                X[i][j] = 1
            elif dbTraining[i][j] == "Hypermetrope":
                X[i][j] = 2
            elif dbTraining[i][j] == "Yes":
                X[i][j] = 1
            elif dbTraining[i][j] == "No":
                X[i][j] = 2
            elif dbTraining[i][j] == "Normal":
                X[i][j] = 1
            elif dbTraining[i][j] == "Reduced":
                X[i][j] = 2
    
    for i in range(len(X)):
        X[i].pop(4)
    #loop your training and test tasks 10 times here
    for trial in range (10):
        global total
        total = 0
        #fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
        clf = clf.fit(X, Y)

        #read the test data and add this data to dbTest
        #--> add your Python code here
        dbTest = []
        with open('contact_lens_test.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i > 0: #skipping the header
                    dbTest.append (row)
        
        for i in range(len(dbTest)):
            for j in range(len(dbTest[0])-1):
                if dbTest[i][j] == "Young":
                    dbTest[i][j] = 1
                elif dbTest[i][j] == "Prepresbyopic":
                    dbTest[i][j] = 2
                elif dbTest[i][j] == "Presbyopic":
                    dbTest[i][j] = 3
                elif dbTest[i][j] == "Myope":
                    dbTest[i][j] = 1
                elif dbTest[i][j] == "Hypermetrope":
                    dbTest[i][j] = 2
                elif dbTest[i][j] == "Yes":
                    dbTest[i][j] = 1
                elif dbTest[i][j] == "No":
                    dbTest[i][j] = 2
                elif dbTest[i][j] == "Normal":
                    dbTest[i][j] = 1
                elif dbTest[i][j] == "Reduced":
                    dbTest[i][j] = 2

        numerator = 0
        denominator = 0
        for data in dbTest:
            #transform the features of the test instances to numbers following the same strategy done during training,
            #and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
            #where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
            #--> add your Python code here
            actualValue = data.pop(4)
            class_predicted = clf.predict([data])[0]
            #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
            #--> add your Python code here
            if actualValue == class_predicted:
                numerator += 1
            denominator += 1
            accuracy = numerator/denominator
            total += accuracy

    #find the average of this model during the 10 runs (training and test set)
    #--> add your Python code here
    average = total/10

    #print the average accuracy of this model during the 10 runs (training and test set).
    #your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    #--> add your Python code here
    print("final accuracy when training on" + ds + ": ")
    print(average)
    average = 0


