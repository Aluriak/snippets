


import tempfile

with tempfile.NamedTemporaryFile(mode='w', delete=False) as fd:
    tmpname = fd.name
    fd.write('data')
with open(tmpname) as fd:
    data = fd.read()
os.unlink(tmpname)
