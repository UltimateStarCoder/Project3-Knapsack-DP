# Python implementation of Top-Down DP of LCS problem
from tabulate import tabulate

# Returns length of LCS for s1[0..m-1], s2[0..n-1]
def lcs(s1, s2, m, n, memo):
    # Base Case
    if m == 0 or n == 0:
        return 0

    # Already exists in the memo table
    if memo[m][n] != -1:
        print(tabulate(memo, tablefmt="fancy_grid"))
        return memo[m][n]

    # Match
    if s1[m - 1] == s2[n - 1]:
        print(tabulate(memo, tablefmt="fancy_grid"))
        memo[m][n] = 1 + lcs(s1, s2, m - 1, n - 1, memo)
        return memo[m][n]

    # Do not match
    print(tabulate(memo, tablefmt="fancy_grid"))
    memo[m][n] = max(lcs(s1, s2, m, n - 1, memo),
                     lcs(s1, s2, m - 1, n, memo))
    print(tabulate(memo, tablefmt="fancy_grid"))
    return memo[m][n]

if __name__ == "__main__":
    s1 = "AGXI"
    s2 = "GXTG"

    m = len(s1)
    n = len(s2)
    memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
    print(lcs(s1, s2, m, n, memo))
    