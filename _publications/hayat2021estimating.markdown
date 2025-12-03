---
layout: publication
title: Estimating Galactic Distances From Images Using Self-supervised Representation
  Learning
authors: "Md Abul Hayat, Peter Harrington, George Stein, Zarija Luki\u0107, Mustafa\
  \ Mustafa"
conference: Arxiv
year: 2021
bibkey: hayat2021estimating
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2101.04293'}]
tags: ["Self-Supervised", "Similarity Search", "Supervised", "Survey Paper", "Tools & Libraries"]
short_authors: Hayat et al.
---
We use a contrastive self-supervised learning framework to estimate distances
to galaxies from their photometric images. We incorporate data augmentations
from computer vision as well as an application-specific augmentation accounting
for galactic dust. We find that the resulting visual representations of galaxy
images are semantically useful and allow for fast similarity searches, and can
be successfully fine-tuned for the task of redshift estimation. We show that
(1) pretraining on a large corpus of unlabeled data followed by fine-tuning on
some labels can attain the accuracy of a fully-supervised model which requires
2-4x more labeled data, and (2) that by fine-tuning our self-supervised
representations using all available data labels in the Main Galaxy Sample of
the Sloan Digital Sky Survey (SDSS), we outperform the state-of-the-art
supervised learning method.