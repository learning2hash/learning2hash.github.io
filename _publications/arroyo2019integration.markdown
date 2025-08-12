---
layout: publication
title: Integration Of Text-maps In Convolutional Neural Networks For Region Detection
  Among Different Textual Categories
authors: "Roberto Arroyo, Javier Tovar, Francisco J. Delgado, Emilio J. Almaz\xE1\
  n, Diego G. Serrador, Antonio Hurtado"
conference: Arxiv
year: 2019
bibkey: arroyo2019integration
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1905.10858'}]
tags: []
short_authors: Arroyo et al.
---
In this work, we propose a new technique that combines appearance and text in
a Convolutional Neural Network (CNN), with the aim of detecting regions of
different textual categories. We define a novel visual representation of the
semantic meaning of text that allows a seamless integration in a standard CNN
architecture. This representation, referred to as text-map, is integrated with
the actual image to provide a much richer input to the network. Text-maps are
colored with different intensities depending on the relevance of the words
recognized over the image. Concretely, these words are previously extracted
using Optical Character Recognition (OCR) and they are colored according to the
probability of belonging to a textual category of interest. In this sense, this
solution is especially relevant in the context of item coding for supermarket
products, where different types of textual categories must be identified, such
as ingredients or nutritional facts. We evaluated our solution in the
proprietary item coding dataset of Nielsen Brandbank, which contains more than
10,000 images for train and 2,000 images for test. The reported results
demonstrate that our approach focused on visual and textual data outperforms
state-of-the-art algorithms only based on appearance, such as standard Faster
R-CNN. These enhancements are reflected in precision and recall, which are
improved in 42 and 33 points respectively.