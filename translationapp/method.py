from googletrans import Translator, LANGUAGES
print(LANGUAGES)
class thetranslator:
    def __init__(self):
        self.languageoptions = list(LANGUAGES.values())
    def run(self,txt="type text down here",src="english",dest="id"):
        self.translator = Translator()
        self.txt = txt
        self.src = src
        self.dest = dest
        try:
            self.translated = self.translator.translate(self.txt,src=self.src,dest=self.dest)
        except:
            self.translated = self.translator.translate(self.txt)
        self.ttext = self.translated.text
        return self.ttext

