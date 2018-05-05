import re


string = "1000"

ret = 2000
assert ret < int(re.findall(r"\b\d+\b", string)[0]), "not true!"
