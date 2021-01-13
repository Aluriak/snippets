from io import StringIO
from contextlib import redirect_stdout

output = StringIO()
with redirect_stdout(output):
    print('hello, world!', end='')
assert output.getvalue() == 'hello, world!'
