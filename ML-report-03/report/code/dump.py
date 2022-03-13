if dataset_dump_file not in glob.glob(os.getcwd() + r'\*'):
    D_face = load_img(os.getcwd() + r'\datasets\original\face', 1)
    D_nonface = load_img(os.getcwd() + r'\datasets\original\nonface', -1)
    D = np.vstack((D_face, D_nonface))
    with open(dataset_dump_file, 'wb') as f:
        # pickle  library dump() function into the memory
        #use load() function to process data
pickle.dump(D, f, pickle.HIGHEST_PROTOCOL)