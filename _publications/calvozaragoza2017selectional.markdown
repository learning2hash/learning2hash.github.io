---
layout: publication
title: A Selectional Auto-encoder Approach For Document Image Binarization
authors: Jorge Calvo-zaragoza, Antonio-javier Gallego
conference: Pattern Recognition
year: 2018
bibkey: calvozaragoza2017selectional
citations: 153
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1706.10241'}]
tags: ["Evaluation"]
short_authors: Jorge Calvo-zaragoza, Antonio-javier Gallego
---
Binarization plays a key role in the automatic information retrieval from
document images. This process is usually performed in the first stages of
documents analysis systems, and serves as a basis for subsequent steps. Hence
it has to be robust in order to allow the full analysis workflow to be
successful. Several methods for document image binarization have been proposed
so far, most of which are based on hand-crafted image processing strategies.
Recently, Convolutional Neural Networks have shown an amazing performance in
many disparate duties related to computer vision. In this paper we discuss the
use of convolutional auto-encoders devoted to learning an end-to-end map from
an input image to its selectional output, in which activations indicate the
likelihood of pixels to be either foreground or background. Once trained,
documents can therefore be binarized by parsing them through the model and
applying a threshold. This approach has proven to outperform existing
binarization strategies in a number of document domains.