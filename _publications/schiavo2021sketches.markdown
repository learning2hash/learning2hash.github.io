---
layout: publication
title: 'Sketches Image Analysis: Web Image Search Engine Usinglsh Index And DNN Inceptionv3'
authors: Alessio Schiavo, Filippo Minutella, Mattia Daole, Marsha Gomez Gomez
conference: Arxiv
year: 2021
bibkey: schiavo2021sketches
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.01147'}]
tags: ["Datasets", "Evaluation", "Hashing Methods", "Image Retrieval", "Similarity Search"]
short_authors: Schiavo et al.
---
The adoption of an appropriate approximate similarity search method is an
essential prereq-uisite for developing a fast and efficient CBIR system,
especially when dealing with large amount ofdata. In this study we implement a
web image search engine on top of a Locality Sensitive Hashing(LSH) Index to
allow fast similarity search on deep features. Specifically, we exploit
transfer learningfor deep features extraction from images. Firstly, we adopt
InceptionV3 pretrained on ImageNet asfeatures extractor, secondly, we try out
several CNNs built on top of InceptionV3 as convolutionalbase fine-tuned on our
dataset. In both of the previous cases we index the features extracted within
ourLSH index implementation so as to compare the retrieval performances with
and without fine-tuning.In our approach we try out two different LSH
implementations: the first one working with real numberfeature vectors and the
second one with the binary transposed version of those vectors.
Interestingly,we obtain the best performances when using the binary LSH,
reaching almost the same result, in termsof mean average precision, obtained by
performing sequential scan of the features, thus avoiding thebias introduced by
the LSH index. Lastly, we carry out a performance analysis class by class in
terms ofrecall againstmAPhighlighting, as expected, a strong positive
correlation between the two.