"""
To Start program, click the green 'play button'. To Stop, click the 'stop sign'
To shift left or right in the alphabet, use the left and right arrow keys respectively
To Select the current letter, hit the Spacebar
"""

import tkinter as tk #GUI, graphical user interface
import pyttsx3 #Vocal, text to speech

class AlphabetCycler:
    def __init__(self, root):
        self.root = root
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.index = 0
        self.selected_letter = []
        
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        
        self.label = tk.Label(root, text=self.alphabet[self.index], font=('Arial', 70))
        self.label.pack()
        
        root.bind('<Right>', self.next_letter) #Change '<Right>' to preferred keybind
        
        root.bind('<Left>', self.prev_letter)

        root.bind('<space>', self.type_letter)
        
         
    def next_letter(self, event=None):
        self.index = (self.index+1) % len(self.alphabet)
        current_letter = self.alphabet[self.index]
        self.label.config(text=current_letter)
        self.speak_letter(current_letter)
        
    def prev_letter(self, event=None):
        self.index = (self.index - 1) % len(self.alphabet)
        current_letter = self.alphabet[self.index]
        self.label.config(text=current_letter)
        self.speak_letter(current_letter)
        
    def type_letter(self, event=None):
        self.selected_letter.append(self.alphabet[self.index])
        current_letter = 'Type.'+ self.alphabet[self.index]
        self.speak_letter(current_letter)
        print(''.join(self.selected_letter))
        
    def speak_letter(self, letter):
        self.engine.say(letter)
        self.engine.runAndWait()
        
if __name__ == '__main__':
    root = tk.Tk()
    app = AlphabetCycler(root)
    root.mainloop()