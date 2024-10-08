import nltk
import pandas as pd
from nltk import hmm

# nltk.download('popular')

#reading dataset from tsv file
dataset = pd.read_table('util/Indonesian_Manually_Tagged_Corpus.tsv', header=None, names=['words','tags'])

#counting how much tags in dataset
counted = dataset['tags'].value_counts()

#most 10 frequent tags
print('10 most frequent tags:', counted.head(10), sep='\n')

#top 10 words with NN tags
NN_tagged = dataset[dataset['tags']=='NN']
NN_counted = NN_tagged['words'].value_counts()
print('\n10 most frequent words given NN tag:', NN_counted.head(10), sep='\n')

#words with multiple tags
grouped_by_word = dataset.groupby('words')['tags'].unique()
word_and_mt1_tags = grouped_by_word[grouped_by_word.apply(lambda x: len(x)>1)]
print('\nWords and more than 1 tags with all tags:', word_and_mt1_tags.sample(5), sep='\n')

def c_list_of_sentences(low, sep):
    sentence = []
    sentences = []
    for word in low:
        sentence.append(word)
        if word == sep:
            sentences.append(sentence)
            sentence = []
    return sentences

#variable for processing
list_of_words = dataset.to_records(index=False).tolist()
sep = ('.', 'Z')

#list of datatraining (format in tuple)
train_data = c_list_of_sentences(list_of_words, sep)

#train model with HMM algorithm
trainer=hmm.HiddenMarkovModelTrainer()

#creating pos tag model
tagger=trainer.train_supervised(train_data)

def get_tag(sentence: str):
    sentence = remove_dots(sentence)
    return tagger.tag(sentence.lower().split())

def remove_dots(sentence: str) -> str:
    return sentence.replace('.', '')

def categorize_insight(tokens: []):
    result = []
    for token in tokens:
        if token[1] == 'JJ':
            result.append(token)
    return result

def distinct_insight(words: []):
    return set(words)