---
layout: publication
title: Deep Transfer Hashing For Adaptive Learning On Federated Streaming Data
authors: "Manuel R\xF6der, Frank-Michael Schleif"
conference: Arxiv
year: 2024
bibkey: "r\xF6der2024deep"
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.12575'}]
tags: [Hashing Methods, Efficiency, Tools & Libraries, Scalability]
short_authors: "Manuel R\xF6der, Frank-Michael Schleif"
---
This extended abstract explores the integration of federated learning with
deep transfer hashing for distributed prediction tasks, emphasizing
resource-efficient client training from evolving data streams. Federated
learning allows multiple clients to collaboratively train a shared model while
maintaining data privacy - by incorporating deep transfer hashing,
high-dimensional data can be converted into compact hash codes, reducing data
transmission size and network loads. The proposed framework utilizes transfer
learning, pre-training deep neural networks on a central server, and
fine-tuning on clients to enhance model accuracy and adaptability. A selective
hash code sharing mechanism using a privacy-preserving global memory bank
further supports client fine-tuning. This approach addresses challenges in
previous research by improving computational efficiency and scalability.
Practical applications include Car2X event predictions, where a shared model is
collectively trained to recognize traffic patterns, aiding in tasks such as
traffic density assessment and accident detection. The research aims to develop
a robust framework that combines federated learning, deep transfer hashing and
transfer learning for efficient and secure downstream task execution.