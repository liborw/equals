from subprocess import Popen, PIPE


test_code = """
1 + 1 #=
a = 1
b = 1 + a #=
"""


class Repl(object):

    def __init__(self, bin):
        self.process:Popen = Popen(bin, stdin=PIPE, stdout=PIPE, stderr=PIPE)

    def write(self, text):
        self.process.stdin.write(text.encode("utf-8"))
        self.process.stdin.flush()

    def read(self):
        return self.process.stdout.readline().decode("utf-8").strip()

    def close(self):
        self.process.terminate()


repl = Repl(['/usr/bin/env', 'python', '-i'])
print(repl.read())

#%% using script command

process = Popen(['script', '-qfec', 'python', '/dev/null'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
stdout, _ = process.communicate(test_code.encode())

print(stdout.decode())

