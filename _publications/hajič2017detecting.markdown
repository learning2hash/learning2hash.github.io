---
layout: publication
title: Detecting Noteheads In Handwritten Scores With Convnets And Bounding Box Regression
authors: "Jan Haji\u010D, Pavel Pecina"
conference: Arxiv
year: 2017
bibkey: "haji\u010D2017detecting"
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1708.01806'}]
tags: []
short_authors: "Jan Haji\u010D, Pavel Pecina"
---
Noteheads are the interface between the written score and music. Each
notehead on the page signifies one note to be played, and detecting noteheads
is thus an unavoidable step for Optical Music Recognition. Noteheads are
clearly distinct objects, however, the variety of music notation handwriting
makes noteheads harder to identify, and while handwritten music notation symbol
\{\em classification\} is a well-studied task, symbol \{\em detection\} has usually
been limited to heuristics and rule-based systems instead of machine learning
methods better suited to deal with the uncertainties in handwriting. We present
ongoing work on a simple notehead detector using convolutional neural networks
for pixel classification and bounding box regression that achieves a detection
f-score of 0.97 on binary score images in the MUSCIMA++ dataset, does not
require staff removal, and is applicable to a variety of handwriting styles and
levels of musical complexity.