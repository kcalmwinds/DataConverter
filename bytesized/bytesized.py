import functools

_VALID_COMMANDS = frozenset({"b", "p", "k", "m", "g", "t", "pb"})


def b_to_pages(num, *, reverse=False, power=-1):
    return (num * 1024 ** power) / 8 if not reverse else (num * 8) / 1024 ** power


conversions = {"b": b_to_pages, "p": lambda num, **kwargs: num}
for power, scale in enumerate(["k", "m", "g", "t", "pb"]):
    conversions[scale] = functools.partial(b_to_pages, power=power)

del power, scale


class ByteSized:
    """Format your input as a list of strings:

    Input_type num num num Input_type num num num...

    Input_Types
    -----------
    p = pages
    k = kilobytes
    m = megabytes
    g = gigabyte
    t = terabyte
    pb = petabyte

        Returns:
            dict: Contains input_types : Float pairing of byte sizes
    """

    def __init__(self, data):
        """Setting this up needs valid byte sizes. We declared that above at the top of the file with _VALID_COMMANDS
        the conversions dict should update as you add in more to the scale variable.

        Args:
            data (List): This should be a list of strings starting with something from _VALID_COMMANDS followed by numbers formatted as strings
            valid_args (frozenset): This is declared at the top of this document and should be passed in
        """
        self.prep = {"p": []}
        self.pages = 0
        self.data = self.format_data(data)

    # data cleaning
    def format_data(self, data):
        try:
            return [
                x if x.lower() in _VALID_COMMANDS else float(x) for x in data.split()
            ]
        except ValueError:
            print("Invalid input")

    def detect_zero_sum(self):
        for k, v in self.prep.items():
            if k == "p":
                continue
            elif sum(v) == 0:
                return "Zero sum detected. Cannot divide by zero."

    def validate_input(self):
        for x in self.data:
            if type(x) == str:
                if x.lower() in _VALID_COMMANDS:
                    hold = x.lower()
                    if hold not in self.prep.keys():
                        self.prep[hold] = []
            elif type(x) == float:
                self.prep[hold].append(
                    x
                )  # hold comes from a previous iteration of the loop
            else:
                print("Invalid input.")
        detect_zeros = self.detect_zero_sum()
        if detect_zeros is not None:
            return 1, detect_zeros

    def sum_input(self):
        for k in self.prep.keys():
            self.prep[k] = sum(self.prep[k])

    # calculate all self.prep.values() to pages

    def convert_to_pages(self):
        for k in self.prep:
            self.prep[k] = conversions[k](self.prep[k])

    def add_to_pages(self):
        total_pages = 0
        for v in self.prep.values():
            total_pages += v
        self.prep["p"] = total_pages

    def recalculate_values(self):
        for k, convert in conversions.items():
            self.prep[k] = convert(self.prep["p"], reverse=True)

    def results(self):
        try:
            self.validate_input()
            self.sum_input()
            self.convert_to_pages()
            self.add_to_pages()
            self.recalculate_values()
            return self.prep
        except TypeError as e:
            print(e)
            print("This might be due to invalid input")
        except UnboundLocalError as e:
            print(e)
            print("You may have started with a number instead of a bytesize")
