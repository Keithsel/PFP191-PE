#Q3.1
import os

def count_sentences(filepath, keyword):
    # Read the file
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    # Split the text into sentences
    sentences = text.split('.')
    # Count the number of sentences containing the keyword
    count = 0
    for sentence in sentences:
        if keyword.lower() in sentence.lower():
            count += 1
    # Return the result
    return count

def main():
    # Please replace the filepath with the path to the file on your computer
    filepath = 'EXAM_PFP191_FA23\PFP191\Vietnamese_Declaration_of_Independence.txt'
    keyword = 'independence'
    # Strip the name of the file from the filepath
    filename = os.path.basename(filepath)
    # Count the number of sentences containing the keyword
    count = count_sentences(filepath, keyword)
    # Print the result
    print(f"There are {count} sentences in {filename} containins keyword '{keyword}'.")

main()
