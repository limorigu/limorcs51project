AutoCorrect

CONTENTS OF THIS FILE
---------------------
   
 * Introduction
 This program is a python implementation of an autocorrect, including a graphic user interface. It is run from the main function. Once running, it will first construct a BK tree version of a dictionary (depending on the .txt file uploaded into it). Then, a GUI will pop up, and allow the user to write words, checking the spelling of the last word every time a space bar is hit. 

If it is similar enough to a word found in the dictionary, it will change it to the closest one, depending on Levenshtein distance and frequency of use in common texts (once again, depends on the .txt file uploaded). If such a close match is not found, will tag it as misspelled, by marking it in red.

 * Requirements
First, your computer needs to run Python 2.7. Next, in order to run the program, you need to download four different files and save them in the same directory - main.py, correct.py, BKtree.py and a .txt file of your choice that will function as you preferred dictionary. NOTICE: if you wish to change the dictionary we are providing you with, make sure to change the name of the .txt file uploaded in line 56 in our main.py file, such that it will read self._words=BK_TREE.BKTree(BK_TREE.levenshtein, BK_TREE.dict_words(“YOURFILE.txt”)). Furthermore, make sure to save your .txt file in the same directory in which main.py, correct.py and BKtree.py are saved.

 * Initialization
When first running the program, the construction of the BKtree tree, based on the .txt file, might take a few minutes, depending on the size of the file. Please be patient. After this initial run - the program will keep on running smoothly until you close the window.

 * Troubleshooting
Make sure you save all four files needed for the program in the same directory. Additionally, make sure you are using Python version 2.7. As for the time the initial construction of the dictionary might take - once again, please be patient :)

 * FAQ
Q: What is a poop deck? A: We’re not quite sure. 
Q: How do I make my dictionary more accurate? A: Upload a bigger .txt file, including more books and other sources, so that our algorithm can get a more accurate frequency of use values. 
Q: Can I make words bold? A: Yes. Simply highlight the word you are interested in bolding, and click on the bold button on the top left part of the window. 
Q: Why a pirate dictionary? A: Go away you scurvy dog! Ye be warned.