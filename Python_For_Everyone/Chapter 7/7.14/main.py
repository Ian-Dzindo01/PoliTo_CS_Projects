import requests

r = requests.get('https://every.sdf.org/Comestibles/potables/heavenly_beer.txt')

filepath = "C:/Users/iandz/OneDrive/Desktop/Faks/CS/Lab/Python_For_Everyone/Chapter 7/7.14/"

x = input("Please enter the name of the file where you want the text stored: ")

fw = open(filepath+x, 'w')
fw.write(r.text)
fw.close()


