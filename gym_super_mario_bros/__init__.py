"""Registration code of Gym environments in this package."""
from .smb_env import SuperMarioBrosEnv
from .smb_random_stages_env import SuperMarioBrosRandomStagesEnv
from .smb_env_straight import SuperMarioBrosEnvStraight
from ._registration import make


# define the outward facing API of this package
__all__ = [
    make.__name__,
    SuperMarioBrosEnv.__name__,
    SuperMarioBrosRandomStagesEnv.__name__,
    SuperMarioBrosEnvStraight.__name
]
