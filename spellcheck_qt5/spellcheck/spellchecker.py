from aqt.qt import *
from aqt import mw
from aqt.webview import AnkiWebView
from anki.hooks import wrap, addHook
from aqt import gui_hooks
from anki.lang import _
from functools import partial

from .const import *

def replaceMisspelledWord(page, sug_word):
    page.replaceMisspelledWord(sug_word)

def onContextMenuEvent(web, menu):
    # Add suggested words to context menu (middle click)
    p=web._page.profile()

    b=p.isSpellCheckEnabled()
    menu.addSeparator()
    a=menu.addAction(_("Spellcheck"))
    a.setCheckable(True)
    a.setChecked(b)
    a.triggered.connect(lambda:p.setSpellCheckEnabled(not b))

    if b:
        firstAct=menu.actions()[0]
        data=web._page.contextMenuData()
        for sug_word in data.spellCheckerSuggestions():
            a=menu.addAction(sug_word)
            menu.insertAction(firstAct, a)
            a.triggered.connect(partial(replaceMisspelledWord, web._page, sug_word))
            # add in blod font
            f=a.font()
            f.setBold(True)
            a.setFont(f)
        menu.insertSeparator(firstAct)

def setupBDIC(web, *args, **kwargs):
    p=web._page.profile()
    # Needs to be passed as list and without extentions .bdic
    current_dictionary = [ CONFIG["dictionary"][:-5] ]
    p.setSpellCheckLanguages(current_dictionary)
    p.setSpellCheckEnabled(True)

gui_hooks.editor_will_show_context_menu.append(onContextMenuEvent)
gui_hooks.webview_will_show_context_menu.append(onContextMenuEvent)

AnkiWebView.__init__=wrap(AnkiWebView.__init__, setupBDIC, "after")