---
layout: publication
title: 'ANER: Arabic And Arabizi Named Entity Recognition Using Transformer-based
  Approach'
authors: Abdelrahman "boda" Sadallah, Omar Ahmed, Shimaa Mohamed, Omar Hatem, Doaa
  Hesham, Ahmed H. Yousef
conference: 2023 Intelligent Methods, Systems, and Applications (IMSA)
year: 2023
bibkey: sadallah2023aner
citations: 2
additional_links: [{name: Code, url: 'http://www.aner.online'}, {name: Code, url: 'https://huggingface.co/boda/ANER,'},
  {name: Paper, url: 'https://arxiv.org/abs/2308.14669'}]
tags: ["Datasets"]
short_authors: Sadallah et al.
---
One of the main tasks of Natural Language Processing (NLP), is Named Entity
Recognition (NER). It is used in many applications and also can be used as an
intermediate step for other tasks. We present ANER, a web-based named entity
recognizer for the Arabic, and Arabizi languages. The model is built upon BERT,
which is a transformer-based encoder. It can recognize 50 different entity
classes, covering various fields. We trained our model on the WikiFANE\_Gold
dataset which consists of Wikipedia articles. We achieved an F1 score of
88.7%, which beats CAMeL Tools' F1 score of 83% on the ANERcorp dataset,
which has only 4 classes. We also got an F1 score of 77.7% on the
NewsFANE\_Gold dataset which contains out-of-domain data from News articles.
The system is deployed on a user-friendly web interface that accepts users'
inputs in Arabic, or Arabizi. It allows users to explore the entities in the
text by highlighting them. It can also direct users to get information about
entities through Wikipedia directly. We added the ability to do NER using our
model, or CAMeL Tools' model through our website. ANER is publicly accessible
at http://www.aner.online. We also deployed our model on HuggingFace at
https://huggingface.co/boda/ANER, to allow developers to test and use it.