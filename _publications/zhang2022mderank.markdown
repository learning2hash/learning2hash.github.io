---
layout: publication
title: 'Mderank: A Masked Document Embedding Rank Approach For Unsupervised Keyphrase
  Extraction'
authors: Linhan Zhang, Qian Chen, Wen Wang, Chong Deng, Shiliang Zhang, Bing Li, Wei
  Wang, Xin Cao
conference: 'Findings of the Association for Computational Linguistics: ACL 2022'
year: 2022
bibkey: zhang2022mderank
citations: 33
additional_links: [{name: Code, url: 'https://github.com/LinhanZ/mderank.'}, {name: Paper,
    url: 'https://arxiv.org/abs/2110.06651'}]
tags: ["Evaluation", "Self-Supervised", "Unsupervised"]
short_authors: Zhang et al.
---
Keyphrase extraction (KPE) automatically extracts phrases in a document that
provide a concise summary of the core content, which benefits downstream
information retrieval and NLP tasks. Previous state-of-the-art (SOTA) methods
select candidate keyphrases based on the similarity between learned
representations of the candidates and the document. They suffer performance
degradation on long documents due to discrepancy between sequence lengths which
causes mismatch between representations of keyphrase candidates and the
document. In this work, we propose a novel unsupervised embedding-based KPE
approach, Masked Document Embedding Rank (MDERank), to address this problem by
leveraging a mask strategy and ranking candidates by the similarity between
embeddings of the source document and the masked document. We further develop a
KPE-oriented BERT (KPEBERT) model by proposing a novel self-supervised
contrastive learning method, which is more compatible to MDERank than vanilla
BERT. Comprehensive evaluations on six KPE benchmarks demonstrate that the
proposed MDERank outperforms state-of-the-art unsupervised KPE approach by
average 1.80 \(F1@15\) improvement. MDERank further benefits from KPEBERT and
overall achieves average 3.53 \(F1@15\) improvement over the SOTA SIFRank. Our
code is available at https://github.com/LinhanZ/mderank.