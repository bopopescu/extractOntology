from gensim.models import Word2Vec
import gensim
import logging
import gzip
# define training data

def read_input(input_file):
    """This method reads the input file which is in gzip format"""
 
    logging.info("reading file {0}...this may take a while".format(input_file))
    with gzip.open(input_file, 'rb') as f:
        for i, line in enumerate(f):
            if (i % 10000 == 0):
                logging.info("read {0} reviews".format(i))
            # do some pre-processing and return list of words for each review
            # text
            yield gensim.utils.simple_preprocess(line)
sentences = read_input('home/kang/Downloads/Papers.txt.gz')

print('WHERE IS MU DATA')
print(sentences)
# train model
model = Word2Vec(sentences, size=229,window=5,min_count=5,workers=4)
# summarize the loaded model
print(model)
# summarize vocabulary
words = list(model.wv.vocab)
print(words)
# access vector for one word
print(model['sentence'])
# save model
model.save('model.p')
# load model
new_model = Word2Vec.load('model.p')
print(new_model)