---
layout: publication
title: Global-local Similarity For Efficient Fine-grained Image Recognition With Vision
  Transformers
authors: Edwin Arkel Rios, Min-chun Hu, Bo-cheng Lai
conference: 2025 IEEE International Symposium on Circuits and Systems (ISCAS)
year: 2025
bibkey: rios2024global
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.12891'}]
tags: []
short_authors: Edwin Arkel Rios, Min-chun Hu, Bo-cheng Lai
---
Fine-grained recognition involves the classification of images from
subordinate macro-categories, and it is challenging due to small inter-class
differences. To overcome this, most methods perform discriminative feature
selection enabled by a feature extraction backbone followed by a high-level
feature refinement step. Recently, many studies have shown the potential behind
vision transformers as a backbone for fine-grained recognition, but their usage
of its attention mechanism to select discriminative tokens can be
computationally expensive. In this work, we propose a novel and computationally
inexpensive metric to identify discriminative regions in an image. We compare
the similarity between the global representation of an image given by the CLS
token, a learnable token used by transformers for classification, and the local
representation of individual patches. We select the regions with the highest
similarity to obtain crops, which are forwarded through the same transformer
encoder. Finally, high-level features of the original and cropped
representations are further refined together in order to make more robust
predictions. Through extensive experimental evaluation we demonstrate the
effectiveness of our proposed method, obtaining favorable results in terms of
accuracy across a variety of datasets. Furthermore, our method achieves these
results at a much lower computational cost compared to the alternatives. Code
and checkpoints are available at: https://github.com/arkel23/GLSim.