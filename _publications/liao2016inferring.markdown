---
layout: publication
title: Inferring Restaurant Styles By Mining Crowd Sourced Photos From User-review
  Websites
authors: Haofu Liao, Yuncheng Li, Tianran Hu, Jiebo Luo
conference: 2016 IEEE International Conference on Big Data (Big Data)
year: 2016
bibkey: liao2016inferring
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1611.06301'}]
tags: ["Datasets"]
short_authors: Liao et al.
---
When looking for a restaurant online, user uploaded photos often give people
an immediate and tangible impression about a restaurant. Due to their
informativeness, such user contributed photos are leveraged by restaurant
review websites to provide their users an intuitive and effective search
experience. In this paper, we present a novel approach to inferring restaurant
types or styles (ambiance, dish styles, suitability for different occasions)
from user uploaded photos on user-review websites. To that end, we first
collect a novel restaurant photo dataset associating the user contributed
photos with the restaurant styles from TripAdvior. We then propose a deep
multi-instance multi-label learning (MIML) framework to deal with the unique
problem setting of the restaurant style classification task. We employ a
two-step bootstrap strategy to train a multi-label convolutional neural network
(CNN). The multi-label CNN is then used to compute the confidence scores of
restaurant styles for all the images associated with a restaurant. The computed
confidence scores are further used to train a final binary classifier for each
restaurant style tag. Upon training, the styles of a restaurant can be profiled
by analyzing restaurant photos with the trained multi-label CNN and SVM models.
Experimental evaluation has demonstrated that our crowd sourcing-based approach
can effectively infer the restaurant style when there are a sufficient number
of user uploaded photos for a given restaurant.