---
layout: publication
title: Photo Aesthetics Ranking Network With Attributes And Content Adaptation
authors: Shu Kong, Xiaohui Shen, Zhe Lin, Radomir Mech, Charless Fowlkes
conference: Lecture Notes in Computer Science
year: 2016
bibkey: kong2016photo
citations: 372
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1606.01621'}]
tags: []
short_authors: Kong et al.
---
Real-world applications could benefit from the ability to automatically
generate a fine-grained ranking of photo aesthetics. However, previous methods
for image aesthetics analysis have primarily focused on the coarse, binary
categorization of images into high- or low-aesthetic categories. In this work,
we propose to learn a deep convolutional neural network to rank photo
aesthetics in which the relative ranking of photo aesthetics are directly
modeled in the loss function. Our model incorporates joint learning of
meaningful photographic attributes and image content information which can help
regularize the complicated photo aesthetics rating problem.
  To train and analyze this model, we have assembled a new aesthetics and
attributes database (AADB) which contains aesthetic scores and meaningful
attributes assigned to each image by multiple human raters. Anonymized rater
identities are recorded across images allowing us to exploit intra-rater
consistency using a novel sampling strategy when computing the ranking loss of
training image pairs. We show the proposed sampling strategy is very effective
and robust in face of subjective judgement of image aesthetics by individuals
with different aesthetic tastes. Experiments demonstrate that our unified model
can generate aesthetic rankings that are more consistent with human ratings. To
further validate our model, we show that by simply thresholding the estimated
aesthetic scores, we are able to achieve state-or-the-art classification
performance on the existing AVA dataset benchmark.