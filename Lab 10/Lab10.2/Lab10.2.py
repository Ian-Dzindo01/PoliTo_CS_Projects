fr = open('input.txt', 'r')
text = fr.read()
fr.close()

newtext = ''

for i, line in enumerate(reversed((text.splitlines()))):
    newtext += line
    newtext += '\n'

fw = open('output.txt', 'w')
fw.write(newtext)
fw.close()
