class DataConvert:

    def __init__(self, data, valid_args):
        self.prep = {'p': []}
        self.pages = 0
        self.data = data
        self.valid = valid_args

    # set up conversions to pages and back

    def b_to_pages(self, num, reverse=False):
        if reverse == False:
            return (num / 1024) / 8
        elif reverse == True:
            return (num * 8) * 1024

    def k_to_pages(self, num, reverse=False):
        if reverse == False:
            return num / 8
        elif reverse == True:
            return num * 8

    def m_to_pages(self, num, reverse=False):
        if reverse == False:
            return self.k_to_pages(num * 1024)
        elif reverse == True:
            return (num * 8) / 1024

    def g_to_pages(self, num, reverse=False):
        if reverse == False:
            return self.k_to_pages(num * 1024**2)
        elif reverse == True:
            return (num * 8) / 1024**2

    def t_to_pages(self, num, reverse=False):
        if reverse == False:
            return self. k_to_pages(num * 1024**3)
        elif reverse == True:
            return (num * 8) / 1024**3

    def pb_to_pages(self, num, reverse=False):
        if reverse == False:
            return self.k_to_pages(num * 1024**4)
        elif reverse == True:
            return (num * 8) / 1024**4

    # data cleaning
    def is_help(self):
        if 'help' in self.prep.keys():
            return '''Format your input:  
Input_type num num num Input_type num num num...

Input_Types
-----------
p = pages
k = kilobytes
m = megabytes
g = gigabyte
t = terabyte

quit = quit
help = help
'''

    def is_quit(self):
        return False

    def detect_zero_sum(self):
        for k, v in self.prep.items():
            if k == 'p':
                continue
            elif sum(v) == 0:
                return 'Zero sum detected. Cannot divide by zero.'

    def validate_input(self):
        for x in self.data:
            if type(x) == str:
                if x.lower() in self.valid:
                    hold = x.lower()
                    if hold == 'quit':
                        return self.is_quit()
                    elif hold == 'help':
                        print(self.is_help())
                        return 1, 'Restarting'
                    elif hold not in self.prep.keys():
                        self.prep[hold] = []
            elif type(x) == float:
                self.prep[hold].append(x)
            else:
                return 0, 'Invalid input.'
        detect_zeros = self.detect_zero_sum()
        if detect_zeros is not None:
            return detect_zeros

    def sum_input(self):
        for k in self.prep.keys():
            self.prep[k] = sum(self.prep[k])

    # calculate all self.prep.values() to pages

    def convert_to_pages(self):
        for k in self.prep.keys():
            if k == 'b':
                self.prep[k] = self.b_to_pages(self.prep[k])
            elif k == 'k':
                self.prep[k] = self.k_to_pages(self.prep[k])
            elif k == 'm':
                self.prep[k] = self.m_to_pages(self.prep[k])
            elif k == 'g':
                self.prep[k] = self.g_to_pages(self.prep[k])
            elif k == 't':
                self.prep[k] = self.t_to_pages(self.prep[k])
            elif k == 'pb':
                self.prep[k] = self.pb_to_pages(self.prep[k])

    def add_to_pages(self):
        total_pages = 0
        for v in self.prep.values():
            total_pages += v
        self.prep['p'] = total_pages

    def recalculate_values(self):
        self.prep['b'] = self.b_to_pages(self.prep['p'], True)
        self.prep['k'] = self.k_to_pages(self.prep['p'], True)
        self.prep['m'] = self.m_to_pages(self.prep['p'], True)
        self.prep['g'] = self.g_to_pages(self.prep['p'], True)
        self.prep['t'] = self.t_to_pages(self.prep['p'], True)
        self.prep['pb'] = self.pb_to_pages(self.prep['p'], True)

    def results(self):
        self.validate_input()
        self.sum_input()
        self.convert_to_pages()
        self.add_to_pages()
        self.recalculate_values()
        return self.prep


class Application:
    def __init__(self):
        self.valid = ['b', 'p', 'k', 'm', 'g',
                      't', 'pb', 'help', 'quit', int, float]

    def request_data(self):
        return input('Please enter values or type "help" for help\n')

    def format_data(self, data, valid_args):
        listify = data.split()
        for x in listify:
            if x.lower() in self.valid:
                continue
            elif x not in self.valid:
                try:
                    listify[listify.index(x)] = float(x)
                except:
                    print('Invalid input')
                    break
        return listify

    def return_str(self, data):
        print('''
Results
============
Bytes : {0[b]}
Pages : {0[p]}
Kilobytes : {0[k]}
Megabytes : {0[m]}
Gigabytes : {0[g]}
Terabytes : {0[t]}
Petabytes : {0[pb]}

'''.format(data))

    def run_it(self):
        a = DataConvert(self.format_data(
            self.request_data(), self.valid), self.valid)
        return self.return_str(a.results())


if __name__ == '__main__':
    running = True
    while running == True:
        a = Application()
        b = a.run_it()
        if b == False:
            running = False
