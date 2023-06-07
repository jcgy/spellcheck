import os
from aqt import mw
import glob

# Global variables
ADDON_NAME = "Spellcheck"
DICT_DIR = os.path.join(mw.pm.base, "dictionaries/")
CONFIG = mw.addonManager.getConfig(ADDON_NAME)
# If QTWEBENGINE_DICTIONARIES_PATH is set, the spellchecker uses the dictionaries
# in the specified directory without looking anywere else.
# Otherwise, it uses the qtwebengine_dictionaries directory relative to the executable
# if it exists. If it does not exist, it will look in QT_INSTALL_PREFIX/qtwebengine_dictionaries.
os.environ["QTWEBENGINE_DICTIONARIES_PATH"] = DICT_DIR
