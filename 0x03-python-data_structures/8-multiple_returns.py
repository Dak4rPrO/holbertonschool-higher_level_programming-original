#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return sentence(0, None)
    return len(sentence), sentence[0]
