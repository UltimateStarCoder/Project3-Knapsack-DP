# A dynamic programming based python program
# to find length of the shortest supersequence

# Returns length of the shortest supersequence of X and Y
from tabulate import tabulate

def superSeq(X, Y, m, n):
    dp = [[0] * (n + 2) for i in range(m + 2)]

    # Fill table in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):

            # Below steps follow above recurrence
            if (not i):
                dp[i][j] = j
            elif (not j):
                dp[i][j] = i

            elif (X[i - 1] == Y[j - 1]):
                dp[i][j] = 1 + dp[i - 1][j - 1]

            else:
                dp[i][j] = 1 + min(dp[i - 1][j],
                                   dp[i][j - 1])
    print(tabulate(dp, tablefmt="fancy_grid"))
    return dp[m][n]


X = "cat"
Y = "tax"
print("Length of the shortest supersequence is %d"
      % superSeq(X, Y, len(X), len(Y)))