---
layout: publication
title: Informative And Representative Triplet Selection For Multilabel Remote Sensing
  Image Retrieval
authors: "Gencer Sumbul, Mahdyar Ravanbakhsh, Beg\xFCm Demir"
conference: IEEE Transactions on Geoscience and Remote Sensing
year: 2021
bibkey: sumbul2021informative
citations: 0
additional_links: [{name: Code, url: 'https://git.tu-berlin.de/rsim/image-retrieval-from-triplets'},
  {name: Paper, url: 'https://arxiv.org/abs/2105.03647'}]
tags: ["Distance Metric Learning", "Evaluation", "Image Retrieval"]
short_authors: "Gencer Sumbul, Mahdyar Ravanbakhsh, Beg\xFCm Demir"
---
Learning the similarity between remote sensing (RS) images forms the
foundation for content-based RS image retrieval (CBIR). Recently, deep metric
learning approaches that map the semantic similarity of images into an
embedding (metric) space have been found very popular in RS. A common approach
for learning the metric space relies on the selection of triplets of similar
(positive) and dissimilar (negative) images to a reference image called as an
anchor. Choosing triplets is a difficult task particularly for multi-label RS
CBIR, where each training image is annotated by multiple class labels. To
address this problem, in this paper we propose a novel triplet sampling method
in the framework of deep neural networks (DNNs) defined for multi-label RS CBIR
problems. The proposed method selects a small set of the most representative
and informative triplets based on two main steps. In the first step, a set of
anchors that are diverse to each other in the embedding space is selected from
the current mini-batch using an iterative algorithm. In the second step,
different sets of positive and negative images are chosen for each anchor by
evaluating the relevancy, hardness and diversity of the images among each other
based on a novel strategy. Experimental results obtained on two multi-label
benchmark archives show that the selection of the most informative and
representative triplets in the context of DNNs results in: i) reducing the
computational complexity of the training phase of the DNNs without any
significant loss on the performance; and ii) an increase in learning speed
since informative triplets allow fast convergence. The code of the proposed
method is publicly available at
https://git.tu-berlin.de/rsim/image-retrieval-from-triplets.