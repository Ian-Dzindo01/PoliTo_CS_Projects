import requests

link = "https://www.cia.gov/library/publications/the-world-factbook/rankorder/rawdata_2004.txt"

f = requests.get(link).text

d = {}

for line in f.splitlines():
    line = line.strip()
    key = (line[7:-8]).strip()
    val = line[-9:].strip()
    d[key] = val

x = input("Please enter the name of the country you are interested in: \n")
print(d[x])

# Note that the names of some countries in the provided link are wrong.
