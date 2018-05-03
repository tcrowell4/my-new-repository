msg = []
msg.append("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ")
msg.append("ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq ")
msg.append("rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ")
msg.append("ynnjw ml rfc spj.")

alpha = "abcdefghijklmnopqrstuvwxyz"
cipher = "cdefghijklmnopqrstuvwxyzab"
trantab = str.maketrans(alpha,cipher)

print("original msg\n", msg, "\n\n")

for line in msg:
    #print(line)
    print(line.translate(trantab))

url ="http://www.pythonchallenge.com/pc/def/map.html"
print("\n\n", url.translate(trantab))

""" the output 
jvvr://yyy.ravjqpejcnngpig.eqo/re/fgh/ocr.jvon
the ocr is the important part
"""
