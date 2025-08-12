---
layout: publication
title: Few-shot Named Entity Recognition With Self-describing Networks
authors: Jiawei Chen, Qing Liu, Hongyu Lin, Xianpei Han, Le Sun
conference: 'Proceedings of the 60th Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)'
year: 2022
bibkey: chen2022few
citations: 37
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.12252'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Chen et al.
---
Few-shot NER needs to effectively capture information from limited instances
and transfer useful knowledge from external resources. In this paper, we
propose a self-describing mechanism for few-shot NER, which can effectively
leverage illustrative instances and precisely transfer knowledge from external
resources by describing both entity types and mentions using a universal
concept set. Specifically, we design Self-describing Networks (SDNet), a
Seq2Seq generation model which can universally describe mentions using
concepts, automatically map novel entity types to concepts, and adaptively
recognize entities on-demand. We pre-train SDNet with large-scale corpus, and
conduct experiments on 8 benchmarks from different domains. Experiments show
that SDNet achieves competitive performances on all benchmarks and achieves the
new state-of-the-art on 6 benchmarks, which demonstrates its effectiveness and
robustness.