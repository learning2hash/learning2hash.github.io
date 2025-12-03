---
layout: publication
title: Text Embeddings By Weakly-supervised Contrastive Pre-training
authors: Liang Wang, Nan Yang, Xiaolong Huang, Binxing Jiao, Linjun Yang, Daxin Jiang,
  Rangan Majumder, Furu Wei
conference: Arxiv
year: 2022
bibkey: wang2022text
citations: 107
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.03533'}]
tags: ["Datasets", "Evaluation", "Few Shot & Zero Shot", "Scalability", "Supervised"]
short_authors: Wang et al.
---
This paper presents E5, a family of state-of-the-art text embeddings that
transfer well to a wide range of tasks. The model is trained in a contrastive
manner with weak supervision signals from our curated large-scale text pair
dataset (called CCPairs). E5 can be readily used as a general-purpose embedding
model for any tasks requiring a single-vector representation of texts such as
retrieval, clustering, and classification, achieving strong performance in both
zero-shot and fine-tuned settings. We conduct extensive evaluations on 56
datasets from the BEIR and MTEB benchmarks. For zero-shot settings, E5 is the
first model that outperforms the strong BM25 baseline on the BEIR retrieval
benchmark without using any labeled data. When fine-tuned, E5 obtains the best
results on the MTEB benchmark, beating existing embedding models with 40x more
parameters.