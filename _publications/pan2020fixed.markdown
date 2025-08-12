---
layout: publication
title: Fixed-size Objects Encoding For Visual Relationship Detection
authors: Hengyue Pan, Xin Niu, Rongchun Li, Siqi Shen, Yong Dou
conference: Arxiv
year: 2020
bibkey: pan2020fixed
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2005.14600'}]
tags: ["Evaluation"]
short_authors: Pan et al.
---
In this paper, we propose a fixed-size object encoding method (FOE-VRD) to
improve performance of visual relationship detection tasks. Comparing with
previous methods, FOE-VRD has an important feature, i.e., it uses one
fixed-size vector to encoding all objects in each input image to assist the
process of relationship detection. Firstly, we use a regular convolution neural
network as a feature extractor to generate high-level features of input images.
Then, for each relationship triplet in input images, i.e.,
\(<\)subject-predicate-object\(>\), we apply ROI-pooling to get feature vectors of
two regions on the feature maps that corresponding to bounding boxes of the
subject and object. Besides the subject and object, our analysis implies that
the results of predicate classification may also related to the rest objects in
input images (we call them background objects). Due to the variable number of
background objects in different images and computational costs, we cannot
generate feature vectors for them one-by-one by using ROI pooling technique.
Instead, we propose a novel method to encode all background objects in each
image by using one fixed-size vector (i.e., FBE vector). By concatenating the 3
vectors we generate above, we successfully encode the objects using one
fixed-size vector. The generated feature vector is then feed into a fully
connected neural network to get predicate classification results. Experimental
results on VRD database (entire set and zero-shot tests) show that the proposed
method works well on both predicate classification and relationship detection.