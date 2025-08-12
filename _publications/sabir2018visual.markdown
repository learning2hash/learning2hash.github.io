---
layout: publication
title: Visual Semantic Re-ranker For Text Spotting
authors: "Ahmed Sabir, Francesc Moreno-noguer, Llu\xEDs Padr\xF3"
conference: Lecture Notes in Computer Science
year: 2019
bibkey: sabir2018visual
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1810.09776'}]
tags: ["Re-Ranking"]
short_authors: "Ahmed Sabir, Francesc Moreno-noguer, Llu\xEDs Padr\xF3"
---
Many current state-of-the-art methods for text recognition are based on
purely local information and ignore the semantic correlation between text and
its surrounding visual context. In this paper, we propose a post-processing
approach to improve the accuracy of text spotting by using the semantic
relation between the text and the scene. We initially rely on an off-the-shelf
deep neural network that provides a series of text hypotheses for each input
image. These text hypotheses are then re-ranked using the semantic relatedness
with the object in the image. As a result of this combination, the performance
of the original network is boosted with a very low computational cost. The
proposed framework can be used as a drop-in complement for any text-spotting
algorithm that outputs a ranking of word hypotheses. We validate our approach
on ICDAR'17 shared task dataset.