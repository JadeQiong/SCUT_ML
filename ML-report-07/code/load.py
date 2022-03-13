X_train, y_train = ds.load_svmlight_file("C:/Users/87179/Desktop/ML2019-lab-02/a9a.txt")
X_test, y_test = ds.load_svmlight_file("C:/Users/87179/Desktop/ML2019-lab-02/a9a.t",n_features = 123)

X_train = X_train.toarray()
X_test = X_test.toarray()
# add a column of 1s to X_train & X_test
X_train = np.concatenate([X_train, np.ones(shape=[X_train.shape[0], 1], dtype = np.float32)],axis = 1)
X_test = np.concatenate([X_test, np.ones(shape=[X_test.shape[0], 1], dtype=np.float32)], axis = 1)

y_train = y_train.reshape([len(y_train), 1])
y_test = y_test.reshape([len(y_test),1 ])