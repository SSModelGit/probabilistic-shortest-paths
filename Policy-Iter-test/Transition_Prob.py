

def transition_matrix(t):
    """
    :param t: possible state transitions
    :return: transition matrix, P
        P[i][j] is the probability of transitioning from i to j
    """
    # num of possible states (in test, max = 9, so possib from 0 -> 11 (11 states))
    n = 1 + max(t)

    # Initialize prob transition matrix
    P = [[0]*n for _ in range(n)]

    # go through and add one for each state by row and col
    for (i,j) in zip(t,t[1:]):
        P[i][j] += 1

    # convert to prob
    for row in P:
        s = sum(row)
        if s > 0:
            row[:] = [f/s for f in row]
    return P


if __name__ == "__main__":
    # states labeled as successive integers, transitions between states
    T = [1,3,5,6,0,1,2,4,6,11,2,5,8,3,9,10,11,4,6,11]
    P = transition_matrix(T)
    for rows in P:
        print(' '.join('{0:.2f}'.format(i) for i in rows))