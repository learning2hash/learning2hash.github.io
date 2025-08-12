---
layout: publication
title: Transform And Bitstream Domain Image Classification
authors: P. R. Hill, D. R. Bull
conference: Arxiv
year: 2021
bibkey: hill2021transform
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.06740'}]
tags: []
short_authors: P. R. Hill, D. R. Bull
---
Classification of images within the compressed domain offers significant
benefits. These benefits include reduced memory and computational requirements
of a classification system. This paper proposes two such methods as a proof of
concept: The first classifies within the JPEG image transform domain (i.e. DCT
transform data); the second classifies the JPEG compressed binary bitstream
directly. These two methods are implemented using Residual Network CNNs and an
adapted Vision Transformer. Top-1 accuracy of approximately 70% and 60% were
achieved using these methods respectively when classifying the Caltech C101
database. Although these results are significantly behind the state of the art
for classification for this database (~95%), it illustrates the first time
direct bitstream image classification has been achieved. This work confirms
that direct bitstream image classification is possible and could be utilised in
a first pass database screening of a raw bitstream (within a wired or wireless
network) or where computational, memory and bandwidth requirements are severely
restricted.