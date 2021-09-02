import selenium
import csv
import os
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# alphabet data structure
alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# creates list of integers each representing the number of times a corresponding letter shows up in provided text
def counteachletter(text):
    letterdistribution = []
    textlower = text.lower()
    for letter in alpha:
        letterdistribution.append(textlower.count(letter))
    return letterdistribution

# gets the content from my author blog 
url = "http://www.theworldofthomerion.com"
res = requests.get(url)
html = res.content
soup = BeautifulSoup(html, 'html.parser')
text = soup.find_all(text=True)

output = ''
blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head', 
    'input',
    'script'
]

# extracts most of the blog content that wouldn't be considered relevant body text
for t in text:
    if t.parent.name not in blacklist:
        output += '{} '.format(t)

# generate a list of the frequency of each letter in my author blog
distribution = counteachletter(output)

f, ax = plt.subplots(1, 1, figsize=(7, 5), sharex=True)

# creates a bar graph using the data generated above
x = np.array(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
y1 = np.array(distribution)
sns.barplot(x=x, y=y1, palette="rocket", ax=ax)
ax.axhline(0, color="k", clip_on=False)
ax.set_ylabel("Letter Frequency")

sns.despine(bottom=True)
plt.setp(f.axes)
plt.tight_layout(h_pad=2)

# writes the generated numerical data to a CSV file
for number in distribution:
    file = open("letteranalysis.csv", "w", newline='')
    with file:
        writer = csv.writer(file)
        writer.writerow(distribution)

file.close()

# opens the blog's contact page in a Chrome browser and prepares to email author an alert

# the pushing of the button is commented out because I don't want to receive spam every time this script is run :-)

driver = webdriver.Chrome()

driver.get('http://www.theworldofthomerion.com/contact/')

namebox = driver.find_element_by_name('g3-name')
namebox.send_keys("Daniel Heck")

emailbox = driver.find_element_by_name('g3-email')
emailbox.send_keys("danielheck@danielheck.com")

commentbox = driver.find_element_by_name('g3-comment')
commentbox.send_keys("Analysis complete!")

#submitbutton = driver.find_element_by_class_name("pushbutton-wide")
#submitbutton.click()

# displays the bar graph until the user closes it
plt.show()