from .smb_env import SuperMarioBrosEnv
class SuperMarioBrosEnvStraight(SuperMarioBrosEnv):
    """This environment focuses on just getting Mario form the start of the level to the end of level
    in the 'traditional' way which is going from the right of the map to left of map whilst trying not to die"""

    def __init__(self, rom_mode='vanilla', lost_levels=False, target=None):
        super().__init__(rom_mode=rom_mode, lost_levels=lost_levels, target=target)


    @property
    def _x_reward(self):
        """Return the reward based on left right movement between steps."""
        _reward = self._x_position - self._x_position_last
        self._x_position_last = self._x_position
        # TODO: check whether this is still necessary
        # resolve an issue where after death the x position resets. The x delta
        # is typically has at most magnitude of 3, 5 is a safe bound
        if _reward < -5 or _reward > 5:
            return 0

        return _reward

    @property
    def _time_penalty(self):
        """Return the reward for the in-game clock ticking."""
        _reward = self._time - self._time_last
        self._time_last = self._time
        # time can only decrease, a positive reward results from a reset and
        # should default to 0 reward
        if _reward > 0:
            return 0

        return _reward



    def _get_reward(self):
        """Return the reward after a step occurs."""
        return self._x_reward + self._time_reward + self._death_penalty




