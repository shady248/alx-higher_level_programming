#!/usr/bin/python3
def multiple_returns(sentence):
    len_sn = len(sentence)

    if (len_sn == 0):
        new_tuple = (len_sn, None)
    else:
        new_tuple = (len_sn, sentence[0])

    return (new_tuple)
