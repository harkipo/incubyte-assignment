class StringCalculator():

    DELIMITER = ","

    def add(self, string):
        if string == "":
            return 0
        else:
            return self.add_numbers(string)

    def add_numbers(self, string):
        return sum(self.extract_numbers_from(string))

    def extract_numbers_from(self, string):
        return [self.parse_number(number) for number in self.split_on_delimiters(string)]

    def parse_number(self, number):
        if "-" in number:
            raise ValueError("Rejecting negative number")
        return int(number)

    def split_on_delimiters(self, string):
        return self.normalize_delimiters(string).split(self.DELIMITER)

    def normalize_delimiters(self, string):
        normalized = string
        normalized = self.handle_custom_delimiter(normalized)
        normalized = normalized.replace("\n", self.DELIMITER)
        return normalized

    def handle_custom_delimiter(self, string):
        if string.startswith("//"):
            custom, rest = string.split("\n", 1)
            return rest.replace(custom[2:], self.DELIMITER)
        return string