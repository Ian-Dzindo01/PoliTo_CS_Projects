fr = open('input.txt', 'r')
text = fr.read()
fr.close()

newtext = ''

for i, line in enumerate(text.splitlines()):
    newtext += '/*' + str(i) + '*/' + str(line)
    newtext += '\n'

fw = open('output.txt', 'w')
fw.write(newtext)
fw.close()
