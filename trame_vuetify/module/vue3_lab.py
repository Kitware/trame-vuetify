import warnings
from .v3_lab import *  # noqa F403

warnings.warn(
    "Should not be imported like that. Should use `from trame.modules import vuetify3_lab` instead"
)
