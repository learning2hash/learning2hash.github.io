---
layout: publication
title: Retrieval Augmentation For Deep Neural Networks
authors: "Rita Parada Ramos, Patr\xEDcia Pereira, Helena Moniz, Joao Paulo Carvalho,\
  \ Bruno Martins"
conference: 2021 International Joint Conference on Neural Networks (IJCNN)
year: 2021
bibkey: ramos2021retrieval
citations: 6
additional_links: [{name: Code, url: 'http://github.com/RitaRamo/retrieval-augmentation-nn'},
  {name: Paper, url: 'https://arxiv.org/abs/2102.13030'}]
tags: ["Text Retrieval"]
short_authors: Ramos et al.
---
Deep neural networks have achieved state-of-the-art results in various vision
and/or language tasks. Despite the use of large training datasets, most models
are trained by iterating over single input-output pairs, discarding the
remaining examples for the current prediction. In this work, we actively
exploit the training data, using the information from nearest training examples
to aid the prediction both during training and testing. Specifically, our
approach uses the target of the most similar training example to initialize the
memory state of an LSTM model, or to guide attention mechanisms. We apply this
approach to image captioning and sentiment analysis, respectively through image
and text retrieval. Results confirm the effectiveness of the proposed approach
for the two tasks, on the widely used Flickr8 and IMDB datasets. Our code is
publicly available at http://github.com/RitaRamo/retrieval-augmentation-nn.