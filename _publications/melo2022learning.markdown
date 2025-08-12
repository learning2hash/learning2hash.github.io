---
layout: publication
title: Learning To Detect Good Keypoints To Match Non-rigid Objects In RGB Images
authors: Welerson Melo, Guilherme Potje, Felipe Cadar, Renato Martins, Erickson R.
  Nascimento
conference: 2022 35th SIBGRAPI Conference on Graphics, Patterns and Images (SIBGRAPI)
year: 2022
bibkey: melo2022learning
citations: 1
additional_links: [{name: Code, url: 'https://github.com/verlab/LearningToDetect'},
  {name: Paper, url: 'https://arxiv.org/abs/2212.09589'}]
tags: []
short_authors: Melo et al.
---
We present a novel learned keypoint detection method designed to maximize the
number of correct matches for the task of non-rigid image correspondence. Our
training framework uses true correspondences, obtained by matching annotated
image pairs with a predefined descriptor extractor, as a ground-truth to train
a convolutional neural network (CNN). We optimize the model architecture by
applying known geometric transformations to images as the supervisory signal.
Experiments show that our method outperforms the state-of-the-art keypoint
detector on real images of non-rigid objects by 20 p.p. on Mean Matching
Accuracy and also improves the matching performance of several descriptors when
coupled with our detection method. We also employ the proposed method in one
challenging realworld application: object retrieval, where our detector
exhibits performance on par with the best available keypoint detectors. The
source code and trained model are publicly available at
https://github.com/verlab/LearningToDetect SIBGRAPI 2022