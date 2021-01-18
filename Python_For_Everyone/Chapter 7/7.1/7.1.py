fw = open('hello.txt', 'w')
fw.write("Hello, World!")
fw.close()

text = open('hello.txt', 'r').read()
print(text)
