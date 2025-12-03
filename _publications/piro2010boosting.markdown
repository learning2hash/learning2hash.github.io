---
layout: publication
title: Boosting K-nn For Categorization Of Natural Scenes
authors: Paolo Piro, Richard Nock, Frank Nielsen, Michel Barlaud
conference: Arxiv
year: 2010
bibkey: piro2010boosting
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1001.1221'}]
tags: ["Datasets"]
short_authors: Piro et al.
---
The k-nearest neighbors (k-NN) classification rule has proven extremely
successful in countless many computer vision applications. For example, image
categorization often relies on uniform voting among the nearest prototypes in
the space of descriptors. In spite of its good properties, the classic k-NN
rule suffers from high variance when dealing with sparse prototype datasets in
high dimensions. A few techniques have been proposed to improve k-NN
classification, which rely on either deforming the nearest neighborhood
relationship or modifying the input space. In this paper, we propose a novel
boosting algorithm, called UNN (Universal Nearest Neighbors), which induces
leveraged k-NN, thus generalizing the classic k-NN rule. We redefine the voting
rule as a strong classifier that linearly combines predictions from the k
closest prototypes. Weak classifiers are learned by UNN so as to minimize a
surrogate risk. A major feature of UNN is the ability to learn which prototypes
are the most relevant for a given class, thus allowing one for effective data
reduction. Experimental results on the synthetic two-class dataset of Ripley
show that such a filtering strategy is able to reject "noisy" prototypes. We
carried out image categorization experiments on a database containing eight
classes of natural scenes. We show that our method outperforms significantly
the classic k-NN classification, while enabling significant reduction of the
computational cost by means of data filtering.