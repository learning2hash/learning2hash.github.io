---
layout: publication
title: Improving Malware Detection Accuracy By Extracting Icon Information
authors: Pedro Silva, Sepehr Akhavan-masouleh, Li Li
conference: 2018 IEEE Conference on Multimedia Information Processing and Retrieval
  (MIPR)
year: 2018
bibkey: silva2017improving
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1712.03483'}]
tags: ["Privacy & Security"]
short_authors: Pedro Silva, Sepehr Akhavan-masouleh, Li Li
---
Detecting PE malware files is now commonly approached using statistical and
machine learning models. While these models commonly use features extracted
from the structure of PE files, we propose that icons from these files can also
help better predict malware. We propose an innovative machine learning approach
to extract information from icons. Our proposed approach consists of two steps:
1) extracting icon features using summary statics, histogram of gradients
(HOG), and a convolutional autoencoder, 2) clustering icons based on the
extracted icon features. Using publicly available data and by using machine
learning experiments, we show our proposed icon clusters significantly boost
the efficacy of malware prediction models. In particular, our experiments show
an average accuracy increase of 10% when icon clusters are used in the
prediction model.