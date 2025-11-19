#!/usr/bin/python3
def best_score(a_dictionary):
    try:
        max_score = max(i for i in a_dictionary.values())
        inverted_dict = {val: key for key, val in a_dictionary.items()}
        return inverted_dict[max_score]
    except:
        return None
