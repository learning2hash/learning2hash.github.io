---
layout: publication
title: 'Virus-mnist: A Benchmark Malware Dataset'
authors: David Noever, Samantha E. Miller Noever
conference: Arxiv
year: 2021
bibkey: noever2021virus
citations: 21
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.00602'}]
tags: ["Datasets", "Evaluation"]
short_authors: David Noever, Samantha E. Miller Noever
---
The short note presents an image classification dataset consisting of 10
executable code varieties and approximately 50,000 virus examples. The
malicious classes include 9 families of computer viruses and one benign set.
The image formatting for the first 1024 bytes of the Portable Executable (PE)
mirrors the familiar MNIST handwriting dataset, such that most of the
previously explored algorithmic methods can transfer with minor modifications.
The designation of 9 virus families for malware derives from unsupervised
learning of class labels; we discover the families with KMeans clustering that
excludes the non-malicious examples. As a benchmark using deep learning methods
(MobileNetV2), we find an overall 80% accuracy for virus identification by
families when beneware is included. We also find that once a positive malware
detection occurs (by signature or heuristics), the projection of the first 1024
bytes into a thumbnail image can classify with 87% accuracy the type of virus.
The work generalizes what other malware investigators have demonstrated as
promising convolutional neural networks originally developed to solve image
problems but applied to a new abstract domain in pixel bytes from executable
files. The dataset is available on Kaggle and Github.