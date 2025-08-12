---
layout: publication
title: Transfer Learning For Image-based Malware Classification
authors: Niket Bhodia, Pratikkumar Prajapati, Fabio di Troia, Mark Stamp
conference: Proceedings of the 5th International Conference on Information Systems
  Security and Privacy
year: 2019
bibkey: bhodia2019transfer
citations: 96
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1903.11551'}]
tags: ["Datasets", "Evaluation"]
short_authors: Bhodia et al.
---
In this paper, we consider the problem of malware detection and
classification based on image analysis. We convert executable files to images
and apply image recognition using deep learning (DL) models. To train these
models, we employ transfer learning based on existing DL models that have been
pre-trained on massive image datasets. We carry out various experiments with
this technique and compare its performance to that of an extremely simple
machine learning technique, namely, k-nearest neighbors (\kNN). For our k-NN
experiments, we use features extracted directly from executables, rather than
image analysis. While our image-based DL technique performs well in the
experiments, surprisingly, it is outperformed by k-NN. We show that DL models
are better able to generalize the data, in the sense that they outperform k-NN
in simulated zero-day experiments.