---
layout: publication
title: 'Optimizing Domain-specific Image Retrieval: A Benchmark Of FAISS And Annoy
  With Fine-tuned Features'
authors: Md Shaikh Rahman, Syed Maudud E Rabbi, Muhammad Mahbubur Rashid
conference: Arxiv
year: 2024
bibkey: rahman2024optimizing
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.01555'}]
tags: ["Datasets", "Efficiency", "Evaluation", "Image Retrieval", "Memory Efficiency", "Quantization", "Tools & Libraries", "Vector Indexing"]
short_authors: Md Shaikh Rahman, Syed Maudud E Rabbi, Muhammad Mahbubur Rashid
---
Approximate Nearest Neighbor search is one of the keys to high-scale data
retrieval performance in many applications. The work is a bridge between
feature extraction and ANN indexing through fine-tuning a ResNet50 model with
various ANN methods: FAISS and Annoy. We evaluate the systems with respect to
indexing time, memory usage, query time, precision, recall, F1-score, and
Recall@5 on a custom image dataset. FAISS's Product Quantization can achieve a
precision of 98.40% with low memory usage at 0.24 MB index size, and Annoy is
the fastest, with average query times of 0.00015 seconds, at a slight cost to
accuracy. These results reveal trade-offs among speed, accuracy, and memory
efficiency and offer actionable insights into the optimization of feature-based
image retrieval systems. This study will serve as a blueprint for constructing
actual retrieval pipelines and be built on fine-tuned deep learning networks
and associated ANN methods.