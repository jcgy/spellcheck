import os
from aqt import mw
import glob

# Global variables
ADDON_NAME = "Spellcheck"
DICT_DIR = os.path.join(mw.pm.base, "addons21/spellcheck/dictionaries/*")
CONFIG = mw.addonManager.getConfig(ADDON_NAME)