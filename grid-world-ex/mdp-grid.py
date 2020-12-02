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
        self.grid = -1 * np.ones([K+2,K+2],dtype=int) # Initialize with -1 for cost of hitting boundaries
        self.grid[1:-1,1:-1]=0 # Fill the non-border cells with 0s
        self.U_past = self.grid.copy()
        self.U_future = self.grid.copy()
        self.init_states = init_states
        for x,y,r in init_states:
            self.grid[x][y]=r

    def _calc_reward(self,i,j):
        """
        Determines if coodinates indicate border state, and calculates the reward.
        """
        return -1 if (i == 0 or i == self.K+2 or j == 0 or j == self.K+2) else 0

    def value_iteration(self):
        """
        Implemenation of the value iteration method.
        First the pseudo-code will be explained, and then the function interace:

        Each grid cell is considered a state.
        Actions are moving in one of the four cardinal directions by one square.
        No reward for actions in general; bumping against a wall has reward -1.

        States to be initialized with specific rewards are in self.init_states.
        """

if __name__ == "__main__":
    special_states = [[5,4,-5],[8,9,10],[3,8,3],[8,4,-10]]
    grid = GridWorld(10,special_states)
    print(grid.grid)
