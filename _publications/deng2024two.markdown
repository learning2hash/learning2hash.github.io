---
layout: publication
title: Two-stream Deep Hashing With Class-specific Centers For Supervised Image Search
authors: Deng Cheng, Yang, Liu, Tao
conference: Arxiv
year: 2024
citations: 63
bibkey: deng2024two
additional_links: [{name: Paper, url: 'https://ieeexplore.ieee.org/document/8833511'}]
tags: [Deep Hashing, Supervised, ANN Search, Evaluation Metrics, Applications]
---
Hashing has been widely used for large-scale approximate nearest neighbor search due to its storage and search efficiency. Recent supervised hashing research has shown that deep learning-based methods can significantly outperform nondeep methods. Most existing supervised deep hashing methods exploit supervisory signals to generate similar and dissimilar image pairs for training. However, natural images can have large intraclass and small interclass variations, which may degrade the accuracy of hash codes. To address this problem, we propose a novel two-stream ConvNet architecture, which learns hash codes with class-specific representation centers. Our basic idea is that if we can learn a unified binary representation for each class as a center and encourage hash codes of images to be close to the corresponding centers, the intraclass variation will be greatly reduced. Accordingly, we design a neural network that leverages label information and outputs a unified binary representation for each class. Moreover, we also design an image network to learn hash codes from images and force these hash codes to be close to the corresponding class-specific centers. These two neural networks are then seamlessly incorporated to create a unified, end-to-end trainable framework. Extensive experiments on three popular benchmarks corroborate that our proposed method outperforms current state-of-the-art methods.