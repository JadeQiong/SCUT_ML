 def fit(self,X,y):
        '''Build a boosted classifier from the training set (X, y).

        Args:
            X: An ndarray indicating the samples to be trained, which shape should be (n_samples,n_features).
            y: An ndarray indicating the ground-truth labels correspond to X, which shape should be (n_samples,1).
        '''
        #the same weight at the beginning
        w = np.ones(y.shape)
        #normalization
        w = w/w.sum()
        self.a = []
        self.base_clfs = []
        
        for i in range(self.n_weakers_limit):
            base_clf=copy.copy(self.weak_clf)
            base_clf.fit(X, y.flatten(),w.flatten())
            # train a basic classifier
            y_pred = base_clf.predict(X).reshape((-1,1))
            #calculate the error rate
            err_rate = w.T.dot(y_pred!=y)[0][0]/w.sum()
            
            if err_rate > 1/2 or err_rate == 0.0:
                break
             
            weight_param_a = math.log((1-err_rate)/err_rate) /2
            
            self.base_clfs.append(base_clf)
            self.a.append(weight_param_a)
            #update the weight
            w = w * np.exp(-weight_param_a*y*y_pred)
            w = w/w.sum()