def truncate(W, threshold, mval):
    W /= mval
    val1 = W <= threshold
    val2 = W >= -threshold
    W[val1 & val2] = 0  # all the numbers b/w (-threshold, threshold) are set to 0
    W *= mval
    return W