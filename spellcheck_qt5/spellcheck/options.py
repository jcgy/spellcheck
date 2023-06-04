# Import the main window object (mw) from aqt
from aqt import mw
from anki.hooks import addHook
# Import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect
# Import all of the Qt GUI library
from aqt.qt import *
import glob
import os
# Import constants
from .const import *

# Options window
class OptionsDialog(QDialog):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Spellcheck Options")

		# Dictionary selection
		self.dictionary_combo = QComboBox()
		# Get dictionary file names
		dict_files = [os.path.basename(x) for x in glob.glob(f"{dict_dir}")]
		for i in dict_files:
			self.dictionary_combo.addItem(f"{i}", f"{i}")
		self.dictionary_combo.setCurrentIndex(self.dictionary_combo.findData(options["dictionary"]))

		# Save buton
		self.save_button = QPushButton("Save")
		self.save_button.clicked.connect(self.save_options)

		# Layout
		layout = QVBoxLayout()
		layout.addWidget(QLabel("Dictionary:"))
		layout.addWidget(self.dictionary_combo)
		layout.addWidget(self.save_button)
		self.setLayout(layout)

	# Save options
	def save_options(self):
		selected_dictionary = self.dictionary_combo.currentData()
		options["dictionary"] = selected_dictionary
		config["dictionary"] = selected_dictionary
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