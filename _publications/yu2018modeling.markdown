---
layout: publication
title: Modeling Text with Graph Convolutional Network for Cross-Modal Information
  Retrieval
authors: Yu et al.
conference: Lecture Notes in Computer Science
year: 2018
bibkey: yu2018modeling
citations: 44
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1802.00985'}]
tags: []
---
Cross-modal information retrieval aims to find heterogeneous data of various
modalities from a given query of one modality. The main challenge is to map
different modalities into a common semantic space, in which distance between
concepts in different modalities can be well modeled. For cross-modal
information retrieval between images and texts, existing work mostly uses
off-the-shelf Convolutional Neural Network (CNN) for image feature extraction.
For texts, word-level features such as bag-of-words or word2vec are employed to
build deep learning models to represent texts. Besides word-level semantics,
the semantic relations between words are also informative but less explored. In
this paper, we model texts by graphs using similarity measure based on
word2vec. A dual-path neural network model is proposed for couple feature
learning in cross-modal information retrieval. One path utilizes Graph
Convolutional Network (GCN) for text modeling based on graph representations.
The other path uses a neural network with layers of nonlinearities for image
modeling based on off-the-shelf features. The model is trained by a pairwise
similarity loss function to maximize the similarity of relevant text-image
pairs and minimize the similarity of irrelevant pairs. Experimental results
show that the proposed model outperforms the state-of-the-art methods
significantly, with 17% improvement on accuracy for the best case.