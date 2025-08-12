---
layout: publication
title: Revisiting Image-language Networks For Open-ended Phrase Detection
authors: Bryan A. Plummer, Kevin J. Shih, Yichen Li, Ke Xu, Svetlana Lazebnik, Stan
  Sclaroff, Kate Saenko
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2020
bibkey: plummer2018revisiting
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.07212'}]
tags: []
short_authors: Plummer et al.
---
Most existing work that grounds natural language phrases in images starts
with the assumption that the phrase in question is relevant to the image. In
this paper we address a more realistic version of the natural language
grounding task where we must both identify whether the phrase is relevant to an
image and localize the phrase. This can also be viewed as a generalization of
object detection to an open-ended vocabulary, introducing elements of few- and
zero-shot detection. We propose an approach for this task that extends Faster
R-CNN to relate image regions and phrases. By carefully initializing the
classification layers of our network using canonical correlation analysis
(CCA), we encourage a solution that is more discerning when reasoning between
similar phrases, resulting in over double the performance compared to a naive
adaptation on three popular phrase grounding datasets, Flickr30K Entities,
ReferIt Game, and Visual Genome, with test-time phrase vocabulary sizes of 5K,
32K, and 159K, respectively.