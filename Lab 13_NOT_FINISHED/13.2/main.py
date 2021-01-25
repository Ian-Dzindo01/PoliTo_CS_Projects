txt1 = open('result1.txt').read()
txt2 = open('result2.txt').read()
txt3 = open('result3.txt').read()

if txt1 == txt2 == txt3:
    print("Brao mali")
else:
    print("Ne valja")


