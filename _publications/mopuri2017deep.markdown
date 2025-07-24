---
layout: publication
title: Deep Image Representations Using Caption Generators
authors: Konda Reddy Mopuri, Vishal B. Athreya, R. Venkatesh Babu
conference: Arxiv
year: 2017
bibkey: mopuri2017deep
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.09142'}]
tags: ["Datasets", "Evaluation", "Neural Hashing"]
short_authors: Konda Reddy Mopuri, Vishal B. Athreya, R. Venkatesh Babu
---
Deep learning exploits large volumes of labeled data to learn powerful
models. When the target dataset is small, it is a common practice to perform
transfer learning using pre-trained models to learn new task specific
representations. However, pre-trained CNNs for image recognition are provided
with limited information about the image during training, which is label alone.
Tasks such as scene retrieval suffer from features learned from this weak
supervision and require stronger supervision to better understand the contents
of the image. In this paper, we exploit the features learned from caption
generating models to learn novel task specific image representations. In
particular, we consider the state-of-the art captioning system Show and
Tell~\cite\{SnT-pami-2016\} and the dense region description model
DenseCap~\cite\{densecap-cvpr-2016\}. We demonstrate that, owing to richer
supervision provided during the process of training, the features learned by
the captioning system perform better than those of CNNs. Further, we train a
siamese network with a modified pair-wise loss to fuse the features learned
by~\cite\{SnT-pami-2016\} and~\cite\{densecap-cvpr-2016\} and learn image
representations suitable for retrieval. Experiments show that the proposed
fusion exploits the complementary nature of the individual features and yields
state-of-the art retrieval results on benchmark datasets.