class BasicWords:
    words: list[str] = []

    def __init__(self, lst: list[str] = []):
        self.words = lst

    def __repr__(self) -> str:
        """ return all words as one string"""
        out: str = " ".join(self.words)
        return out

    def read_words_from_file(self, filename):
        """ read words from file. FORMAT IS: one line - one word"""
        # f = open(filename, 'r')
        # while f.readline():
        #     self.words.append()
        with open(filename, 'r') as f:
            self.words = f.read().splitlines()
        f.close()


def print_headers_around_some_text(func):
    def wrapper():
        print("=== we will test you ===")
        func()
        print("=== we have just done all test ===")
    return wrapper


@print_headers_around_some_text
def test():
    # at this test  words just read and print/check
    some_words = BasicWords()
    try:
        # some_words.words = ['abc', 'def']
        # print(some_words)

        # read from file and check
        some_words.read_words_from_file('./words.txt')
        # print(some_words)
        for x in some_words.words:
            assert x in ["python", "squirrel", "flask", "cucumbers"]
    except AssertionError:
        print("You have errors, check your functions")
    else:
        print("Ok. All test passed")


# this block for a self-test
if __name__ == '__main__':
    test()
