---
layout: publication
title: Class-weighted Convolutional Features For Visual Instance Search
authors: Albert Jimenez, Jose M. Alvarez, Xavier Giro-I-Nieto
conference: Procedings of the British Machine Vision Conference 2017
year: 2017
bibkey: jimenez2017class
citations: 71
additional_links: [{name: Code, url: 'http://imatge-upc.github.io/retrieval-2017-cam/.'},
  {name: Paper, url: 'https://arxiv.org/abs/1707.02581'}]
tags: [Datasets, Hybrid ANN Methods, Re-ranking, Image Retrieval, Unsupervised]
short_authors: Albert Jimenez, Jose M. Alvarez, Xavier Giro-I-Nieto
---
Image retrieval in realistic scenarios targets large dynamic datasets of
unlabeled images. In these cases, training or fine-tuning a model every time
new images are added to the database is neither efficient nor scalable.
Convolutional neural networks trained for image classification over large
datasets have been proven effective feature extractors for image retrieval. The
most successful approaches are based on encoding the activations of
convolutional layers, as they convey the image spatial information. In this
paper, we go beyond this spatial information and propose a local-aware encoding
of convolutional features based on semantic information predicted in the target
image. To this end, we obtain the most discriminative regions of an image using
Class Activation Maps (CAMs). CAMs are based on the knowledge contained in the
network and therefore, our approach, has the additional advantage of not
requiring external information. In addition, we use CAMs to generate object
proposals during an unsupervised re-ranking stage after a first fast search.
Our experiments on two public available datasets for instance retrieval,
Oxford5k and Paris6k, demonstrate the competitiveness of our approach
outperforming the current state-of-the-art when using off-the-shelf models
trained on ImageNet. The source code and model used in this paper are publicly
available at http://imatge-upc.github.io/retrieval-2017-cam/.