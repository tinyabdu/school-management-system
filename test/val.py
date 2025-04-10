import random
from enum import Enum, EnumMeta
from typing import TYPE_CHECKING, Dict, List, Optional, Union
from warnings import warn

values = ["me", "you", "us"]

def random_values():
    return random.choice(list(values))

print(random_values())

if random_values() == "me":
    print(warn(message="dont try it"))