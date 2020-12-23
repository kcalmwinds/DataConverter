import functools

_VALID_COMMANDS = frozenset({"b", "p", "k", "m", "g", "t", "pb", "help"})


def b_to_pages(num, *, reverse=False, power=-1):
    return (num * 1024 ** power) / 8 if not reverse else (num * 8) / 1024 ** power


conversions = {"b": b_to_pages, "p": lambda num, **kwargs: num}
for power, scale in enumerate(["k", "m", "g", "t", "pb"]):
    conversions[scale] = functools.partial(b_to_pages, power=power)

del power, scale


class ByteSize:
    """Format your input:
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
            [dict]: [Contains input_types : Float pairing of byte sizes]
    """

    def __init__(self, data, valid_args):
        self.prep = {"p": []}
        self.pages = 0
        self.data = data
        self.valid = valid_args

    # data cleaning
    def is_help(self):
        return

    def is_quit(self):
        return False

    def detect_zero_sum(self):
        for k, v in self.prep.items():
            if k == "p":
                continue
            elif sum(v) == 0:
                return "Zero sum detected. Cannot divide by zero."

    def validate_input(self):
        for x in self.data:
            if type(x) == str:
                if x.lower() in self.valid:
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
        self.validate_input()
        self.sum_input()
        self.convert_to_pages()
        self.add_to_pages()
        self.recalculate_values()
        return self.prep


def request_data():
    return input('Please enter values or type "help" for help\n')


def format_data(data):
    try:
        return [x if x.lower() in _VALID_COMMANDS else float(x) for x in data.split()]
    except ValueError:
        print("Invalid input")


def data_to_str(data):
    return f"""
Results
============
Bytes : {data['b']}
Pages : {data['p']}
Kilobytes : {data['k']}
Megabytes : {data['m']}
Gigabytes : {data['g']}
Terabytes : {data['t']}
Petabytes : {data['pb']}

"""


def main():
    try:
        formatted_data = format_data(request_data())
        a = ByteSize(formatted_data, _VALID_COMMANDS)
        print(data_to_str(a.results()))
    except TypeError as e:
        print(e)
        print("This might be due to invalid input")
    except UnboundLocalError as e:
        print(e)
        print("You may have started with a number instead of a bytesize")


if __name__ == "__main__":
    main()
