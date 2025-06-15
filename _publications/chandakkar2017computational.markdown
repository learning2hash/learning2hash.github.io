---
layout: publication
title: 'A Computational Approach To Relative Aesthetics'
authors: Parag S. Chandakkar, Vijetha Gattupalli, Baoxin Li
conference: "Arxiv"
year: 2017
citations: 7
bibkey: chandakkar2017computational
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1704.01248'}
tags: ['Cross-Modal', 'Deep', 'Retrieval Models', 'Supervised', 'Training Strategy', 'Applications']
---
Computational visual aesthetics has recently become an active research area.
Existing state-of-art methods formulate this as a binary classification task
where a given image is predicted to be beautiful or not. In many applications
such as image retrieval and enhancement, it is more important to rank images
based on their aesthetic quality instead of binary-categorizing them.
Furthermore, in such applications, it may be possible that all images belong to
the same category. Hence determining the aesthetic ranking of the images is
more appropriate. To this end, we formulate a novel problem of ranking images
with respect to their aesthetic quality. We construct a new dataset of image
pairs with relative labels by carefully selecting images from the popular AVA
dataset. Unlike in aesthetics classification, there is no single threshold
which would determine the ranking order of the images across our entire
dataset. We propose a deep neural network based approach that is trained on
image pairs by incorporating principles from relative learning. Results show
that such relative training procedure allows our network to rank the images
with a higher accuracy than a state-of-art network trained on the same set of
images using binary labels.
