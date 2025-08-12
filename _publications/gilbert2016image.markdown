---
layout: publication
title: Image And Video Mining Through Online Learning
authors: Andrew Gilbert, Richard Bowden
conference: Computer Vision and Image Understanding
year: 2017
bibkey: gilbert2016image
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1609.02770'}]
tags: ["Datasets", "Tools & Libraries"]
short_authors: Andrew Gilbert, Richard Bowden
---
Within the field of image and video recognition, the traditional approach is
a dataset split into fixed training and test partitions. However, the labelling
of the training set is time-consuming, especially as datasets grow in size and
complexity. Furthermore, this approach is not applicable to the home user, who
wants to intuitively group their media without tirelessly labelling the
content. Our interactive approach is able to iteratively cluster classes of
images and video. Our approach is based around the concept of an image
signature which, unlike a standard bag of words model, can express
co-occurrence statistics as well as symbol frequency. We efficiently compute
metric distances between signatures despite their inherent high dimensionality
and provide discriminative feature selection, to allow common and distinctive
elements to be identified from a small set of user labelled examples. These
elements are then accentuated in the image signature to increase similarity
between examples and pull correct classes together. By repeating this process
in an online learning framework, the accuracy of similarity increases
dramatically despite labelling only a few training examples. To demonstrate
that the approach is agnostic to media type and features used, we evaluate on
three image datasets (15 scene, Caltech101 and FG-NET), a mixed text and image
dataset (ImageTag), a dataset used in active learning (Iris) and on three
action recognition datasets (UCF11, KTH and Hollywood2). On the UCF11 video
dataset, the accuracy is 86.7% despite using only 90 labelled examples from a
dataset of over 1200 videos, instead of the standard 1122 training videos. The
approach is both scalable and efficient, with a single iteration over the full
UCF11 dataset of around 1200 videos taking approximately 1 minute on a standard
desktop machine.