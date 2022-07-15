import os
from typing import Optional

env1 = os.environ.get('RUN_HEADLESS')


def should_run_headless() -> bool:
    """
    Checks if Chrome should run in headless mode or not.
    """
    return bool(_get_env_var("RUN_HEADLESS") == "True")
    # return bool(_get_env_var(env1))



def _get_env_var(name, default: str = "True"):
    """
    Gets the value of an environment variable. If the environment variable does not exist, it throws a ValueError.
    :param name: The name of the environment variable to fetch.
    :param default: Option for setting a default value to return if the env variable is not found.
    :return: The value of an environment variable.
    """
    # print(env1)
    if name not in os.environ and not default:
        raise ValueError(f"The {name} environment variable has not been set.")
    return os.getenv(name, default)


def get_is_inside_wsl() -> Optional[str]:
    """
    Check if working inside WSL to set DISPLAY variable for UI tests local debug
    """
    return _get_env_var("AUT_IS_INSIDE_WSL", default="")