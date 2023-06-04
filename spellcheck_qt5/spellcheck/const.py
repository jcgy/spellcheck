import os
from aqt import mw

# Global variables
addon_name = "Spellcheck"
dict_dir = os.path.join(mw.pm.base, "addons21/spellcheck/dictionaries/*")
config = mw.addonManager.getConfig(addon_name)
options = {
	"dictionary": config["dictionary"]
}