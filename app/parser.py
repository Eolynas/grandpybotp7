import json


class Parser:
    """
    # TODO
    """

    def __init__(self):
        """
        Constructor for Substitut
        """
        self.list_spec = [",",
                          "?",
                          ";",
                          ".",
                          ":",
                          "/",
                          "!",
                          "§",
                          "ù",
                          "*",
                          "%",
                          "µ",
                          "^",
                          "$",
                          "&",
                          "é",
                          "\"",
                          "'",
                          "(",
                          "-",
                          "è",
                          "_",
                          "_",
                          "ç",
                          "à",
                          ")",
                          "=",
                          "~",
                          "#",
                          "{",
                          "[",
                          "|",
                          "`",
                          "^",
                          "@",
                          "]",
                          "]",
                          "}",]
        self.bad_word = ['bonjour', 'connait', 'adresse']

    def loading_json(self, file: str):
        """
        load json with word fr
        :return:
        """
        pass

    def parser(self, string: str) -> list:
        """
        parse str
        :return:
        """

        data_json: list
        file_json = "/home/eddy/PycharmProjects/project_7/app/word_fr.json"
        with open(file_json) as json_file:
            data = json.load(json_file)
            data_json = data
        words = string.split(' ')

        list_word_parsed = []
        for word in words:
            if word == "" or word.isdigit():
                continue

            word = word.lower()
            if word[len(word) - 1] in self.list_spec:
                word = word[:len(word) - 1]
            if word[1] == "'":
                word = word[2:]
            # if not word in data_json and not word in self.bad_word:
            #     print(f"le mot {word} n'est pas dans les deux list")
            if word in data_json or word in self.bad_word or word == "":
                continue

            list_word_parsed.append(word.rstrip())

        print(list_word_parsed)
        return list_word_parsed


if __name__ == "__main__":
    p = Parser()
    p.parser("(--èè_--è:; bonjour")
