from bytesized import ByteSized


def request_data():  # not needed and can be moved out of this interface.  leaving it here for testing
    return input("Please enter values.\n")


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
        formatted_data = request_data()
        a = ByteSized(formatted_data)
        print(data_to_str(a.results()))
    except TypeError as e:
        print(e)
        print("This might be due to invalid input")
    except UnboundLocalError as e:
        print(e)
        print("You may have started with a number instead of a bytesize")


if __name__ == "__main__":
    main()
