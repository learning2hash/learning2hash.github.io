---
layout: publication
title: Soft-phoc Descriptor For End-to-end Word Spotting In Egocentric Scene Images
authors: Dena Bazazian, Dimosthenis Karatzas, Andrew D. Bagdanov
conference: Arxiv
year: 2018
bibkey: bazazian2018soft
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1809.00854'}]
tags: ["Datasets"]
short_authors: Dena Bazazian, Dimosthenis Karatzas, Andrew D. Bagdanov
---
Word spotting in natural scene images has many applications in scene
understanding and visual assistance. In this paper we propose a technique to
create and exploit an intermediate representation of images based on text
attributes which are character probability maps. Our representation extends the
concept of the Pyramidal Histogram Of Characters (PHOC) by exploiting Fully
Convolutional Networks to derive a pixel-wise mapping of the character
distribution within candidate word regions. We call this representation the
Soft-PHOC. Furthermore, we show how to use Soft-PHOC descriptors for word
spotting tasks in egocentric camera streams through an efficient text line
proposal algorithm. This is based on the Hough Transform over character
attribute maps followed by scoring using Dynamic Time Warping (DTW). We
evaluate our results on ICDAR 2015 Challenge 4 dataset of incidental scene text
captured by an egocentric camera.