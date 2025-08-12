---
layout: publication
title: Recognizing Characters In Art History Using Deep Learning
authors: "Prathmesh Madhu, Ronak Kosti, Lara M\xFChrenberg, Peter Bell, Andreas Maier,\
  \ Vincent Christlein"
conference: Proceedings of the 1st Workshop on Structuring and Understanding of Multimedia
  heritAge Contents
year: 2019
bibkey: madhu2019recognizing
citations: 14
additional_links: [{name: Code, url: 'https://github.com/prathmeshrmadhu/recognize_characters_art_history'},
  {name: Code, url: 'https://dl.acm.org/citation.cfm?id=3357242'}, {name: Paper, url: 'https://arxiv.org/abs/2003.14171'}]
tags: []
short_authors: Madhu et al.
---
In the field of Art History, images of artworks and their contexts are core
to understanding the underlying semantic information. However, the highly
complex and sophisticated representation of these artworks makes it difficult,
even for the experts, to analyze the scene. From the computer vision
perspective, the task of analyzing such artworks can be divided into
sub-problems by taking a bottom-up approach. In this paper, we focus on the
problem of recognizing the characters in Art History. From the iconography of
\(Annunciation\) \(of\) \(the\) \(Lord\) (Figure 1), we consider the representation of
the main protagonists, \(Mary\) and \(Gabriel\), across different artworks and
styles. We investigate and present the findings of training a character
classifier on features extracted from their face images. The limitations of
this method, and the inherent ambiguity in the representation of \(Gabriel\),
motivated us to consider their bodies (a bigger context) to analyze in order to
recognize the characters. Convolutional Neural Networks (CNN) trained on the
bodies of \(Mary\) and \(Gabriel\) are able to learn person related features and
ultimately improve the performance of character recognition. We introduce a new
technique that generates more data with similar styles, effectively creating
data in the similar domain. We present experiments and analysis on three
different models and show that the model trained on domain related data gives
the best performance for recognizing character. Additionally, we analyze the
localized image regions for the network predictions. Code is open-sourced and
available at
https://github.com/prathmeshrmadhu/recognize_characters_art_history and the
link to the published peer-reviewed article is
https://dl.acm.org/citation.cfm?id=3357242.