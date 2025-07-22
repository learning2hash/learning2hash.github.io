---
layout: publication
title: 'Procsim: Proxy-based Confidence For Robust Similarity Learning'
authors: Barbany Oriol, Lin Xiaofan, Bastan Muhammet, Dhua Arnab
conference: 2024 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2024
bibkey: barbany2023procsim
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.00668'}]
tags: ["Tools-&-Libraries", "Evaluation", "Distance-Metric-Learning", "Datasets"]
short_authors: Barbany et al.
---
Deep Metric Learning (DML) methods aim at learning an embedding space in
which distances are closely related to the inherent semantic similarity of the
inputs. Previous studies have shown that popular benchmark datasets often
contain numerous wrong labels, and DML methods are susceptible to them.
Intending to study the effect of realistic noise, we create an ontology of the
classes in a dataset and use it to simulate semantically coherent labeling
mistakes. To train robust DML models, we propose ProcSim, a simple framework
that assigns a confidence score to each sample using the normalized distance to
its class representative. The experimental results show that the proposed
method achieves state-of-the-art performance on the DML benchmark datasets
injected with uniform and the proposed semantically coherent noise.