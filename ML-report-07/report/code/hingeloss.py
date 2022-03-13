def hinge_loss(x, y, w):
    # hinge_loss = max(0,1-yi(wTX +b))
    y_hat = np.matmul(x, w)
    # min L(w,b) = 1/2(w**2) + C/n sigma_{1}^{n} max(0, 1-yi(w^T * xi + b))
    # hinge_loss = np.maximum(0, 1 - y * (y_hat + bias))
    hinge_loss = np.maximum(0, 1- y * y_hat)
    return hinge_loss
