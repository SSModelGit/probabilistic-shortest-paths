import numpy as np

class GridWorld:
    """
    This is the example of the grid world example in the reference material.
    """
    def __init__(self, K, init_states):
        """
        K: Size of the KxK grid. (0,0) is at top left, pos x axis going down, pos y axis going right.
        init_states:
          States that will be initialized with specific rewards.
          Border at all states to align coordinates (0,:), (:,0), (K+1,:),(:,K+1)
          Formatted as list of lists: [[x1,y1,r1],...,[xi,yi,ri],...]
        """
        # For a grid of KxK, pad on all sides to make (K+2)x(K+2)
        self.grid = -1 * np.ones([K+2,K+2]) # Initialize with -1 for cost of hitting boundaries
        self.grid[1:-1,1:-1]=0 # Fill the non-border cells with 0s
        self.U_past = self.grid.copy()
        self.policy = np.zeros([K,K],dtype=object)
        self.rewards = self.grid.copy()
        self.gamma = 0.9

        self.actions = dict([["up",   [-1,0]],
                             ["down", [1,0]],
                             ["left", [0,-1]],
                             ["right",[0,1]]])
        self.a_ord   = dict([["up",   0],
                             ["down", 1],
                             ["left", 2],
                             ["right",3]])
        self.a_wt    = dict([["up",   [0.7,0.1,0.1,0.1]],
                             ["down", [0.1,0.7,0.1,0.1]],
                             ["left", [0.1,0.1,0.7,0.1]],
                             ["right",[0.1,0.1,0.1,0.7]]])

        # temporary variables
        # movement intermediaries
        self.pos  = np.array([1,1])
        self.spot = np.array([0,0])
        # utility intermediaries
        self.pnU  = 0
        self.pot_U  = np.zeros([4])
        self.reward = np.zeros([4])

        self.K = K
        self.init_states = init_states
        for x,y,r in init_states:
            self.grid[x][y]=r

    def _something(self):
        for a in self.actions:
            self.spot = self.pos+self.actions[a]
            self.pot_U[self.a_ord[a]] = self.U_past[max(self.spot[0],1)][max(self.spot[1],1)]
            self.reward[self.a_ord[a]] = self.rewards[self.spot[0]][self.spot[1]]

        self.grid[self.pos[0]][self.pos[1]] = -np.inf
        for a in self.actions:
            self.pnU = self.reward.dot(self.a_wt[a])+self.gamma*self.pot_U.dot(self.a_wt[a])
            if self.grid[self.pos[0]][self.pos[1]]<self.pnU:
                self.grid[self.pos[0]][self.pos[1]] = self.pnU
                self.policy[self.pos[0]-1][self.pos[1]-1] = a

    def value_iteration(self, absorbers):
        """
        Implemenation of the value iteration method.
        First the pseudo-code will be explained, and then the function interace:

        Each grid cell is considered a state.
        Actions are moving in one of the four cardinal directions by one square.
        No reward for actions in general; bumping against a wall has reward -1.

        States to be initialized with specific rewards are in self.init_states.
        """
        for i in range(1,self.K+1):
            for j in range(1,self.K+1):
                if i not in absorbers[:,0] and j not in absorbers[:,1]:
                    self.pos = np.array([i,j])
                    self._something()
        return self.policy

if __name__ == "__main__":
    special_states = [[5,4,-5],[8,9,10],[3,8,3],[8,4,-10]]
    grid = GridWorld(10,special_states)
    print(grid.grid)
    print(grid.value_iteration(np.array([[3,8],[8,9]])))
    print(grid.grid)
