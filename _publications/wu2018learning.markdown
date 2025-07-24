---
layout: publication
title: Learning Product Codebooks Using Vector Quantized Autoencoders For Image Retrieval
authors: Hanwei Wu, Markus Flierl
conference: Arxiv
year: 2018
bibkey: wu2018learning
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1807.04629'}]
tags: ["Efficiency", "Image Retrieval", "Quantization", "Unsupervised"]
short_authors: Hanwei Wu, Markus Flierl
---
Vector-Quantized Variational Autoencoders (VQ-VAE)[1] provide an unsupervised
model for learning discrete representations by combining vector quantization
and autoencoders. In this paper, we study the use of VQ-VAE for representation
learning for downstream tasks, such as image retrieval. We first describe the
VQ-VAE in the context of an information-theoretic framework. We show that the
regularization term on the learned representation is determined by the size of
the embedded codebook before the training and it affects the generalization
ability of the model. As a result, we introduce a hyperparameter to balance the
strength of the vector quantizer and the reconstruction error. By tuning the
hyperparameter, the embedded bottleneck quantizer is used as a regularizer that
forces the output of the encoder to share a constrained coding space such that
learned latent features preserve the similarity relations of the data space. In
addition, we provide a search range for finding the best hyperparameter.
Finally, we incorporate the product quantization into the bottleneck stage of
VQ-VAE and propose an end-to-end unsupervised learning model for the image
retrieval task. The product quantizer has the advantage of generating
large-size codebooks. Fast retrieval can be achieved by using the lookup tables
that store the distance between any pair of sub-codewords. State-of-the-art
retrieval results are achieved by the learned codebooks.