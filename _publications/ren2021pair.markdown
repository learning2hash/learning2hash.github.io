---
layout: publication
title: 'PAIR: Leveraging Passage-centric Similarity Relation For Improving Dense Passage
  Retrieval'
authors: Ruiyang Ren, Shangwen Lv, Yingqi Qu, Jing Liu, Wayne Xin Zhao, Qiaoqiao She,
  Hua Wu, Haifeng Wang, Ji-Rong Wen
conference: 'Findings of the Association for Computational Linguistics: ACL-IJCNLP
  2021'
year: 2021
bibkey: ren2021pair
citations: 34
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.06027'}]
tags: ["Datasets", "Similarity Search", "Text Retrieval"]
short_authors: Ren et al.
---
Recently, dense passage retrieval has become a mainstream approach to finding
relevant information in various natural language processing tasks. A number of
studies have been devoted to improving the widely adopted dual-encoder
architecture. However, most of the previous studies only consider query-centric
similarity relation when learning the dual-encoder retriever. In order to
capture more comprehensive similarity relations, we propose a novel approach
that leverages both query-centric and PAssage-centric sImilarity Relations
(called PAIR) for dense passage retrieval. To implement our approach, we make
three major technical contributions by introducing formal formulations of the
two kinds of similarity relations, generating high-quality pseudo labeled data
via knowledge distillation, and designing an effective two-stage training
procedure that incorporates passage-centric similarity relation constraint.
Extensive experiments show that our approach significantly outperforms previous
state-of-the-art models on both MSMARCO and Natural Questions datasets.