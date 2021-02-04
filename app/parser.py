import json

list_spec = [",",
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
bad_word = ['bonjour', 'connait', 'adresse']



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

    def parser(self, string: str) -> str:
        """
        parse str
        :return:stringer parsed
        """

        data_json: list
        file_json = "app/word_fr.json"
        with open(file_json) as json_file:
            data = json.load(json_file)
            data_json = data
        words = string.split(' ')

        list_word_parsed = []
        for word in words:
            if word == "" or word.isdigit():
                continue

            if word[len(word) - 1] in list_spec:
                word = word[:len(word) - 1]
            if len(word) > 1:
                if word[1] == "'":
                    word = word[2:]
            word_lower = word.lower()
            if word_lower in data_json or word_lower in bad_word or word_lower == "":
                continue

            list_word_parsed.append(word.rstrip())

        string_parsed = " ".join(list_word_parsed)
        return string_parsed


if __name__ == "__main__":
    p = Parser()
    p.parser("(--èè_--è:; bonjour")
