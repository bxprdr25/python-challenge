import re
import csv
import os

outputPath = os.path.join(".", "Analysis", "PyParagraph")
paragraphTwo = os.path.join(".", "Resources", "paragraph_2.txt")

with open(paragraphTwo, 'r') as textData:

    #read the text file and determine the word count
    paraLines = textData.read()
    wordCount = paraLines.split()

    #split the sentences by punctuation and determine the sentence count
    sentences = re.split(r'[!?]+|(?<!\.)\.(?!\.)', paraLines)
    sentences = sentences[:-1]
    sentence_count = len(sentences)

    #create a letter counter variable to iterate through each word and calculate the average
    letterCount = 0
    for word in wordCount:
        letterCount = letterCount + len(word)
        avgLetterCount = round(letterCount/len(wordCount), 2)

    #create a list to append the words in sentences iterate through sentences and calculate the average sentence lengh
    wordsInSentence = []

    for sentence in sentences:

        wordsInSentence.append(len(sentence.split(" ")))

        avgSenLen = round(sum(wordsInSentence) / len(wordsInSentence), 2)

    #print results to terminal
    print(f"Paragraph Analysis")
    print(f"------------------")
    print("Approximate Word Count: " + str(len(wordCount)))
    print("Approximate Sentence Count: " + str(sentence_count))
    print("Average Letter Count: " + str(avgLetterCount))
    print(f"Average Sentence Length: " + str(avgSenLen))
    print(f"------------------")

    # print results to a text file
with open(outputPath, "w", newline='') as textfile:
    print(f"Paragraph Analysis", file=textfile)
    print(f"------------------", file=textfile)
    print("Approximate Word Count: " + str(len(wordCount)), file=textfile)
    print("Approximate Sentence Count: " + str(sentence_count), file=textfile)
    print("Average Letter Count: " + str(avgLetterCount), file=textfile)
    print(f"Average Sentence Length: " + str(avgSenLen), file=textfile)
    print(f"------------------", file=textfile)