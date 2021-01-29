def truncate(W, threshold, mval):
    W /= mval
    val = W < threshold
    W[val] = 0  # all the numbers b/w (-threshold, threshold) are set to 0
    W *= mval
    return W