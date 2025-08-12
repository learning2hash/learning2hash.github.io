---
layout: publication
title: Transductive Learning For Near-duplicate Image Detection In Scanned Photo Collections
authors: Francesc Net, Marc Folia, Pep Casals, Lluis Gomez
conference: Lecture Notes in Computer Science
year: 2023
bibkey: net2023transductive
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.19437'}]
tags: ["Datasets"]
short_authors: Net et al.
---
This paper presents a comparative study of near-duplicate image detection
techniques in a real-world use case scenario, where a document management
company is commissioned to manually annotate a collection of scanned
photographs. Detecting duplicate and near-duplicate photographs can reduce the
time spent on manual annotation by archivists. This real use case differs from
laboratory settings as the deployment dataset is available in advance, allowing
the use of transductive learning. We propose a transductive learning approach
that leverages state-of-the-art deep learning architectures such as
convolutional neural networks (CNNs) and Vision Transformers (ViTs). Our
approach involves pre-training a deep neural network on a large dataset and
then fine-tuning the network on the unlabeled target collection with
self-supervised learning. The results show that the proposed approach
outperforms the baseline methods in the task of near-duplicate image detection
in the UKBench and an in-house private dataset.