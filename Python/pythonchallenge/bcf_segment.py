import fileinput
import re

segments = []
member = "member interface-group kstopcobxp-rc718001_02-vdc3-po159 vlan %s"

for line in fileinput.input():
    if "segment" in line:
        segments.append(line.strip())

print(segments)
for line in segments:
    match = re.search(r'-(\d+)$', line)
    if match:
        print(line)
        print(member % match.group(1))


