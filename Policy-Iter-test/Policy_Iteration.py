import numpy as np


def policy_eval(V, P, R, gamma, policy, theta, len_s):
    for s in range(len_s):
        V_best = V[s]
        delta = 0

        V[s] = sum([P[s, int(policy[s]), s1] * (R[s, int(policy[s]), s1] + gamma * V[s1]) for s1 in range(len_s)])
        delta = max(delta, abs(V_best - V[s]))
        if delta < theta:
            return V[s]


def policy_stable(V, P, R, gamma, policy, alpha, theta, len_s):
    for s in range(len_s):
        b = policy[s]
        for a in alpha:
            policy[s] = sum([P[s, a, s1] * (R[s, a, s1] + gamma * V[s1]) for s1 in range(len_s)])
            if policy[s] != b:
                policy[s] = a
                V[s] = policy_eval(V, P, R, gamma, policy, theta, len_s)
            else:
                return policy


def test():
    # How many states; unsure yet so put arbitrary states
    states = [0,1,2,3,4]
    # How many actions can the robot take? (stay, move up, move down, move left, move right)
    alpha = [0,1,2,3,4]

    len_s = len(states)
    len_alpha = len(alpha)

    # empty matrix for transition probability
    P = np.zeros((len_s, len_alpha, len_s))
    # empty matrix for rewards
    R = np.zeros((len_s, len_alpha, len_s))

    # Temp Theta, to compare when delta is a really small pos number
    theta = 0.01

    # Temp gamma
    gamma = 0.2

    # Empty policy (just have zeros)
    policy = [0 for s in range(len_s)]

    # Empty V for now (just zeros)
    V = np.zeros(len_s)

    P[0,0,1] = 0.2
    P[0,1,2] = 0.5
    P[0,2,3] = 0.3
    P[1,0,2] = 0.4
    P[2,1,3] = 0.8
    P[2,3,4] = 0.7
    P[3,1,4] = 0.9
    P[4,0,3] = 0.6


    R[0,0,1] = 1
    R[1,1,3] = 10
    R[3,2,4] = 100
    R[3,3,4] = 100
    R[3,1,4] = 1000
    R[4,1,4] = 10


    # Do policy iter and check if it stabilized
    policy_stable(V, P, R, gamma, policy, alpha, theta, len_s)


if __name__== "__main__":
    test()
