---
layout: publication
title: Person Re-identification In The Wild
authors: Liang Zheng, Hengheng Zhang, Shaoyan Sun, Manmohan Chandraker, Yi Yang, Qi
  Tian
conference: 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2017
bibkey: zheng2016person
citations: 752
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1604.02531'}]
tags: ["CVPR"]
short_authors: Zheng et al.
---
We present a novel large-scale dataset and comprehensive baselines for
end-to-end pedestrian detection and person recognition in raw video frames. Our
baselines address three issues: the performance of various combinations of
detectors and recognizers, mechanisms for pedestrian detection to help improve
overall re-identification accuracy and assessing the effectiveness of different
detectors for re-identification. We make three distinct contributions. First, a
new dataset, PRW, is introduced to evaluate Person Re-identification in the
Wild, using videos acquired through six synchronized cameras. It contains 932
identities and 11,816 frames in which pedestrians are annotated with their
bounding box positions and identities. Extensive benchmarking results are
presented on this dataset. Second, we show that pedestrian detection aids
re-identification through two simple yet effective improvements: a
discriminatively trained ID-discriminative Embedding (IDE) in the person
subspace using convolutional neural network (CNN) features and a Confidence
Weighted Similarity (CWS) metric that incorporates detection scores into
similarity measurement. Third, we derive insights in evaluating detector
performance for the particular scenario of accurate person re-identification.