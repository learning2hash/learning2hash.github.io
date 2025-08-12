---
layout: publication
title: 'Deep Learning For Metagenomic Data: Using 2D Embeddings And Convolutional
  Neural Networks'
authors: Thanh Hai Nguyen, Yann Chevaleyre, Edi Prifti, Nataliya Sokolovska, Jean-Daniel
  Zucker
conference: Arxiv
year: 2017
bibkey: nguyen2017deep
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1712.00244'}]
tags: ["Datasets"]
short_authors: Nguyen et al.
---
Deep learning (DL) techniques have had unprecedented success when applied to
images, waveforms, and texts to cite a few. In general, when the sample size
(N) is much greater than the number of features (d), DL outperforms previous
machine learning (ML) techniques, often through the use of convolution neural
networks (CNNs). However, in many bioinformatics ML tasks, we encounter the
opposite situation where d is greater than N. In these situations, applying DL
techniques (such as feed-forward networks) would lead to severe overfitting.
Thus, sparse ML techniques (such as LASSO e.g.) usually yield the best results
on these tasks. In this paper, we show how to apply CNNs on data which do not
have originally an image structure (in particular on metagenomic data). Our
first contribution is to show how to map metagenomic data in a meaningful way
to 1D or 2D images. Based on this representation, we then apply a CNN, with the
aim of predicting various diseases. The proposed approach is applied on six
different datasets including in total over 1000 samples from various diseases.
This approach could be a promising one for prediction tasks in the
bioinformatics field.