---
layout: publication
title: Explaining Deepfake Detection By Analysing Image Matching
authors: Shichao Dong, Jin Wang, Jiajun Liang, Haoqiang Fan, Renhe Ji
conference: Lecture Notes in Computer Science
year: 2022
bibkey: dong2022explaining
citations: 28
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.09679'}]
tags: ["Evaluation"]
short_authors: Dong et al.
---
This paper aims to interpret how deepfake detection models learn artifact
features of images when just supervised by binary labels. To this end, three
hypotheses from the perspective of image matching are proposed as follows. 1.
Deepfake detection models indicate real/fake images based on visual concepts
that are neither source-relevant nor target-relevant, that is, considering such
visual concepts as artifact-relevant. 2. Besides the supervision of binary
labels, deepfake detection models implicitly learn artifact-relevant visual
concepts through the FST-Matching (i.e. the matching fake, source, target
images) in the training set. 3. Implicitly learned artifact visual concepts
through the FST-Matching in the raw training set are vulnerable to video
compression. In experiments, the above hypotheses are verified among various
DNNs. Furthermore, based on this understanding, we propose the FST-Matching
Deepfake Detection Model to boost the performance of forgery detection on
compressed videos. Experiment results show that our method achieves great
performance, especially on highly-compressed (e.g. c40) videos.