---
layout: publication
title: 'Vico: Word Embeddings From Visual Co-occurrences'
authors: Tanmay Gupta, Alexander Schwing, Derek Hoiem
conference: 2019 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2019
bibkey: gupta2019vico
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.08527'}]
tags: ["ICCV"]
short_authors: Tanmay Gupta, Alexander Schwing, Derek Hoiem
---
We propose to learn word embeddings from visual co-occurrences. Two words
co-occur visually if both words apply to the same image or image region.
Specifically, we extract four types of visual co-occurrences between object and
attribute words from large-scale, textually-annotated visual databases like
VisualGenome and ImageNet. We then train a multi-task log-bilinear model that
compactly encodes word "meanings" represented by each co-occurrence type into a
single visual word-vector. Through unsupervised clustering, supervised
partitioning, and a zero-shot-like generalization analysis we show that our
word embeddings complement text-only embeddings like GloVe by better
representing similarities and differences between visual concepts that are
difficult to obtain from text corpora alone. We further evaluate our embeddings
on five downstream applications, four of which are vision-language tasks.
Augmenting GloVe with our embeddings yields gains on all tasks. We also find
that random embeddings perform comparably to learned embeddings on all
supervised vision-language tasks, contrary to conventional wisdom.