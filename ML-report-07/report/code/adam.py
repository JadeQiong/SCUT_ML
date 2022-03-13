elif mode == "adam":
delta = 1e-8
beta1 = 0.9
beta2 = 0.999
m = 0
v = 0
learning_rate = para['learning_rate']

grad = compute_gradient(x, y, w)
 #print("Grad is " +str(grad))
m = beta1 * m + (1 - beta1) * grad
v= beta2 * v + (1 - beta2) * (grad **2)
m_hat = m / (1 - beta1)
v_hat = v / (1 - beta2)
w -= (m_hat * learning_rate)/(np.sqrt(v_hat) + delta)