---
layout: publication
title: Unsupervised Multilingual Dense Retrieval Via Generative Pseudo Labeling
authors: Chao-Wei Huang, Chen-An Li, Tsu-Yuan Hsu, Chen-Yu Hsu, Yun-Nung Chen
conference: Arxiv
year: 2024
bibkey: huang2024unsupervised
citations: 1
additional_links: [{name: Code, url: 'https://github.com/MiuLab/UMR'}, {name: Paper,
    url: 'https://arxiv.org/abs/2403.03516'}]
tags: [Evaluation, Supervised, Datasets, Tools & Libraries, Unsupervised]
short_authors: Huang et al.
---
Dense retrieval methods have demonstrated promising performance in
multilingual information retrieval, where queries and documents can be in
different languages. However, dense retrievers typically require a substantial
amount of paired data, which poses even greater challenges in multilingual
scenarios. This paper introduces UMR, an Unsupervised Multilingual dense
Retriever trained without any paired data. Our approach leverages the sequence
likelihood estimation capabilities of multilingual language models to acquire
pseudo labels for training dense retrievers. We propose a two-stage framework
which iteratively improves the performance of multilingual dense retrievers.
Experimental results on two benchmark datasets show that UMR outperforms
supervised baselines, showcasing the potential of training multilingual
retrievers without paired data, thereby enhancing their practicality. Our
source code, data, and models are publicly available at
https://github.com/MiuLab/UMR