---
layout: publication
title: 'No Spare Parts: Sharing Part Detectors For Image Categorization'
authors: Pascal Mettes, Jan C. van Gemert, Cees G. M. Snoek
conference: Computer Vision and Image Understanding
year: 2016
bibkey: mettes2015no
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1510.04908'}]
tags: ["Evaluation"]
short_authors: Pascal Mettes, Jan C. van Gemert, Cees G. M. Snoek
---
This work aims for image categorization using a representation of distinctive
parts. Different from existing part-based work, we argue that parts are
naturally shared between image categories and should be modeled as such. We
motivate our approach with a quantitative and qualitative analysis by
backtracking where selected parts come from. Our analysis shows that in
addition to the category parts defining the class, the parts coming from the
background context and parts from other image categories improve categorization
performance. Part selection should not be done separately for each category,
but instead be shared and optimized over all categories. To incorporate part
sharing between categories, we present an algorithm based on AdaBoost to
jointly optimize part sharing and selection, as well as fusion with the global
image representation. We achieve results competitive to the state-of-the-art on
object, scene, and action categories, further improving over deep convolutional
neural networks.