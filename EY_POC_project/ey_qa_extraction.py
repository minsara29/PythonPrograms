import pandas as pd
import re

def extract_question(string):
    pattern = r"\s*([^.?]*(?:do|did|is|are|was|were|will|can|could|may|what|where|describe|who|when|how)[^.?]*?\s*\?)"
    string = str(string).lower()
    return re.findall(pattern, string)

def extract_question_keywords(strings):
    result_lst = []
    for string in strings:
        print(string)
        words = string.split(' ')
        for i, word in enumerate(words):
            if word in wh_ques_keys:
                result_lst.append(word)
            if word in ax_ques_keys:
                result_lst.append(f"{word} {words[i + 1]}")
            if word in other_ques_keys:
                result_lst.append(word)
    print(result_lst)
    return result_lst

q_script = []
q_questions = []
all_script = []
all_questions = []
question_words = []

question_list = ["do i", "do you",  "is it", "would you", "is there",
"are there", "is it so", "is this true", "to know", "is that true", "are we", "am i",
 "question is", "tell me more", "can i", "can we", "tell me", "can you",
 "question","answer", "questions", "answers", "ask","can you", "what", "who", "why", "how",]

wh_ques_keys = ['how much', 'how many', 'how often', 'how far', 'what',"what's", 'when', 'why', 'which', 'who', 'how', 'whose', 'whom', 'where', 'whether', 'whatsoever', 'whence', 'right?', 'have you']
ax_ques_keys = ['do', 'does', 'did', 'were', 'will', 'shall', 'could', 'would', 'can', 'is', 'are', 'am']
other_ques_keys = ['question', 'questions', 'answer', 'answers', 'ask', 'tell me']

df = pd.read_excel('ey_data/EY Foundry - Consolidated Pilot Transcripts Data.xlsx', sheet_name='Transcripts')

for index, row in df.iterrows():
    # print('--------------------------------')
    # print(row["Learner's transcript"])
    results = extract_question(row["Learner's transcript"])
    # print(results)
    # print('--------------------------------')
    all_script.append(row["Learner's transcript"])
    all_questions.append(results)
    if results == []:
        pass
    else:
        q_script.append(row["Learner's transcript"])
        q_questions.append(results)
        question_words.append(extract_question_keywords(results))

# out_df = pd.DataFrame(list(zip(all_script, all_questions)),
#                columns =["Learner's transcript", "Questions"])

q_df = pd.DataFrame(list(zip(q_script, q_questions, question_words)),
               columns =["Learner's transcript", "Questions", "Question Keywords"])


# out_df.to_csv("output_ey_data/all_question_extractions.csv")
q_df.to_csv("output_ey_data/EY_question_extractions.csv")


#
# txt = "I like to eat apple. Me too. Let's go buy some oranges."
# txt = "Hi Rose, it's always a pleasure to meet and talk about performance and expectations. What I hear you saying is you feel like you did a really good job on the most recent work and that the client was really happy with what you turned in. I also hear that you're looking to be progressed into a manager position this year. Is that right? Did I capture that correctly wage?"
# results = extract_question(txt)

# """
# \s*([^.?]*(?:how|can|what|where|describe|who|when)[^.?]*?\s*\?)
# """