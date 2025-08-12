---
layout: publication
title: Improving The Matching Of Deformable Objects By Learning To Detect Keypoints
authors: Felipe Cadar, Welerson Melo, Vaishnavi Kanagasabapathi, Guilherme Potje,
  Renato Martins, Erickson R. Nascimento
conference: Pattern Recognition Letters
year: 2023
bibkey: cadar2023improving
citations: 3
additional_links: [{name: Code, url: 'https://github.com/verlab/LearningToDetect_PRL_2023'},
  {name: Paper, url: 'https://arxiv.org/abs/2309.00434'}]
tags: []
short_authors: Cadar et al.
---
We propose a novel learned keypoint detection method to increase the number
of correct matches for the task of non-rigid image correspondence. By
leveraging true correspondences acquired by matching annotated image pairs with
a specified descriptor extractor, we train an end-to-end convolutional neural
network (CNN) to find keypoint locations that are more appropriate to the
considered descriptor. For that, we apply geometric and photometric warpings to
images to generate a supervisory signal, allowing the optimization of the
detector. Experiments demonstrate that our method enhances the Mean Matching
Accuracy of numerous descriptors when used in conjunction with our detection
method, while outperforming the state-of-the-art keypoint detectors on real
images of non-rigid objects by 20 p.p. We also apply our method on the complex
real-world task of object retrieval where our detector performs on par with the
finest keypoint detectors currently available for this task. The source code
and trained models are publicly available at
https://github.com/verlab/LearningToDetect_PRL_2023