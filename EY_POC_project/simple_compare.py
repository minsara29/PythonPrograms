from difflib import SequenceMatcher, context_diff, ndiff
import pandas as pd


def similar(actual, predicted):
    """
    :param actual:Str
    :param predicted: Str
    :return: accuracy: float - percentage
    """
    actual = actual.translate({ord(c): " " for c in "'!@#$%^&*()’[]{};:,./<>?\|`~-=_+"}).lower()
    predicted = predicted.translate({ord(c): " " for c in "'!@#$%^&*()’[]{};:,./<>?\|`~-=_+"}).lower()

    print(actual)
    print(predicted)
    return SequenceMatcher(None, actual, predicted).ratio() * 100

#word by word comparison
def find_accuracy(actual, predicted):

    actual = actual.translate({ord(c): " " for c in "'!@#$%^&*()’[]{};:,./<>?\|`~-=_+"}).lower()
    predicted = predicted.translate({ord(c): " " for c in "'!@#$%^&*()’[]{};:,./<>?\|`~-=_+"}).lower()

    s1 = actual.split()
    s2 = predicted.split()
    count = 0
    for diff in ndiff(s1, s2):
        if '-' in diff:
            count += 1

    return (len(s1) - count) / len(s1) * 100


text1 = """Nina, I really appreciate that you invested so much time and wanted to do a stellar job on your first engagement at the firm, but you own your performance and you own your commitment to meeting deadlines. There are a number of resources available to us all in terms of getting help asking teammates and colleagues. I'd be happy to show you how to look back at some of those things. But in terms of the overall performance, we can't let this happen again. So what do you think you could take as next steps in order to prevent this from happening again?"""
text2 = """Nina i really appreciate that you invested so much time and wanted to do a stellar job on your first engagement the firm. But you own your performance and you own your commitment to meeting deadlines. There are number of resources available to us all in terms of getting help asking teammates and colleagues. I'd be happy to show you how to look back on some of those things. But in terms of the overall performance we can't let this happen again. So. What do you think you could take as next steps in order to prevent this from happening again."""
# text1 = """life is good"""
# text2 = """life was good"""
# text2 = """Life is Good"""

result = similar(text1, text2)
print(result)
accuracy = find_accuracy(text1, text2)
print(accuracy)


