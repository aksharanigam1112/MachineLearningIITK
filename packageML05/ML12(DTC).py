import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split

from sklearn.externals.six import StringIO
from IPython.display import Image
import pydotplus

df = pd.read_csv("diabetes.csv")
array = df.values
x = array[:,0:8]
y = array[:,8]

xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.2,random_state=1)

model = DecisionTreeClassifier()
model = model.fit(xtrain,ytrain)
ypred = model.predict(xtest)
# print(ypred)

dot_data = StringIO()
export_graphviz(model , out_file=dot_data , filled=True , rounded=True , special_characters=True)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('diabetes.png')
Image(graph.create_png())

