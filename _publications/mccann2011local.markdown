---
layout: publication
title: Local Naive Bayes Nearest Neighbor For Image Classification
authors: Sancho Mccann, David G. Lowe
conference: 2012 IEEE Conference on Computer Vision and Pattern Recognition
year: 2012
bibkey: mccann2011local
citations: 178
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1112.0059'}]
tags: ["CVPR"]
short_authors: Sancho Mccann, David G. Lowe
---
We present Local Naive Bayes Nearest Neighbor, an improvement to the NBNN
image classification algorithm that increases classification accuracy and
improves its ability to scale to large numbers of object classes. The key
observation is that only the classes represented in the local neighborhood of a
descriptor contribute significantly and reliably to their posterior probability
estimates. Instead of maintaining a separate search structure for each class,
we merge all of the reference data together into one search structure, allowing
quick identification of a descriptor's local neighborhood. We show an increase
in classification accuracy when we ignore adjustments to the more distant
classes and show that the run time grows with the log of the number of classes
rather than linearly in the number of classes as did the original. This gives a
100 times speed-up over the original method on the Caltech 256 dataset. We also
provide the first head-to-head comparison of NBNN against spatial pyramid
methods using a common set of input features. We show that local NBNN
outperforms all previous NBNN based methods and the original spatial pyramid
model. However, we find that local NBNN, while competitive with, does not beat
state-of-the-art spatial pyramid methods that use local soft assignment and
max-pooling.