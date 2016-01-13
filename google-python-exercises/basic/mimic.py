#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys
import re


def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  # Extract contents from file as a single string and close the file.
  con = open(filename, "r")
  word_string = con.read()
  con.close()
  
  # Format the string so casing is not problematic.
  word_string = word_string.lower()
  
  # Break the string into a list of words.
  word_list = word_string.split()
  
  # Create dictionary capture unique words.
  # Dictionary values will be empty lists to capture following
  # words.
  word_dict = {}
  
  # Capture the unique words as keys associated with empty lists.
  for word in word_list:
    if word not in word_dict.keys():
        word_dict[word] = []
  
  # Populate the dictionary values by searching the (lower-cased)
  # string for the target word and capturing all words that
  # follow it.
  for key in word_dict.keys():
    word_dict[key] = re.findall(r"%s\s([^\s]+)\s" % key, word_string)
    
  # Add an empty string to make sure the first word is represented
  # in a value list.
  word_dict[""] = word_list[0]
    
  return word_dict


def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words."""
  new_string = ""
  
  for count in range(10):
    new_string = new_string + " " + word
    if word not in mimic_dict.keys() or len(mimic_dict[word]) == 0:
        word = mimic_dict[""]
    elif word == "":
        word = mimic_dict[word]
    else:
        word = random.choice(mimic_dict[word])
        
        
  print new_string

# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print 'usage: ./mimic.py file-to-read'
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()
