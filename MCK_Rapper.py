from MCK_NLP import MCK_Structure
import nltk
import requests
class Rapper():
    def __init__(
        self,
        structure_model,
        theme
        ):
        self.structure_model = structure_model
        self.theme = theme
        self.freestyle = []
    def get_next_word(self):
        if len(self.freestyle) == 0:  
            last_word = ""
        else:
            last_word = self.freestyle[-1]
        related_word_url = "https://api.datamuse.com/words?ml={0}".format(self.theme)
        if last_word:
            related_word_url = related_word_url + "&rel_rhy=" + last_word
        response = requests.get(related_word_url)
        related_word_theme = response.json()
        related_word_array = []
        for item in related_word_theme:
            related_word_array.append(item["word"])
        return related_word_array

if __name__ == "__main__":
    theme = input("Pick your theme: ")
    structure = MCK_Structure.Structure("copora/MGKmodLyrics.txt")
    rap = Rapper(structure, theme)
    print(rap.get_next_word())
    