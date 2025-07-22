---
layout: publication
title: Contextual Visual Similarity
authors: Wang Xiaofang, Kitani Kris M., Hebert Martial
conference: Arxiv
year: 2016
bibkey: wang2016contextual
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1612.02534'}]
tags: ["Similarity-Search", "Unsupervised", "Image-Retrieval"]
short_authors: Wang Xiaofang, Kitani Kris M., Hebert Martial
---
Measuring visual similarity is critical for image understanding. But what
makes two images similar? Most existing work on visual similarity assumes that
images are similar because they contain the same object instance or category.
However, the reason why images are similar is much more complex. For example,
from the perspective of category, a black dog image is similar to a white dog
image. However, in terms of color, a black dog image is more similar to a black
horse image than the white dog image. This example serves to illustrate that
visual similarity is ambiguous but can be made precise when given an explicit
contextual perspective. Based on this observation, we propose the concept of
contextual visual similarity. To be concrete, we examine the concept of
contextual visual similarity in the application domain of image search. Instead
of providing only a single image for image similarity search (\eg, Google image
search), we require three images. Given a query image, a second positive image
and a third negative image, dissimilar to the first two images, we define a
contextualized similarity search criteria. In particular, we learn feature
weights over all the feature dimensions of each image such that the distance
between the query image and the positive image is small and their distances to
the negative image are large after reweighting their features. The learned
feature weights encode the contextualized visual similarity specified by the
user and can be used for attribute specific image search. We also show the
usefulness of our contextualized similarity weighting scheme for different
tasks, such as answering visual analogy questions and unsupervised attribute
discovery.