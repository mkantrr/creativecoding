# -*- coding: utf-8 -*-
"""markovbiblenovel.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qYqWxLU8x5ZNw47dCQCID9Mn0FRvsrGD
"""

from google.colab import drive
drive.mount('/content/drive')

import random
!pip install markovify
import markovify
text = open("/content/drive/MyDrive/creativecoding/bible.txt", "r").read()
def sentence():

  ngrams = []

  for b in range(len(text) - 4):
    ngrams.append(text[b:b+4])

  random.shuffle(ngrams)
  seed = random.choice(ngrams)

  new_text = seed

  for i in range(300):
    for n in ngrams:
      if (n[:3] == new_text[-3:]):
        new_text += n[-1]
        ngrams.remove(n)

  text_model = markovify.Text(new_text)
  markovist = []
  for x in range(10000):
    markovist.append(text_model.make_sentence())
  markovist.remove(None)
  markovism = '\n'.join(str(s) for s in markovist)
  return markovism

# let's install weasyprint!
!pip install weasyprint==52.5

# also we need markdown
import markdown

# import some specific parts of weasyprint
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration
import random

novel = """


# The Biebel
### by Matthew Kanter


"""

for a in range(1):
  novel += sentence().capitalize()
html = markdown.markdown(novel)

font_config = FontConfiguration()
rendered_html = HTML(string=html)
css = CSS(string='''
@import url('https://fonts.googleapis.com/css2?family=Festive&display=swap');

@import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@300&display=swap');
body {
font-family: 'Merriweather', serif;
}

hr {
  break-after: recto; 
}

h1 {
  font-size: 50pt;
  text-align:center;
  margin-top: 3in;
  font-family: 'Montserrat',cursive;
}
h2{
  break-before: recto;
  font-family: 'Montserrat',cursive;
}

h3 {
  font-size: 20pt;
  text-align:center;
}

/* set the basic page geometry and start the incrementer */
@page {
  font-family: 'Merriweather', serif;
  margin: 1in;
  size: letter;
  counter-increment: page;
  @bottom-center {
    content: "Biebel";
    text-align:center;
    font-style: italic;
    color: #666666;
  }
}

/* print the page number on the bottom-right of recto pages */
@page :right {
  @bottom-right{
    content: counter(page);
    text-align:right;
    color: #666666;
    visibility: invisible;
  }
}

/* print the page number on the bottom-left of verso pages */
@page :left {
  @bottom-left{
    content: counter(page);
    text-align:left;
    color: #666666;
  }
}

/* blank the footer on the first page */
@page:first{
  @bottom-left {content: ""}
  @bottom-right {content: ""}
  @bottom-center {content: ""}
}


''', font_config=font_config)

rendered_html.write_pdf('/content/drive/MyDrive/creativecoding/markovism.pdf', stylesheets=[css],font_config=font_config)