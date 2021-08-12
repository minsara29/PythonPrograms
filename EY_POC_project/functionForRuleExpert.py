def Caller(type, node_input, input_string):
    if type == “pass”: return True, 1.0, “”
    elif type == “meaning_similarity”:
    threshold = eval(node_input[0])
    return meaning_similarity(input_string, node_input[1:], threshold)

elif type == “keyword_analysis”:
keywords = []
pos_tags = []
if len(node_input) == 2:
    keywords.append(node_input[0])
    pos_tags.append(node_input[1])
elif len(node_input) > 2 and len(node_input) % 2 == 0:
    for i in range(0, len(node_input) - 3:
        keywords.append(node_input[i])
    pos_tags.append(node_input[i + 1])
    else: return False
    return keyword_analysis(input_string, keywords, pos_tags)
elif type == “perspective_analysis”:
    return perspective_analysis(input_string, eval(node_input[0]))
elif type == “sentiment_analysis”:
    total_flag == False
    if node_input[1].lower() == “true”: total_flag == True
    threshold = eval(node_input[2])
    return sentiment_analysis(input_string, node_input[0], total_flag, threshold)
elif type == “question_analysis”:
    return question_analysis(input_string)
else:
    return False, 0.0, “”

def Reader(intent_id, input_text):
    # pull intent tree from Intent Graph Database
    intent_tree_page = query(intent_graph_db, intent_id)
    intent_tree = convert_to_binary_tree(intent_tree_page)

    # traverse tree
    stack = []
    root = intent_tree[0]
    current = root
    tree_input = input_text
    while True:
        if current is not None:
            result, raw_score, result_text = Caller(current.type, current.input, tree_input)
            if result:
                if current.left == None and current.right == None:
                    return True
                if current.link:
                    tree_input = result_text
                else:
                    tree_input = input_text
                stack.append(current)
                current = current.left
            else:
                current = None
        elif (stack):
            current = stack.pop()
            current = current.right
        else:
            return False


