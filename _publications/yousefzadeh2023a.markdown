---
layout: publication
title: A Triplet-loss Dilated Residual Network For High-resolution Representation
  Learning In Image Retrieval
authors: Saeideh Yousefzadeh, Hamidreza Pourreza, Hamidreza Mahyar
conference: Journal of Signal Processing Systems
year: 2023
bibkey: yousefzadeh2023a
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.08398'}]
tags: [Evaluation, Image Retrieval, Distance Metric Learning, Datasets, Robustness]
short_authors: Saeideh Yousefzadeh, Hamidreza Pourreza, Hamidreza Mahyar
---
Content-based image retrieval is the process of retrieving a subset of images
from an extensive image gallery based on visual contents, such as color, shape
or spatial relations, and texture. In some applications, such as localization,
image retrieval is employed as the initial step. In such cases, the accuracy of
the top-retrieved images significantly affects the overall system accuracy. The
current paper introduces a simple yet efficient image retrieval system with a
fewer trainable parameters, which offers acceptable accuracy in top-retrieved
images. The proposed method benefits from a dilated residual convolutional
neural network with triplet loss. Experimental evaluations show that this model
can extract richer information (i.e., high-resolution representations) by
enlarging the receptive field, thus improving image retrieval accuracy without
increasing the depth or complexity of the model. To enhance the extracted
representations' robustness, the current research obtains candidate regions of
interest from each feature map and applies Generalized-Mean pooling to the
regions. As the choice of triplets in a triplet-based network affects the model
training, we employ a triplet online mining method. We test the performance of
the proposed method under various configurations on two of the challenging
image-retrieval datasets, namely Revisited Paris6k (RPar) and UKBench. The
experimental results show an accuracy of 94.54 and 80.23 (mean precision at
rank 10) in the RPar medium and hard modes and 3.86 (recall at rank 4) in the
UKBench dataset, respectively.