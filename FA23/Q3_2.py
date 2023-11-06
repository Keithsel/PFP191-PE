#Q3.2
def count_words(filepath):
    # Read the file
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read().replace('\n', ' ').lower() # Replace newlines with spaces and convert to lowercase
        # Remove all non-alphanumeric characters except spaces
        for char in text:
            if not char.isalnum() and not char.isspace():
                text = text.replace(char, "")
        # Split the text into words
        words = [word for word in text.split(' ') if word != '']    
        # Count the number of occurrences of each word
        words_dict = {}
        for word in words:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1
        # Sort the dictionary by value in descending order
        sorted_words = sorted(words_dict.items(), key = lambda x: x[1], reverse = True)
        # Return the dictionary of top 10 most frequent words
        return dict(sorted_words[:10])

def main():
    # Please replace the filepath with the path to the file on your computer
    filepath = 'EXAM_PFP191_FA23\PFP191\Vietnamese_Declaration_of_Independence.txt'
    # Count the top 10 most frequent words
    words_dict = count_words(filepath)
    # Print the result
    for word, count in words_dict.items():
        print(f"{word} {count}")

main()
