from io import StringIO
from contextlib import redirect_stdout

output = StringIO()
with redirect_stdout(output):
    print('hello, world!', end='')
assert output.getvalue() == 'hello, world!'



class PrintAndAcc():
    "Replacement for io.StringIO() instance where stdout is both accumulated and printed in real time in stdout"
    def __init__(self, target=sys.stdout):
        self.content = []
        self.target = target
    def write(self, content):
        print(content, end='', file=self.target)
        self.content.append(content)  # avoid O2 complexity
    def getvalue(self):
        return ''.join(self.content)

acc = PrintAndAcc()
with contextlib.redirect_stdout(acc):
    print('test')
assert acc.getvalue() == 'test'

