---
layout: publication
title: Autoencoder Based Face Verification System
authors: Enoch Solomon, Abraham Woubie, Eyael Solomon Emiru
conference: Arxiv
year: 2023
bibkey: solomon2023autoencoder
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.14301'}]
tags: ["Datasets", "Evaluation", "Supervised", "Unsupervised"]
short_authors: Enoch Solomon, Abraham Woubie, Eyael Solomon Emiru
---
The primary objective of this work is to present an alternative approach
aimed at reducing the dependency on labeled data. Our proposed method involves
utilizing autoencoder pre-training within a face image recognition task with
two step processes. Initially, an autoencoder is trained in an unsupervised
manner using a substantial amount of unlabeled training dataset. Subsequently,
a deep learning model is trained with initialized parameters from the
pre-trained autoencoder. This deep learning training process is conducted in a
supervised manner, employing relatively limited labeled training dataset.
During evaluation phase, face image embeddings is generated as the output of
deep neural network layer. Our training is executed on the CelebA dataset,
while evaluation is performed using benchmark face recognition datasets such as
Labeled Faces in the Wild (LFW) and YouTube Faces (YTF). Experimental results
demonstrate that by initializing the deep neural network with pre-trained
autoencoder parameters achieve comparable results to state-of-the-art methods.