import warnings
from .v2 import *  # noqa F403

warnings.warn(
    "Should not be imported like that. Should use `from trame.modules import vuetify2` instead"
)
