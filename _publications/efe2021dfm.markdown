---
layout: publication
title: 'DFM: A Performance Baseline For Deep Feature Matching'
authors: Ufuk Efe, Kutalmis Gokalp Ince, A. Aydin Alatan
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2021
bibkey: efe2021dfm
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.07791'}]
tags: ["CVPR", "Datasets", "Evaluation"]
short_authors: Ufuk Efe, Kutalmis Gokalp Ince, A. Aydin Alatan
---
A novel image matching method is proposed that utilizes learned features
extracted by an off-the-shelf deep neural network to obtain a promising
performance. The proposed method uses pre-trained VGG architecture as a feature
extractor and does not require any additional training specific to improve
matching. Inspired by well-established concepts in the psychology area, such as
the Mental Rotation paradigm, an initial warping is performed as a result of a
preliminary geometric transformation estimate. These estimates are simply based
on dense matching of nearest neighbors at the terminal layer of VGG network
outputs of the images to be matched. After this initial alignment, the same
approach is repeated again between reference and aligned images in a
hierarchical manner to reach a good localization and matching performance. Our
algorithm achieves 0.57 and 0.80 overall scores in terms of Mean Matching
Accuracy (MMA) for 1 pixel and 2 pixels thresholds respectively on Hpatches
dataset, which indicates a better performance than the state-of-the-art.