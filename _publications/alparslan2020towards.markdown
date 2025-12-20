---
layout: publication
title: Towards Evaluating Gaussian Blurring In Perceptual Hashing As A Facial Image
  Filter
authors: Yigit Alparslan, Ken Alparslan, Mannika Kshettry, Louis Kratz
conference: Arxiv
year: 2020
bibkey: alparslan2020towards
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.00140'}]
tags: ["Evaluation", "Hashing Methods", "Robustness"]
short_authors: Alparslan et al.
---
With the growth in social media, there is a huge amount of images of faces
available on the internet. Often, people use other people's pictures on their
own profile. Perceptual hashing is often used to detect whether two images are
identical. Therefore, it can be used to detect whether people are misusing
others' pictures. In perceptual hashing, a hash is calculated for a given
image, and a new test image is mapped to one of the existing hashes if
duplicate features are present. Therefore, it can be used as an image filter to
flag banned image content or adversarial attacks --which are modifications that
are made on purpose to deceive the filter-- even though the content might be
changed to deceive the filters. For this reason, it is critical for perceptual
hashing to be robust enough to take transformations such as resizing, cropping,
and slight pixel modifications into account. In this paper, we would like to
propose to experiment with effect of gaussian blurring in perceptual hashing
for detecting misuse of personal images specifically for face images. We
hypothesize that use of gaussian blurring on the image before calculating its
hash will increase the accuracy of our filter that detects adversarial attacks
which consist of image cropping, adding text annotation, and image rotation.