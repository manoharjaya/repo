# Load libraries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Load dataset
url = "iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

print dataset





'''
Summarize the Dataset

Now it is time to take a look at the data.

In this step we are going to take a look at the data a few different ways:

    1)Dimensions of the dataset.
    2)Peek at the data itself.
    3)Statistical summary of all attributes.
    4)Breakdown of the data by the class variable.

'''

# shape
print dataset.shape

# head
print(dataset.head(10))

# descriptions
print(dataset.describe())

# class distribution
print(dataset.groupby('class').size())


# # box and whisker plots
# dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
# plt.show()


# # histograms
# dataset.hist()
# plt.show()

# # scatter plot matrix
# scatter_matrix(dataset)
# plt.show()


print
# Split-out validation dataset
array = dataset.values
X = array[:,0:4]
Y = array[:,4]
print X
print Y
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)