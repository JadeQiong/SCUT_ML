def extract(self):
    '''Extract features from given image.
    Returns:
        A one-dimension ndarray to store the extracted NPD features.
    '''
     count = 0
       for i in range(self.n_pixels - 1):
            for j in range(i + 1, self.n_pixels, 1):
                self.features[count] = NPDFeature.__NPD_table__[self.image[i]][self.image[j]]
           	count += 1
return self.features