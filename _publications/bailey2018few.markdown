---
layout: publication
title: Few-shot Text Classification With Pre-trained Word Embeddings And A Human In
  The Loop
authors: Katherine Bailey, Sunny Chopra
conference: Arxiv
year: 2018
bibkey: bailey2018few
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1804.02063'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Katherine Bailey, Sunny Chopra
---
Most of the literature around text classification treats it as a supervised
learning problem: given a corpus of labeled documents, train a classifier such
that it can accurately predict the classes of unseen documents. In industry,
however, it is not uncommon for a business to have entire corpora of documents
where few or none have been classified, or where existing classifications have
become meaningless. With web content, for example, poor taxonomy management can
result in labels being applied indiscriminately, making filtering by these
labels unhelpful. Our work aims to make it possible to classify an entire
corpus of unlabeled documents using a human-in-the-loop approach, where the
content owner manually classifies just one or two documents per category and
the rest can be automatically classified. This "few-shot" learning approach
requires rich representations of the documents such that those that have been
manually labeled can be treated as prototypes, and automatic classification of
the rest is a simple case of measuring the distance to prototypes. This
approach uses pre-trained word embeddings, where documents are represented
using a simple weighted average of constituent word embeddings. We have tested
the accuracy of the approach on existing labeled datasets and provide the
results here. We have also made code available for reproducing the results we
got on the 20 Newsgroups dataset.