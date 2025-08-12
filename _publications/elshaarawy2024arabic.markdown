---
layout: publication
title: Arabic Music Classification And Generation Using Deep Learning
authors: Mohamed Elshaarawy, Ashrakat Saeed, Mariam Sheta, Abdelrahman Said, Asem
  Bakr, Omar Bahaa, Walid Gomaa
conference: Arxiv
year: 2024
bibkey: elshaarawy2024arabic
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.19719'}]
tags: []
short_authors: Elshaarawy et al.
---
This paper proposes a machine learning approach for classifying classical and
new Egyptian music by composer and generating new similar music. The proposed
system utilizes a convolutional neural network (CNN) for classification and a
CNN autoencoder for generation. The dataset used in this project consists of
new and classical Egyptian music pieces composed by different composers.
  To classify the music by composer, each sample is normalized and transformed
into a mel spectrogram. The CNN model is trained on the dataset using the mel
spectrograms as input features and the composer labels as output classes. The
model achieves 81.4% accuracy in classifying the music by composer,
demonstrating the effectiveness of the proposed approach.
  To generate new music similar to the original pieces, a CNN autoencoder is
trained on a similar dataset. The model is trained to encode the mel
spectrograms of the original pieces into a lower-dimensional latent space and
then decode them back into the original mel spectrogram. The generated music is
produced by sampling from the latent space and decoding the samples back into
mel spectrograms, which are then transformed into audio.
  In conclusion, the proposed system provides a promising approach to
classifying and generating classical Egyptian music, which can be applied in
various musical applications, such as music recommendation systems, music
production, and music education.