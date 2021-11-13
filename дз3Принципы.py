class Text:
    def __init__(self, text):
        self.__text = text

    def paragraph(self):
        paragraph = self.__text.split("/")
        for i in range(len(paragraph)):
            print(paragraph[i])

    def str(self):
        paragraph = self.__text.split("/")
        for i in range(len(paragraph)):
            print(i + 1)

    def number(self, number):
        paragraph = self.__text.split("/")
        # for number in range(len(paragraph))
        print(paragraph[number - 1])

    def value(self, number):
        paragraph = self.__text.split("/")
        sgt = paragraph[number - 1]
        worlds = sgt.split()
        return len(worlds)

    def word(self, number, slovo):
        paragraph = self.__text.split("/")
        sgt = paragraph[number - 1]
        worlds = sgt.split()
        slovo = worlds[slovo - 1]
        return str(slovo)


text = input()
numer = int(input())
word = int(input())
c = Text(text)
print(c.paragraph(), c.str(), c.number(numer), c.value(numer), c.word(numer, word))
