import numpy as np
import nltk.corpus 
import random
import pandas as pd
import statistics

corp = nltk.corpus.gutenberg.raw('austen-sense.txt')
corpus = nltk.word_tokenize(corp.lower())
#corpus = corp[:500]
#sentence = ['she', 'was', 'not']

def main(sentence, n, corpus):
    find = sentence[-(n-1):]
    dict = {}
    for i in range(len(corpus) - n + 1):
        if find in [corpus[i:i+(n-1)]]:
            if corpus[i+(n-1)] in dict:
                dict[corpus[i+(n-1)]] += 1
            else:
                dict[corpus[i+(n-1)]] = 1
                pass
            pass
    return dict

def find_word(sentence, n, corpus):
    ans = {}
    for i in reversed(range(1, n+1)):
        if i > 1 and ans == {}:
            ans = main(sentence, i, corpus)
        elif i == 1 and ans == {}:
            ans[statistics.mode(corpus)] = 1
    df = pd.DataFrame(list(ans.items()), columns= ['word', 'count'])
    df['prob'] = df['count']/df['count'].sum()
    c = df.loc[df['prob'] == df['prob'].max()]
    return c.iloc[0,0]

def finish_sentence(sentence, n, corpus, deterministic):
    while len(sentence) < 15 and (sentence[-1] != '.' and sentence[-1] != '?' and sentence[-1] != '!'):
        if deterministic:
            new_word = find_word(sentence, n, corpus)
            sentence.append(new_word)
        else:
            new_word = np.random.choice(corpus)
            sentence.append(new_word)
    return sentence
        

#find = ['Get', 'out']
#print(finish_sentence(find, 4, corpus, deterministic=False))






        




