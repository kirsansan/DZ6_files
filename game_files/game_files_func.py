class BasicWords:
    words: list = []

    def __init__(self, lst: list = []):
        self.words = lst

    def __repr__(self) -> str:
        out: str = " ".join(self.words)
        return out

    def read_words_from_file(self, filename):
        # f = open(filename, 'r')
        # while f.readline():
        #     self.words.append()
        with open(filename, 'r') as f:
            self.words = f.read().splitlines()
        f.close()

# this block for a self-test
if __name__ == '__main__':
        # easy words fill and print
        some_words = BasicWords()
        some_words.words = ['abc', 'def']
        print(some_words)

        # read from file and print
        some_words.read_words_from_file('./words.txt')
        print(some_words)