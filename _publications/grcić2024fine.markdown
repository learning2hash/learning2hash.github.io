---
layout: publication
title: Fine-grained Classes And How To Find Them
authors: "Matej Grci\u0107, Artyom Gadetsky, Maria Brbi\u0107"
conference: Arxiv
year: 2024
bibkey: "grci\u01072024fine"
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.11070'}]
tags: []
short_authors: "Matej Grci\u0107, Artyom Gadetsky, Maria Brbi\u0107"
---
In many practical applications, coarse-grained labels are readily available
compared to fine-grained labels that reflect subtle differences between
classes. However, existing methods cannot leverage coarse labels to infer
fine-grained labels in an unsupervised manner. To bridge this gap, we propose
FALCON, a method that discovers fine-grained classes from coarsely labeled data
without any supervision at the fine-grained level. FALCON simultaneously infers
unknown fine-grained classes and underlying relationships between coarse and
fine-grained classes. Moreover, FALCON is a modular method that can effectively
learn from multiple datasets labeled with different strategies. We evaluate
FALCON on eight image classification tasks and a single-cell classification
task. FALCON outperforms baselines by a large margin, achieving 22% improvement
over the best baseline on the tieredImageNet dataset with over 600 fine-grained
classes.