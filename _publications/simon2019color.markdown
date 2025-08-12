---
layout: publication
title: Color Inference From Semantic Labeling For Person Search In Videos
authors: Jules Simon, Guillaume-alexandre Bilodeau, David Steele, Harshad Mahadik
conference: Lecture Notes in Computer Science
year: 2020
bibkey: simon2019color
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.13114'}]
tags: ["Datasets", "Evaluation"]
short_authors: Simon et al.
---
We propose an explainable model to generate semantic color labels for person
search. In this context, persons are described from their semantic parts, such
as hat, shirt, etc. Person search consists in looking for people based on these
descriptions. In this work, we aim to improve the accuracy of color labels for
people. Our goal is to handle the high variability of human perception.
Existing solutions are based on hand-crafted features or learnt features that
are not explainable. Moreover most of them only focus on a limited set of
colors. We propose a method based on binary search trees and a large
peer-labelled color name dataset. This allows us to synthesize the human
perception of colors. Using semantic segmentation and our color labeling
method, we label segments of pedestrians with their associated colors. We
evaluate our solution on person search on datasets such as PCN, and show a
precision as high as 80.4%.