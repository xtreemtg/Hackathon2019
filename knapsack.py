def knapsack(W, wt, val, n):
    """ Return max value while keeping weight under W. """
    K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]

# Driver program to test above function
# val = [60, 100, 120]
# wt = [10, 20, 30]
# W = 50
# n = len(val)
# print(knapsack(W, wt, val, n))
