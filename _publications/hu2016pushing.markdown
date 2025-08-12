---
layout: publication
title: Pushing The Limits Of Deep Cnns For Pedestrian Detection
authors: Qichang Hu, Peng Wang, Chunhua Shen, Anton van Den Hengel, Fatih Porikli
conference: IEEE Transactions on Circuits and Systems for Video Technology
year: 2017
bibkey: hu2016pushing
citations: 86
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1603.04525'}]
tags: []
short_authors: Hu et al.
---
Compared to other applications in computer vision, convolutional neural
networks have under-performed on pedestrian detection. A breakthrough was made
very recently by using sophisticated deep CNN models, with a number of
hand-crafted features, or explicit occlusion handling mechanism. In this work,
we show that by re-using the convolutional feature maps (CFMs) of a deep
convolutional neural network (DCNN) model as image features to train an
ensemble of boosted decision models, we are able to achieve the best reported
accuracy without using specially designed learning algorithms. We empirically
identify and disclose important implementation details. We also show that pixel
labelling may be simply combined with a detector to boost the detection
performance. By adding complementary hand-crafted features such as optical
flow, the DCNN based detector can be further improved. We set a new record on
the Caltech pedestrian dataset, lowering the log-average miss rate from
\\(11.7%\\) to \\(8.9%\\), a relative improvement of \\(24%\\). We also achieve a
comparable result to the state-of-the-art approaches on the KITTI dataset.