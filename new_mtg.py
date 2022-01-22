import numpy as np
import nltk.corpus 
import random
import pandas as pd

corp = nltk.corpus.gutenberg.raw('austen-sense.txt')
corpus = nltk.word_tokenize(corp.lower())
#corpus = corp[:500]
#sentence = ['she', 'was', 'not']

def main(sentence, n, corpus):
    find = sentence[-(n):]
    dict = {}
    for i in range(len(corpus) - n):
        if find in [corpus[i:i+n]]:
            if corpus[i+(n)] in dict:
                dict[corpus[i+(n)]] += 1
            else:
                dict[corpus[i+(n)]] = 1
                pass
            pass
    return dict

def find_word(sentence, n, corpus):
    ans = {}
    for i in reversed(range(1, n+1)):
        if i > 1 and ans == {}:
            ans = main(sentence, i, corpus)
        elif i == 1 and ans == {}:
            ans[np.random.choice(corpus)] = 1
    df = pd.DataFrame(list(ans.items()), columns= ['word', 'count'])
    df['prob'] = df['count']/df['count'].sum()
    #return df
    return df.iloc[0, 0]

def finish_sentence(sentence, n, corpus, deterministic):
    while len(sentence) < 15 and (sentence[-1] != '.' and sentence[-1] != '?' and sentence[-1] != '!'):
        if deterministic == True:
            new_word = find_word(sentence, n, corpus)
            sentence.append(new_word)
        else:
            new_word = np.random.choice()
            sentence.append(new_word)
    return sentence
        

find = ['she', 'was', 'not']
print(finish_sentence(find, 3, corpus, deterministic=True))






        




