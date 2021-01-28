def truncate(W, threshold):
    val1 = W < threshold
    val2 = W > -threshold
    W[val1&val2] = 0  # all the numbers b/w (-threshold, threshold) are set to 0
    return W