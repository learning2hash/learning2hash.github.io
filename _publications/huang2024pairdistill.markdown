---
layout: publication
title: 'Pairdistill: Pairwise Relevance Distillation For Dense Retrieval'
authors: Chao-wei Huang, Yun-nung Chen
conference: Proceedings of the 2024 Conference on Empirical Methods in Natural Language
  Processing
year: 2024
bibkey: huang2024pairdistill
citations: 0
additional_links: [{name: Code, url: 'https://github.com/MiuLab/PairDistill'}, {name: Paper,
    url: 'https://arxiv.org/abs/2410.01383'}]
tags: ["Datasets", "EMNLP", "Evaluation"]
short_authors: Chao-wei Huang, Yun-nung Chen
---
Effective information retrieval (IR) from vast datasets relies on advanced
techniques to extract relevant information in response to queries. Recent
advancements in dense retrieval have showcased remarkable efficacy compared to
traditional sparse retrieval methods. To further enhance retrieval performance,
knowledge distillation techniques, often leveraging robust cross-encoder
rerankers, have been extensively explored. However, existing approaches
primarily distill knowledge from pointwise rerankers, which assign absolute
relevance scores to documents, thus facing challenges related to inconsistent
comparisons. This paper introduces Pairwise Relevance Distillation
(PairDistill) to leverage pairwise reranking, offering fine-grained
distinctions between similarly relevant documents to enrich the training of
dense retrieval models. Our experiments demonstrate that PairDistill
outperforms existing methods, achieving new state-of-the-art results across
multiple benchmarks. This highlights the potential of PairDistill in advancing
dense retrieval techniques effectively. Our source code and trained models are
released at https://github.com/MiuLab/PairDistill