from subprocess import Popen, PIPE


class Repl(object):

    def __init__(self, bin):
        self.process = Popen(bin, stdin=PIPE, stdout=PIPE, stderr=PIPE)

    def write(self, text):
        self.process.stdin.write(text.encode("utf-8"))
        self.process.stdin.flush()

    def read(self):
        return self.process.stdout.readline().decode("utf-8").strip()

    def close(self):
        self.process.terminate()


repl = Repl(['python', '-i'])
print(repl.read())
