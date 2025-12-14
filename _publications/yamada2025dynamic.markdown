---
layout: publication
title: Dynamic Injection Of Entity Knowledge Into Dense Retrievers
authors: Ikuya Yamada, Ryokan Ri, Takeshi Kojima, Yusuke Iwasawa, Yutaka Matsuo
conference: 'Findings of the Association for Computational Linguistics: EMNLP 2025'
year: 2025
bibkey: yamada2025dynamic
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2507.03922'}]
tags: [EMNLP, Evaluation, Datasets, ACL]
short_authors: Yamada et al.
---
Dense retrievers often struggle with queries involving less-frequent entities due to their limited entity knowledge. We propose the Knowledgeable Passage Retriever (KPR), a BERT-based retriever enhanced with a context-entity attention layer and dynamically updatable entity embeddings. This design enables KPR to incorporate external entity knowledge without retraining. Experiments on three datasets show that KPR consistently improves retrieval accuracy, achieving a substantial 12.6% gain on the EntityQuestions dataset over the model without KPR extensions. When built on the off-the-shelf bge-base retriever, KPR achieves state-of-the-art performance among similarly sized models on two datasets. Code and models will be released soon.