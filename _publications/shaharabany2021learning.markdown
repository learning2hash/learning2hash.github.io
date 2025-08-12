---
layout: publication
title: Learning A Weight Map For Weakly-supervised Localization
authors: Tal Shaharabany, Lior Wolf
conference: Arxiv
year: 2021
bibkey: shaharabany2021learning
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.14131'}]
tags: []
short_authors: Tal Shaharabany, Lior Wolf
---
In the weakly supervised localization setting, supervision is given as an
image-level label. We propose to employ an image classifier \(f\) and to train a
generative network \(g\) that outputs, given the input image, a per-pixel weight
map that indicates the location of the object within the image. Network \(g\) is
trained by minimizing the discrepancy between the output of the classifier \(f\)
on the original image and its output given the same image weighted by the
output of \(g\). The scheme requires a regularization term that ensures that \(g\)
does not provide a uniform weight, and an early stopping criterion in order to
prevent \(g\) from over-segmenting the image. Our results indicate that the
method outperforms existing localization methods by a sizable margin on the
challenging fine-grained classification datasets, as well as a generic image
recognition dataset. Additionally, the obtained weight map is also
state-of-the-art in weakly supervised segmentation in fine-grained
categorization datasets.