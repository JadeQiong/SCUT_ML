from sklearn.datasets import load_svmlight_file
from io import BytesIO

X, y = load_svmlight_file(f=BytesIO(r.content), n_features=13)
X = X.toarray()

# preprocess
n_samples, n_features = X.shape
X = numpy.column_stack((X, numpy.ones((n_samples, 1))))
#change y to an array of 1 columns
y = y.reshape((-1, 1))