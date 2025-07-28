---
layout: publication
title: A Location-aware Embedding Technique For Accurate Landmark Recognition
authors: Federico Magliani, Navid Mahmoudian Bidgoli, Andrea Prati
conference: Proceedings of the 11th International Conference on Distributed Smart
  Cameras
year: 2017
bibkey: magliani2017location
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1704.05754'}]
tags: ["Datasets"]
short_authors: Federico Magliani, Navid Mahmoudian Bidgoli, Andrea Prati
---
The current state of the research in landmark recognition highlights the good
accuracy which can be achieved by embedding techniques, such as Fisher vector
and VLAD. All these techniques do not exploit spatial information, i.e.
consider all the features and the corresponding descriptors without embedding
their location in the image. This paper presents a new variant of the
well-known VLAD (Vector of Locally Aggregated Descriptors) embedding technique
which accounts, at a certain degree, for the location of features. The driving
motivation comes from the observation that, usually, the most interesting part
of an image (e.g., the landmark to be recognized) is almost at the center of
the image, while the features at the borders are irrelevant features which do
no depend on the landmark. The proposed variant, called locVLAD (location-aware
VLAD), computes the mean of the two global descriptors: the VLAD executed on
the entire original image, and the one computed on a cropped image which
removes a certain percentage of the image borders. This simple variant shows an
accuracy greater than the existing state-of-the-art approach. Experiments are
conducted on two public datasets (ZuBuD and Holidays) which are used both for
training and testing. Morever a more balanced version of ZuBuD is proposed.