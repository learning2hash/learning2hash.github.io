---
layout: publication
title: Learning A Distance Function With A Siamese Network To Localize Anomalies In
  Videos
authors: Bharathkumar Ramachandra, Michael J. Jones, Ranga Raju Vatsavai
conference: 2020 IEEE Winter Conference on Applications of Computer Vision (WACV)
year: 2020
bibkey: ramachandra2020learning
citations: 83
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2001.09189'}]
tags: []
short_authors: Bharathkumar Ramachandra, Michael J. Jones, Ranga Raju Vatsavai
---
This work introduces a new approach to localize anomalies in surveillance
video. The main novelty is the idea of using a Siamese convolutional neural
network (CNN) to learn a distance function between a pair of video patches
(spatio-temporal regions of video). The learned distance function, which is not
specific to the target video, is used to measure the distance between each
video patch in the testing video and the video patches found in normal training
video. If a testing video patch is not similar to any normal video patch then
it must be anomalous. We compare our approach to previously published
algorithms using 4 evaluation measures and 3 challenging target benchmark
datasets. Experiments show that our approach either surpasses or performs
comparably to current state-of-the-art methods.