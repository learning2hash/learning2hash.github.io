---
layout: publication
title: Adaptive Hierarchical Graph Cut For Multi-granularity Out-of-distribution Detection
authors: Xiang Fang, Arvind Easwaran, Blaise Genest, Ponnuthurai Nagaratnam Suganthan
conference: Arxiv
year: 2024
bibkey: fang2024adaptive
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.15668'}]
tags: ["Datasets", "Evaluation"]
short_authors: Fang et al.
---
This paper focuses on a significant yet challenging task: out-of-distribution
detection (OOD detection), which aims to distinguish and reject test samples
with semantic shifts, so as to prevent models trained on in-distribution (ID)
data from producing unreliable predictions. Although previous works have made
decent success, they are ineffective for real-world challenging applications
since these methods simply regard all unlabeled data as OOD data and ignore the
case that different datasets have different label granularity. For example,
"cat" on CIFAR-10 and "tabby cat" on Tiny-ImageNet share the same semantics but
have different labels due to various label granularity. To this end, in this
paper, we propose a novel Adaptive Hierarchical Graph Cut network (AHGC) to
deeply explore the semantic relationship between different images.
Specifically, we construct a hierarchical KNN graph to evaluate the
similarities between different images based on the cosine similarity. Based on
the linkage and density information of the graph, we cut the graph into
multiple subgraphs to integrate these semantics-similar samples. If the labeled
percentage in a subgraph is larger than a threshold, we will assign the label
with the highest percentage to unlabeled images. To further improve the model
generalization, we augment each image into two augmentation versions, and
maximize the similarity between the two versions. Finally, we leverage the
similarity score for OOD detection. Extensive experiments on two challenging
benchmarks (CIFAR- 10 and CIFAR-100) illustrate that in representative cases,
AHGC outperforms state-of-the-art OOD detection methods by 81.24% on CIFAR-100
and by 40.47% on CIFAR-10 in terms of "FPR95", which shows the effectiveness of
our AHGC.