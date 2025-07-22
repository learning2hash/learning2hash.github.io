---
layout: publication
title: 'Facenet: A Unified Embedding For Face Recognition And Clustering'
authors: Schroff Florian, Kalenichenko Dmitry, Philbin James
conference: 2015 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2015
bibkey: schroff2015facenet
citations: 8312
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1503.03832'}]
tags: ["Efficiency", "CVPR", "Evaluation", "Datasets"]
short_authors: Schroff Florian, Kalenichenko Dmitry, Philbin James
---
Despite significant recent advances in the field of face recognition,
implementing face verification and recognition efficiently at scale presents
serious challenges to current approaches. In this paper we present a system,
called FaceNet, that directly learns a mapping from face images to a compact
Euclidean space where distances directly correspond to a measure of face
similarity. Once this space has been produced, tasks such as face recognition,
verification and clustering can be easily implemented using standard techniques
with FaceNet embeddings as feature vectors.
  Our method uses a deep convolutional network trained to directly optimize the
embedding itself, rather than an intermediate bottleneck layer as in previous
deep learning approaches. To train, we use triplets of roughly aligned matching
/ non-matching face patches generated using a novel online triplet mining
method. The benefit of our approach is much greater representational
efficiency: we achieve state-of-the-art face recognition performance using only
128-bytes per face.
  On the widely used Labeled Faces in the Wild (LFW) dataset, our system
achieves a new record accuracy of 99.63%. On YouTube Faces DB it achieves
95.12%. Our system cuts the error rate in comparison to the best published
result by 30% on both datasets.
  We also introduce the concept of harmonic embeddings, and a harmonic triplet
loss, which describe different versions of face embeddings (produced by
different networks) that are compatible to each other and allow for direct
comparison between each other.