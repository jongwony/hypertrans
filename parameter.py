class TransParam:

    def __init__(self):
        self.url = 'https://translate.google.com'
        self.src = 'en'
        self.dst = 'ko'
        self._sentence = ''

    def set_sentence(self):
        self._sentence = input(self.src + '->' + self.dst + ': ')
        return self._sentence

    def build_params(self):
        params = {
            'sl': self.src,
            'tl': self.dst,
            'oe': 'UTF-8',
            'q': self._sentence,
        }
        return params

    def swap(self, result):
        self.src, self.dst = self.dst, self.src
        self._sentence = result

    def custom(self):
        source = input('Source Language: ')
        assert len(source) < 5, "Write ISO-639-1 Code, https://cloud.google.com/translate/docs/languages"
        if source is not '':
            self.src = source

        destination = input('Destination Language: ')
        assert destination is not '', "Specify destination language."
        assert len(destination) < 5, "Write ISO-639-1 Code, https://cloud.google.com/translate/docs/languages"
        self.dst = destination

