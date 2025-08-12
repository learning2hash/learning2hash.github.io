---
layout: publication
title: How Can Voting Mechanisms Improve The Robustness And Generalizability Of Toponym
  Disambiguation?
authors: Xuke Hu, Yeran Sun, Jens Kersten, Zhiyong Zhou, Friederike Klan, Hongchao
  Fan
conference: International Journal of Applied Earth Observation and Geoinformation
year: 2023
bibkey: hu2022how
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.08286'}]
tags: ["Robustness"]
short_authors: Hu et al.
---
A vast amount of geographic information exists in natural language texts,
such as tweets and news. Extracting geographic information from texts is called
Geoparsing, which includes two subtasks: toponym recognition and toponym
disambiguation, i.e., to identify the geospatial representations of toponyms.
This paper focuses on toponym disambiguation, which is usually approached by
toponym resolution and entity linking. Recently, many novel approaches have
been proposed, especially deep learning-based approaches, such as CamCoder,
GENRE, and BLINK. In this paper, a spatial clustering-based voting approach
that combines several individual approaches is proposed to improve SOTA
performance in terms of robustness and generalizability. Experiments are
conducted to compare a voting ensemble with 20 latest and commonly-used
approaches based on 12 public datasets, including several highly ambiguous and
challenging datasets (e.g., WikToR and CLDW). The datasets are of six types:
tweets, historical documents, news, web pages, scientific articles, and
Wikipedia articles, containing in total 98,300 places across the world. The
results show that the voting ensemble performs the best on all the datasets,
achieving an average Accuracy@161km of 0.86, proving the generalizability and
robustness of the voting approach. Also, the voting ensemble drastically
improves the performance of resolving fine-grained places, i.e., POIs, natural
features, and traffic ways.