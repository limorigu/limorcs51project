__author__ = 'Meg, Limor and Gal'

#!/usr/bin/env python

"""
A simple widget-like system is created supporting keyboard and mouse focus.
This is edited from an online example for a Text GUI, found at:
http://stackoverflow.com/questions/3732605/add-advanced-features-to-a-tkinter-text-widget
"""

import Tkinter as autocorrect
import tkFont
import BK_TREE
import time
import correct

class App(autocorrect.Tk):
    def __init__(self):
        autocorrect.Tk.__init__(self)

        ## Toolbar
        self.toolbar = autocorrect.Frame()
        self.bold = autocorrect.Button(name="toolbar", text="bold",
                              borderwidth=1, command=self.OnBold,)
        self.bold.pack(in_=self.toolbar, side="left")
        self.title("Autocorrect")

        """
        Main part of the GUI
        We'll use a frame to contain the widget
        and scrollbar; it looks a little nicer that way.
        """
        text_frame = autocorrect.Frame(borderwidth=1, relief="sunken")
        self.text = autocorrect.Text(wrap="word", background="white",
                            borderwidth=0, highlightthickness=0)
        self.vsb = autocorrect.Scrollbar(orient="vertical", borderwidth=1,
                                command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(in_=text_frame,side="right", fill="y", expand=False)
        self.text.pack(in_=text_frame, side="left", fill="both", expand=True)
        self.toolbar.pack(side="top", fill="x")
        text_frame.pack(side="bottom", fill="both", expand=True)

        # clone the text widget font and use it as a basis for some
        # tags
        bold_font = tkFont.Font(self.text, self.text.cget("font"))
        bold_font.configure(weight="bold")
        self.text.tag_configure("bold", font=bold_font)
        self.text.tag_configure("misspelled", foreground="red", underline=True)

        """
        set up a binding to do simple spell check. This merely
        checks the previous word when you type a space. For production
        use you'll need to be a bit more intelligent about when
        to do it.
        """
        self.text.bind("<space>", self.Spellcheck)

        # initialize the spell checking dictionary.
        self._words=BK_TREE.BKTree(BK_TREE.levenshtein, BK_TREE.dict_words("big.txt"))


    def Spellcheck(self, event):
        # Spellcheck the word preceding the insertion point
        index = self.text.search(r'\s', "insert", backwards=True, regexp=True)
        if index == "":
            index ="1.0"
        else:
            index = self.text.index("%s+1c" % index)
        # assign last word typed to "word"
        word = self.text.get(index, "insert")
        """if word.lower() in self._words:
            self.text.tag_remove("misspelled", index, "%s+%dc" % (index, len(word)))"""
        # if there is a match, increment frequency of the word
        print(word)
        words = BK_TREE.BKTree.query(self._words,word.strip('.,;\"!:?\'()').lower(),2)
        print(words)
        # if not in tree, run correct and replace with most reasonable replacement
        if len(words) == 0:
            self.text.tag_add("misspelled", index, "%s+%dc" % (index, len(word)))
        # if the word is not in the dictionary replace it
        elif not (words[0][1] == 0):
            # The replacement word is the result of correct on the word we typed and the array that query returns
            new_word = correct.correct(word,words)
            # sequence of checks to add back punctuation
            if not word == '':
                start = word[0]
                end = word[-1]
                if start in ("\'","(","{","[","$",'\"',"*"):
                    new_word = start + new_word
                if end in ("\'",")","]",".",",","\"",";",":","?","!","*"):
                    new_word = new_word + end

            self.text.delete(index, "%s+%dc" % (index, len(word)))
            self.text.insert(index,new_word)

    def OnBold(self):
        """
        Toggle the bold state based on the first character
        in the selected range. If bold, unbold it. If not
        bold, bold it.
        """
        #Toggle the bold state of the selected text
        current_tags = self.text.tag_names("sel.first")
        if "bold" in current_tags:
            # first char is bold, so unbold the range
            self.text.tag_remove("bold", "sel.first", "sel.last")
        else:
            # first char is normal, so bold the whole selection
            self.text.tag_add("bold", "sel.first", "sel.last")

if __name__ == "__main__":
    app=App()
    app.mainloop()