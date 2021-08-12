wh_ques_keys = ['how much','how many','how often','how far','what', 'when', 'why', 'which', 'who', 'how', 'whose', 'whom', 'where', 'whether', 'whatsoever', 'whence']
ax_ques_keys = ['do', 'does', 'were', 'will', 'shall', 'could', 'can', 'is', 'are', 'am' ]
other_ques_keys = ['question', 'questions', 'answer', 'answers', 'ask', 'tell']

texts = ["so could you elaborate a little more about you know why you think you're ready to be manager?"]

question_words = []

for string in texts:
    words = string.split(' ')
    for i, word in enumerate(words):
        if word in wh_ques_keys:
            question_words.append(word)
        if word in ax_ques_keys:
            question_words.append(f"{word} {words[i+1]}")
        if word in other_ques_keys:
            question_words.append(word)


print(question_words)