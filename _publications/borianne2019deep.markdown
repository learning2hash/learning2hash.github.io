---
layout: publication
title: 'Deep Mangoes: From Fruit Detection To Cultivar Identification In Colour Images
  Of Mango Trees'
authors: Philippe Borianne, Frederic Borne, Julien Sarron, Emile Faye
conference: DISP19 International Conference on Digital Image and Signal Processing
  Apr 2019 Oxford United Kingdom
year: 2019
bibkey: borianne2019deep
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.10939'}]
tags: []
short_authors: Borianne et al.
---
This paper presents results on the detection and identification mango fruits
from colour images of trees. We evaluate the behaviour and the performances of
the Faster R-CNN network to determine whether it is robust enough to "detect
and classify" fruits under particularly heterogeneous conditions in terms of
plant cultivars, plantation scheme, and visual information acquisition
contexts. The network is trained to distinguish the 'Kent', 'Keitt', and
"Boucodiekhal" mango cultivars from 3,000 representative labelled fruit
annotations. The validation set composed of about 7,000 annotations was then
tested with a confidence threshold of 0.7 and a Non-Maximal-Suppression
threshold of 0.25. With a F1-score of 0.90, the Faster R-CNN is well suitable
to the simple fruit detection in tiles of 500x500 pixels. We then combine a
multi-tiling approach with a Jaccard matrix to merge the different parts of
objects detected several times, and thus report the detections made at the tile
scale to the native 6,000x4,000 pixel size images. Nonetheless with a F1-score
of 0.56, the cultivar identification Faster R-CNN network presents some
limitations for simultaneously detecting the mango fruits and identifying their
respective cultivars. Despite the proven errors in fruit detection, the
cultivar identification rates of the detected mango fruits are in the order of
80%. The ideal solution could combine a Mask R-CNN for the image
pre-segmentation of trees and a double-stream Faster R-CNN for detecting the
mango fruits and identifying their respective cultivar to provide predictions
more relevant to users' expectations.