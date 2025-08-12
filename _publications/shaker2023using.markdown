---
layout: publication
title: Using LSTM And GRU With A New Dataset For Named Entity Recognition In The Arabic
  Language
authors: Alaa Shaker, Alaa Aldarf, Igor Bessmertny
conference: Arxiv
year: 2023
bibkey: shaker2023using
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.03399'}]
tags: ["Datasets"]
short_authors: Alaa Shaker, Alaa Aldarf, Igor Bessmertny
---
Named entity recognition (NER) is a natural language processing task (NLP),
which aims to identify named entities and classify them like person, location,
organization, etc. In the Arabic language, we can find a considerable size of
unstructured data, and it needs to different preprocessing tool than languages
like (English, Russian, German...). From this point, we can note the importance
of building a new structured dataset to solve the lack of structured data. In
this work, we use the BIOES format to tag the word, which allows us to handle
the nested name entity that consists of more than one sentence and define the
start and the end of the name. The dataset consists of more than thirty-six
thousand records. In addition, this work proposes long short term memory (LSTM)
units and Gated Recurrent Units (GRU) for building the named entity recognition
model in the Arabic language. The models give an approximately good result
(80%) because LSTM and GRU models can find the relationships between the words
of the sentence. Also, use a new library from Google, which is Trax and
platform Colab