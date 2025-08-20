---
layout: publication
title: Siamese Networks For Large-scale Author Identification
authors: Chakaveh Saedi, Mark Dras
conference: Computer Speech &amp; Language
year: 2021
bibkey: saedi2021siamese
citations: 22
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.10616'}]
tags: [Datasets, Scalability]
short_authors: Chakaveh Saedi, Mark Dras
---
Authorship attribution is the process of identifying the author of a text.
Approaches to tackling it have been conventionally divided into
classification-based ones, which work well for small numbers of candidate
authors, and similarity-based methods, which are applicable for larger numbers
of authors or for authors beyond the training set; these existing
similarity-based methods have only embodied static notions of similarity. Deep
learning methods, which blur the boundaries between classification-based and
similarity-based approaches, are promising in terms of ability to learn a
notion of similarity, but have previously only been used in a conventional
small-closed-class classification setup.
  Siamese networks have been used to develop learned notions of similarity in
one-shot image tasks, and also for tasks of mostly semantic relatedness in NLP.
We examine their application to the stylistic task of authorship attribution on
datasets with large numbers of authors, looking at multiple energy functions
and neural network architectures, and show that they can substantially
outperform previous approaches.