class Players:
    """
    include data about players in format of list with dict
    [ {glogal_try:<try int>, name:<name string>, score:<score int>}, {...}, {...}  ] """
    name_and_score: list[dict[int:, str:, int:]] = []

    def __init__(self):
        self.name_and_score = []

    def __repr__(self) -> str:
        """ we shall return all what we know """
        out: str = ""
        for element in self.name_and_score:
            out += str(element['global_try']) + ' ' + element['name'] + ' ' + str(element['score']) + ';'
        return out

    def read_history_from_file(self, filename):
        """ read lines from file and fill structure of self.name_and_score
        file format is <name><space><score> in each line without anything else
        """
        iterator = 0
        # my_str: str = ""
        file_object = open(filename, 'r', encoding='utf-8')
        self.name_and_score = []
        while True:
            my_str = file_object.readline()
            if not my_str:
                break
            my_str = my_str.rstrip('\n')

            # so we will mark records with human-style (from 1), if we found 0 somewhere, it would mean error
            iterator += 1
            # print(iterator, my_str, end='')
            self.name_and_score.append({"global_try": iterator,
                                        "name": my_str.split(' ')[0],
                                        "score": int(my_str.split(' ')[1])})
        #  second short method for work with files
        # with open(filename, 'r') as f:
        #    self.name_and_score[] = f.read().splitlines()
        file_object.close()

    def get_statistic(self) -> dict[str:, str:]:
        """ return name and best result as a mini-dictionary"""
        best_result: int = 0
        # name_for_best_result: str = ""
        i_am_name_for_out: str = ""
        for element in self.name_and_score:
            if element['score'] > best_result:
                i_am_name_for_out = (element['name'])
                # i_am_list_for_out.append(str(element['score']))
                best_result = element['score']
        return {'name': i_am_name_for_out, 'score': str(best_result)}

    def put_new_player_2_file(self, filename: str = "tmp.txt", name: str = "", score: int = 0) -> bool:
        """ this func may be static but i am going add filename as variable of self class in future"""
        file_object = open(filename, 'a', encoding='utf-8')
        # print(file_object)
        if file_object.writable():
            file_object.write(f"{name} {str(score)}\n")
            file_object.close()
            return True
        return False

    def get_length(self) -> int:
        """ just return length of data list"""
        return self.name_and_score.__len__()


# this block for a self-test
if __name__ == '__main__':
    test_player = Players()
    test_player.name_and_score = [{"global_try": 1, "name": "Lelik", "score": 20},
                                  {"global_try": 2, "name": "Bolik", "score": 30}]
    print(test_player)

    tmp_list = test_player.get_statistic()
    # print(tmp_list)
    print(tmp_list['name'], tmp_list['score'])   # wait for "Bolik 30"

    test_player.read_history_from_file('./history.txt')
    print(test_player)  # wait for some string from __repr__()

    test_player.put_new_player_2_file('./temp.txt', 'Krolik', 15)  # put one more white rabbit to the test file
