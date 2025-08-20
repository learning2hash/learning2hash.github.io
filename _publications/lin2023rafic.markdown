---
layout: publication
title: 'RAFIC: Retrieval-augmented Few-shot Image Classification'
authors: Hangfei Lin, Li Miao, Amir Ziai
conference: Arxiv
year: 2023
bibkey: lin2023rafic
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.06868'}]
tags: [Evaluation, Tools & Libraries, Datasets, Few-shot & Zero-shot]
short_authors: Hangfei Lin, Li Miao, Amir Ziai
---
Few-shot image classification is the task of classifying unseen images to one
of N mutually exclusive classes, using only a small number of training examples
for each class. The limited availability of these examples (denoted as K)
presents a significant challenge to classification accuracy in some cases. To
address this, we have developed a method for augmenting the set of K with an
addition set of A retrieved images. We call this system Retrieval-Augmented
Few-shot Image Classification (RAFIC). Through a series of experiments, we
demonstrate that RAFIC markedly improves performance of few-shot image
classification across two challenging datasets. RAFIC consists of two main
components: (a) a retrieval component which uses CLIP, LAION-5B, and faiss, in
order to efficiently retrieve images similar to the supplied images, and (b)
retrieval meta-learning, which learns to judiciously utilize the retrieved
images. Code and data is available at github.com/amirziai/rafic.