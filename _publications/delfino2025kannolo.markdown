---
layout: publication
title: 'Kannolo: Sweet And Smooth Approximate K-nearest Neighbors Search'
authors: Leonardo Delfino, Domenico Erriquez, Silvio Martinico, Franco Maria Nardini,
  Cosimo Rulli, Rossano Venturini
conference: Lecture Notes in Computer Science
year: 2025
bibkey: delfino2025kannolo
citations: 1
additional_links: [{name: Code, url: 'https://github.com/TusKANNy/kannolo'}, {name: Paper,
    url: 'https://arxiv.org/abs/2501.06121'}]
tags: []
short_authors: Delfino et al.
---
Approximate Nearest Neighbors (ANN) search is a crucial task in several
applications like recommender systems and information retrieval. Current
state-of-the-art ANN libraries, although being performance-oriented, often lack
modularity and ease of use. This translates into them not being fully suitable
for easy prototyping and testing of research ideas, an important feature to
enable. We address these limitations by introducing kANNolo, a novel
research-oriented ANN library written in Rust and explicitly designed to
combine usability with performance effectively. kANNolo is the first ANN
library that supports dense and sparse vector representations made available on
top of different similarity measures, e.g., euclidean distance and inner
product. Moreover, it also supports vector quantization techniques, e.g.,
Product Quantization, on top of the indexing strategies implemented. These
functionalities are managed through Rust traits, allowing shared behaviors to
be handled abstractly. This abstraction ensures flexibility and facilitates an
easy integration of new components. In this work, we detail the architecture of
kANNolo and demonstrate that its flexibility does not compromise performance.
The experimental analysis shows that kANNolo achieves state-of-the-art
performance in terms of speed-accuracy trade-off while allowing fast and easy
prototyping, thus making kANNolo a valuable tool for advancing ANN research.
Source code available on GitHub: https://github.com/TusKANNy/kannolo.