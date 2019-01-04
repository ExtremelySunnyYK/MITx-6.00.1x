# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 15:20:05 2019

@author: admin
"""
class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        super().__init__(text)
        

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
       #Split the words up
       #Run a loop and shifts the text range(0,27)
       #Test if the word is valid. Count no of real words
       #If yes, break and return the best shift value and text
       #else, continue trying out all the shift
        
        shift = 0
        mem = {}
        for i in range(0,27):
            counter = 0
            for j in super(CiphertextMessage, self).apply_shift(shift).split(' '):
                if is_word(self.valid_words, j) == True:
                    counter +=1
            mem[shift] = counter
            shift +=1
        
        best_shift = max(mem,key = mem.get)
        hidden_message = super(CiphertextMessage, self).apply_shift(best_shift)
        return (best_shift,hidden_message)
        
        
            
            
