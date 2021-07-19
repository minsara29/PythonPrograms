from difflib import SequenceMatcher, context_diff, ndiff
import pandas as pd

#letter by Letter comparison
def similar(actual, predicted):
    """
    :param actual:Str
    :param predicted: Str
    :return: accuracy: float - percentage
    """
    return SequenceMatcher(None, actual, predicted).ratio() * 100

#word by word comparison
def find_accuracy(actual, predicted):
    s1 = actual.replace(".", "").replace(",", "").replace("'", "").replace('"', "").split()
    s2 = predicted.replace(".", "").replace(",", "").replace("'", "").replace('"', "").split()
    count = 0
    for diff in ndiff(s1, s2):
        if '-' in diff:
            count += 1

    return (len(s1) - count) / len(s1) * 100



#read the xlsx file
file_name = "../EY_POC/data\\transcripts_july14.xlsx"
excel = pd.read_excel(file_name, sheet_name=None)

#processing the records
for key, data in excel.items():
    for index, row in data.iterrows():
        data.at[index, 'Google_letter_accuracy'] = similar(row['Original Transcription'], row['Google regular Transcription'])
        data.at[index, 'Google_Enhanced_letter_accuracy'] = similar(row['Original Transcription'], row['Google Enhanced Transcriptions'])
        data.at[index, 'Azure_letter_accuracy'] = similar(row['Original Transcription'], row['Azure Transcription'])
        data.at[index, 'AWS_letter_accuracy'] = similar(row['Original Transcription'], row['AWS Transcriptions'])

        data.at[index, 'Google_word_accuracy'] = find_accuracy(row['Original Transcription'], row['Google regular Transcription'])
        data.at[index, 'Google_Enhanced_word_accuracy'] = find_accuracy(row['Original Transcription'], row['Google Enhanced Transcriptions'])
        data.at[index, 'Azure_word_accuracy'] = find_accuracy(row['Original Transcription'], row['Azure Transcription'])
        data.at[index, 'AWS_word_accuracy'] = find_accuracy(row['Original Transcription'], row['AWS Transcriptions'])


#writing output in csv format
data.to_csv('output\\excel_accuracy_july14.csv', index=False)