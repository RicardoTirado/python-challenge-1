"""
In this challenge, you get to play the role of chief linguist at a local learning academy. As chief linguist, you are responsible for assessing the complexity of various passages of writing, ranging from the sophomoric Twilight novel to the nauseatingly high-minded research article. Having read so many passages, you've since come up with a fairly simple set of metrics for assessing complexity.

Your task is to create a Python script to automate the analysis of any such passage using these metrics. Your script will need to do the following:

- Import a text file filled with a paragraph of your choosing.
- Assess the passage for each of the following:
  - Approximate word count
  - Approximate sentence count
  - Approximate letter count (per word)
  - Average sentence length (in words)
"""

import os
import re

source_dir = 'raw_data'
file_list  = os.listdir(source_dir)
file_location = []

# Prefix dir to name of file
for file in file_list:
    file_location.append(os.path.join(source_dir, file))

for file in file_location:
    word_count = 0
    letter_count = 0
    
    with open(file, 'r') as txt:
        # Read complete text in
        full_txt = txt.read()
        # Split paragraph
        sentences = re.split(r'[.!?;]\s*', full_txt)
        sentence_count = len(sentences)

        # Count number of words in each sentence        
        for sentence in sentences:
            sentence.strip()
            words = sentence.split()

            for word in words:
                # Add to total word count
                word_count += 1
                # Count number of letters in each word
                letter_count += len(word)

        print(f"\nParagraph Analysis for File '{file}'\n-----------------\nApproximate Word Count: {word_count}")  
        # Truncate float to 4 decimal points
        print(f"Approximate Sentence Count: {sentence_count}\nAverage Letter Count: {(letter_count / word_count):.4f}") 
        print(f"Approximate Sentence Length: {(word_count / sentence_count):.4f}\n")