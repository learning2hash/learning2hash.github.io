---
layout: publication
title: 'Clean Image May Be Dangerous: Data Poisoning Attacks Against Deep Hashing'
authors: Li et al.
conference: Lecture Notes in Computer Science
year: 2025
bibkey: li2025clean
citations: 61
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2503.21236'}]
tags: ["Neural Hashing", "Hashing Methods"]
---
Large-scale image retrieval using deep hashing has become increasingly
popular due to the exponential growth of image data and the remarkable feature
extraction capabilities of deep neural networks (DNNs). However, deep hashing
methods are vulnerable to malicious attacks, including adversarial and backdoor
attacks. It is worth noting that these attacks typically involve altering the
query images, which is not a practical concern in real-world scenarios. In this
paper, we point out that even clean query images can be dangerous, inducing
malicious target retrieval results, like undesired or illegal images. To the
best of our knowledge, we are the first to study data \textbf\{p\}oisoning
\textbf\{a\}ttacks against \textbf\{d\}eep \textbf\{hash\}ing
\textbf\{(\textit\{PADHASH\})\}. Specifically, we first train a surrogate model to
simulate the behavior of the target deep hashing model. Then, a strict gradient
matching strategy is proposed to generate the poisoned images. Extensive
experiments on different models, datasets, hash methods, and hash code lengths
demonstrate the effectiveness and generality of our attack method.