# Import the main window object (mw) from aqt
from aqt import mw
from anki.hooks import addHook
# Import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect
# Import all of the Qt GUI library
from aqt.qt import *

# Global variables
addon_name = "Spellcheck"
config = mw.addonManager.getConfig(addon_name)
options = {
	"language": config["language"]
}

# Options window
class OptionsDialog(QDialog):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Spellcheck Options")

		# Language selection
		self.language_combo = QComboBox()
		self.language_combo.addItem("English (US)", "en_US")
		self.language_combo.addItem("English (UK)", "en_UK")
		self.language_combo.setCurrentIndex(self.language_combo.findData(options["language"]))

		# Save buton
		self.save_button = QPushButton("Save")
		self.save_button.clicked.connect(self.save_options)

		# Layout
		layout = QVBoxLayout()
		layout.addWidget(QLabel("Language:"))
		layout.addWidget(self.language_combo)
		layout.addWidget(self.save_button)
		self.setLayout(layout)

	# Save options
	def save_options(self):
		selected_language = self.language_combo.currentData()
		options["language"] = selected_language
		config["language"] = selected_language
		mw.addonManager.writeConfig(addon_name, config)
		self.close()

# Add the menu item to access the options dialog
def show_options_dialog():
	dialog = OptionsDialog()
	dialog.exec()

# Create a new menu item, "test"
action = QAction("Spellcheck Options", mw)
# set it to call testFunction when it's clicked
qconnect(action.triggered, show_options_dialog)
# And add it to the tools menu
mw.form.menuTools.addAction(action)