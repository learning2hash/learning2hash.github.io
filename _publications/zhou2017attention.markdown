---
layout: publication
title: Attention-based Natural Language Person Retrieval
authors: Tao Zhou, Muhao Chen, Jie Yu, Demetri Terzopoulos
conference: 2017 IEEE Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2017
bibkey: zhou2017attention
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.08923'}]
tags: ["CVPR", "Datasets", "Evaluation"]
short_authors: Zhou et al.
---
Following the recent progress in image classification and captioning using
deep learning, we develop a novel natural language person retrieval system
based on an attention mechanism. More specifically, given the description of a
person, the goal is to localize the person in an image. To this end, we first
construct a benchmark dataset for natural language person retrieval. To do so,
we generate bounding boxes for persons in a public image dataset from the
segmentation masks, which are then annotated with descriptions and attributes
using the Amazon Mechanical Turk. We then adopt a region proposal network in
Faster R-CNN as a candidate region generator. The cropped images based on the
region proposals as well as the whole images with attention weights are fed
into Convolutional Neural Networks for visual feature extraction, while the
natural language expression and attributes are input to Bidirectional Long
Short- Term Memory (BLSTM) models for text feature extraction. The visual and
text features are integrated to score region proposals, and the one with the
highest score is retrieved as the output of our system. The experimental
results show significant improvement over the state-of-the-art method for
generic object retrieval and this line of research promises to benefit search
in surveillance video footage.