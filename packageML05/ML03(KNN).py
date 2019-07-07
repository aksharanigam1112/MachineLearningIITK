import numpy as np
from operator import itemgetter
import csv , os

class KNNClassifier(object):

    def __init__(self):
        self.training_features = None       # value of kicks,kisses
        self.training_labels = None         # movie genre ['Romance' ,'Action' ]
        self.test_features = None           # ques data to find the genre kicks =18 kisses = 90
        self.elegantResult = "Most likely ,{0} , '{1}' is of type '{2}'"

    def loadTrainingDataFromFile(self,file_path):

        # User has given a name & does the file with that name exists ?
        if file_path is not None and os.path.exists(file_path):

            tr_features = []
            self.training_labels =[]

            with open(file_path,"r") as training_data_file:

                #It reads the entire data except the 1st row ( considering it to be the meta-data)
                reader = csv.DictReader(training_data_file)

                for row in reader:

                    if(row['moviename']!='?'):

                        tr_features.append( [ float (row['kicks']) , float(row['kisses']) ])
                        self.training_labels.append(row['movietype'])

                    else:
                        self.test_features = np.array( [float(row['kicks']) , float(row['kisses']) ])

            if (len(tr_features)>0) :
                self.training_features = np.array(tr_features)

            print("self.training_features = \n",self.training_features)
            print("self.training_labels = \n",self.training_labels)
            print("self.test_features = \n",self.test_features)


    def classifyTestData(self , test_data=None , k=0):

        print("\nClassify_test_data : test_data : ",test_data)

        if(test_data is not None):      # When we give external value
            self.test_features = np.array(test_data , dtype=float)

        print("\nClassify test data : self.test_features : ",self.test_features)

        #Ensure we have training data , tarining labels , test data and k
        if self.test_features is not None and self.training_features is not None and self.training_labels is not None and k>0 :

            print("\nclassifyTestData says self.test_features : ",self.test_features)
            print("self.training_features : \n",self.training_features)     # Multivariate
            print("self.training_labels : \n",self.training_labels)

            featureVectorSize = self.training_features.shape[0]         # Rows = 6  (6,2)

            print("\nfeatureVectorSize",featureVectorSize)

            tileOfTestData = np.tile(self.test_features , (featureVectorSize,1))
            # [18,90] (test_features) ko 6 times repeat karna hai to make 1 col

            print("After tileOfTestData : \n",tileOfTestData)

            diffMat  = self.training_features -  tileOfTestData
            print("\ndiffMat : ",diffMat)

            sqDiffMat = diffMat**2
            print("sqDiffMat :\n",sqDiffMat)
            sqDistances = sqDiffMat.sum(axis=1)   # (x2 - x1)^2 + (y2 - y1)^2 to to this row wise we supply axis=1
            print("\nRow wise sum sqDistances : ",sqDistances)

            distance = sqDistances ** 0.5
            print("\ndistance (sq root of sqDistances) : ",distance)

            sortedDistanceIndex = distance.argsort()
            print("sortedDistanceIndex : \n",sortedDistanceIndex)
            print("\nself.training_labels : ",self.training_labels)

            classCount = {}

            for i in range(k):
                print("\nsortedDistanceIndex[i] : ",sortedDistanceIndex[i])
                voteIlabel = self.training_labels[sortedDistanceIndex[i]]
                print("voteIlabel : ",voteIlabel)
                classCount[voteIlabel] = classCount.get(voteIlabel,0)+1  #Incrementing the value of the labels

            print("classCount = ",classCount)
            sortedClassCount = sorted(classCount.items() , key=itemgetter(1) , reverse = True)
            # classCount.items() converts the dict to tuple of tuples, where inner tuple is a set of (key , value)
            # ( ("Roamnce" , 3) , ("Action" , 2) )

            print("\nsortedClassCount = ",sortedClassCount)
            print("\nsortedClassCount[0] = ",sortedClassCount[0])
            print("\nsortedClassCount[0][0] = ",sortedClassCount[0][0])
            return sortedClassCount[0][0]

        else:
            return "Can't Determine result for empty test-data."

def predictMovieType():

    instance = KNNClassifier()
    instance.loadTrainingDataFromFile('LgR_Movies_kNN_classifier.csv')
    print("**"*30)

    my_test_data = [50,50]      # can be supplied to instance.classifyTestData()
    # classOfTestData = instance.classifyTestData(test_data= my_test_data , k=5)

    classOfTestData = instance.classifyTestData(test_data=None , k=5)
    # print(" predictMovieType classOfTestData : ",  classOfTestData)

    return instance.elegantResult.format('movie' , str(instance.test_features) , classOfTestData)
    # to use class variable we use instance. while inside class we use self.

if __name__ == "__main__":
    print(predictMovieType())