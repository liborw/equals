import subprocess



process = subprocess.Popen(
        ['python'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
)

stdout, stderr = process.communicate()
print('out:', repr(stdout.decode()), repr(stderr.decode()))

