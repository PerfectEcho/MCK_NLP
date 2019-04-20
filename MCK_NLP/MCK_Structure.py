import nltk
import string

class Structure():
    def __init__(
        self,
        corpus = "copora/MGKmodLyrics.txt"
        ):
        with open(corpus, "r") as corpusReader:
            self.corpus = corpusReader.read().replace("'","")
        tokenized_words = [word for word in nltk.word_tokenize(self.corpus) if word not in string.punctuation]
        tagged_words = nltk.pos_tag(tokenized_words)
        tagged_array = []
        for tag in tagged_words:
            tagged_array.append(tag[1])
        biPairtags = list(nltk.bigrams(tagged_array))
        super_dict = {}

        for pair in biPairtags:
            if pair[0] in super_dict:
                if pair[1] in super_dict[pair[0]]:
                    super_dict[pair[0]][pair[1]] += 1
                else:
                    super_dict[pair[0]][pair[1]] = 1
            else:
                super_dict[pair[0]] = {}
                super_dict[pair[0]][pair[1]] =1
        
        self.structure = super_dict

    def get_type(self, prev_type):
        self.structure[prev_type] = sorted(self.structure[prev_type].items(), key=lambda item: item[1], reverse = True)
        return self.structure[prev_type][0][0]
    def get_structure(self):
        return self.structure