---
layout: publication
title: Fine-tuning CNN Image Retrieval With No Human Annotation
authors: "Radenovi\u0107 Filip, Tolias Giorgos, Chum Ond\u0159ej"
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2018
bibkey: "radenovi\u01072017fine"
citations: 1184
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1711.02512'}]
tags: ["Efficiency", "Evaluation", "Image-Retrieval", "Datasets"]
short_authors: "Radenovi\u0107 Filip, Tolias Giorgos, Chum Ond\u0159ej"
---
Image descriptors based on activations of Convolutional Neural Networks
(CNNs) have become dominant in image retrieval due to their discriminative
power, compactness of representation, and search efficiency. Training of CNNs,
either from scratch or fine-tuning, requires a large amount of annotated data,
where a high quality of annotation is often crucial. In this work, we propose
to fine-tune CNNs for image retrieval on a large collection of unordered images
in a fully automated manner. Reconstructed 3D models obtained by the
state-of-the-art retrieval and structure-from-motion methods guide the
selection of the training data. We show that both hard-positive and
hard-negative examples, selected by exploiting the geometry and the camera
positions available from the 3D models, enhance the performance of
particular-object retrieval. CNN descriptor whitening discriminatively learned
from the same training data outperforms commonly used PCA whitening. We propose
a novel trainable Generalized-Mean (GeM) pooling layer that generalizes max and
average pooling and show that it boosts retrieval performance. Applying the
proposed method to the VGG network achieves state-of-the-art performance on the
standard benchmarks: Oxford Buildings, Paris, and Holidays datasets.