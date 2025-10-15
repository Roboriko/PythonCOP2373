# This program will ask the user to enter their own paragraph, divide it into individual
# sentences and display each one along with the sentence count


import re


# Identifies sentences using expression patterns
SENTENCE_PATTERN = r'[A-Z0-9].*?[.?!](?= [A-Z0-9]|$)'



# Asks the user to input a paragraph
def get_paragraph():
    paragraph = input("Enter a paragraph that may also start with a number:\n\n")
    return paragraph



# Function divides the paragraph into individual sentences
def split_sentences(paragraph):
    sentences = re.findall(SENTENCE_PATTERN, paragraph, flags=re.DOTALL | re.MULTILINE)
    return sentences


# Displays every individual sentence along with sentence count
def display_sentences(sentences):
    print("\n- Individual sentences -:\n")

    count = 0

    # A loop that plays through every sentence and displays it
    for sentence in sentences:
        count += 1
        print(f"{count}. {sentence.strip()}")

    # Displays the total number of sentences
    print(f"\nTotal number of sentences: {count}\n")


# Function that plays through each other function to get the paragraph, count the sentences, and display results
def main():
    # Function that asks user for a paragraph
    paragraph = get_paragraph()

    # Function that divides the paragraph into sentences
    sentences = split_sentences(paragraph)

    # Function that displays final results
    display_sentences(sentences)


# Runs the program
if __name__ == "__main__":
    main()
