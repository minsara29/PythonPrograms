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


text1 = """At EY you need to own your performance Nina and make sure to be proactive in communicating when you re not able to deliver on agreed upon timelines  What you think should have been done to prevent this from happening"""
text2 = """Eat why You need to own your performance  Nina And make sure to be proactive in communicating when you re not able to deliver on agreed upon  timelines What you think should have been done to prevent this from happening"""

result = similar(text1, text2)
print(result)
accuracy = find_accuracy(text1, text2)
print(accuracy)


