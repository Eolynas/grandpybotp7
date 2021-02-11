""" this module takes care of the wiki api """
import json


class Parser:
    """
    Class to parse the user's question
    """

    def __init__(self):
        """
        Constructor for Substitut
        """
        self.path_file = "app/static/word_fr.json"
        self.list_spec = [
            ",",
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
            '"',
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
            "}",
        ]
        self.bad_word = ["bonjour", "connait", "adresse"]

        self.data_json = []
        self.loading_json(file=self.path_file)

    def loading_json(self, file: str):
        """
        load json with word fr
        :return:
        """
        with open(file) as json_file:
            data = json.load(json_file)
            self.data_json = data

    def parser(self, string: str) -> str:
        """
        parse str
        :return:stringer parsed
        """

        words = string.split(" ")

        list_word_parsed = []
        for word in words:
            if word == "" or word.isdigit():
                continue

            if word[len(word) - 1] in self.list_spec:
                word = word[: len(word) - 1]
            if len(word) > 1:
                if word[1] == "'":
                    word = word[2:]
            word_lower = word.lower()
            if (
                word_lower in self.data_json
                or word_lower in self.bad_word
                or word_lower == ""
            ):
                continue

            list_word_parsed.append(word.rstrip())

        string_parsed = " ".join(list_word_parsed)
        return string_parsed
