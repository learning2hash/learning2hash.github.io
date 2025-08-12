---
layout: publication
title: Bag-of-visual-words For Signature-based Multi-script Document Retrieval
authors: Ranju Mandal, Partha Pratim Roy, Umapada Pal, Michael Blumenstein
conference: Neural Computing and Applications
year: 2018
bibkey: mandal2018bag
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1807.06772'}]
tags: ["Text Retrieval"]
short_authors: Mandal et al.
---
An end-to-end architecture for multi-script document retrieval using
handwritten signatures is proposed in this paper. The user supplies a query
signature sample and the system exclusively returns a set of documents that
contain the query signature. In the first stage, a component-wise
classification technique separates the potential signature components from all
other components. A bag-of-visual-words powered by SIFT descriptors in a
patch-based framework is proposed to compute the features and a Support Vector
Machine (SVM)-based classifier was used to separate signatures from the
documents. In the second stage, features from the foreground (i.e. signature
strokes) and the background spatial information (i.e. background loops,
reservoirs etc.) were combined to characterize the signature object to match
with the query signature. Finally, three distance measures were used to match a
query signature with the signature present in target documents for retrieval.
The `Tobacco' document database and an Indian script database containing 560
documents of Devanagari (Hindi) and Bangla scripts were used for the
performance evaluation. The proposed system was also tested on noisy documents
and promising results were obtained. A comparative study shows that the
proposed method outperforms the state-of-the-art approaches.