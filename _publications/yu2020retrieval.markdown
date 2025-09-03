---
layout: publication
title: Retrieval Of Family Members Using Siamese Neural Network
authors: Jun Yu, Guochen Xie, Mengyan Li, Xinlong Hao
conference: 2020 15th IEEE International Conference on Automatic Face and Gesture
  Recognition (FG 2020)
year: 2020
bibkey: yu2020retrieval
citations: 13
additional_links: [{name: Code, url: 'https://github'}, {name: Paper, url: 'https://arxiv.org/abs/2006.00174'}]
tags: ["Datasets", "Distance Metric Learning"]
short_authors: Yu et al.
---
Retrieval of family members in the wild aims at finding family members of the
given subject in the dataset, which is useful in finding the lost children and
analyzing the kinship. However, due to the diversity in age, gender, pose and
illumination of the collected data, this task is always challenging. To solve
this problem, we propose our solution with deep Siamese neural network. Our
solution can be divided into two parts: similarity computation and ranking. In
training procedure, the Siamese network firstly takes two candidate images as
input and produces two feature vectors. And then, the similarity between the
two vectors is computed with several fully connected layers. While in inference
procedure, we try another similarity computing method by dropping the followed
several fully connected layers and directly computing the cosine similarity of
the two feature vectors. After similarity computation, we use the ranking
algorithm to merge the similarity scores with the same identity and output the
ordered list according to their similarities. To gain further improvement, we
try different combinations of backbones, training methods and similarity
computing methods. Finally, we submit the best combination as our solution and
our team(ustc-nelslip) obtains favorable result in the track3 of the RFIW2020
challenge with the first runner-up, which verifies the effectiveness of our
method. Our code is available at: https://github.com/gniknoil/FG2020-kinship