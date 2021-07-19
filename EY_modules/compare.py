from difflib import SequenceMatcher, context_diff, ndiff
import pandas as pd

#letter by Letter comparison
def similar(actual, predicted):
    """
    :param actual:Str
    :param predicted: Str
    :return: accuracy: float - percentage
    """
    actual = "".join(e for e in actual if e.isalnum())
    predicted = "".join(e for e in predicted if e.isalnum())

    print(actual)
    print(predicted)
    return SequenceMatcher(None, actual, predicted).ratio() * 100

#word by word comparison
def find_accuracy(actual, predicted):

    actual = "".join(e for e in actual if e.isalnum())
    predicted = "".join(e for e in predicted if e.isalnum())

    s1 = actual.replace(".", "").replace(",", "").replace("'", "").replace('"', "").split()
    s2 = predicted.replace(".", "").replace(",", "").replace("'", "").replace('"', "").split()
    count = 0
    for diff in ndiff(s1, s2):
        if '-' in diff:
            count += 1

    return (len(s1) - count) / len(s1) * 100



#read the xlsx file
file_name = "../EY_POC/data\\transcripts_july141.csv"

excel = pd.read_csv(file_name,  encoding='utf8')

print(excel.columns)


Google_regular_letter = []
Google_Enhanced_letter = []
Azure_letter = []
AWS_letter = []
Google_regular_word = []
Google_Enhanced_word = []
Azure_word = []
AWS_word = []


for index, data in excel.iterrows():
    Google_regular_letter.append(similar(data["Original Transcription"], data["Google regular Transcription"]))
    Google_Enhanced_letter.append(similar(data["Original Transcription"], data["Google Enhanced Transcriptions"]))
    Azure_letter.append(similar(data["Original Transcription"], data["Azure Transcription"]))
    AWS_letter.append(similar(data["Original Transcription"], data["AWS Transcriptions"]))
    #
    Google_regular_word.append(find_accuracy(data["Original Transcription"], data["Google regular Transcription"]))
    Google_Enhanced_word.append(find_accuracy(data["Original Transcription"], data["Google Enhanced Transcriptions"]))
    Azure_word.append(find_accuracy(data["Original Transcription"], data["Azure Transcription"]))
    AWS_word.append(find_accuracy(data["Original Transcription"], data["AWS Transcriptions"]))

# print(excel.columns)
excel["Google_regular_letter_accuracy"] = Google_regular_letter
excel["Google_Enhanced_letter_accuracy"] = Google_Enhanced_letter
excel["Azure_letter_accuracy"] = Azure_letter
excel["AWS_letter_accuracy"] = AWS_letter
#
excel["Google_regular_word_accuracy"] = Google_regular_letter
excel["Google_Enhanced_word_accuracy"] = Google_Enhanced_letter
excel["Azure_word_accuracy"] = Azure_letter
excel["AWS_word_accuracy"] = AWS_letter

#writing output in csv format
# excel.to_csv('output\\transcript_accuracy_july14.csv', index=False)


# import numpy as np
# def find_accuracy(actual,predicted):
#     actual_list = np.array(actual.split())
#     predicted_list = np.array(predicted.split())
#     correct = (actual_list == predicted_list)
#     return correct.sum() / correct.size

text1 = """And I understand that you feel you've done a great job on this project. Let's talk a little more about you know, are your expectations versus how you've done on the project and how you've done in general and we'll take it from there."""
text2 = """and I understand you feel you've done a great job on this project. Let's talk a little bit more about, you know, our your expectations versus how you've done in the project, how you've done in general, we'll take it from there."""

result = similar(text1, text2)
print(result)
# accuracy = find_accuracy(text1, text2)
# print(accuracy)

