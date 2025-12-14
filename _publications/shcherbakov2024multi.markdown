---
layout: publication
title: Multi-word Term Embeddings Improve Lexical Product Retrieval
authors: Viktor Shcherbakov, Fedor Krasnov
conference: In Proceedings of the Seventh Workshop on e-Commerce and NLP LREC-COLING
  2024 pages 115-124 Torino Italia. ELRA and ICCL
year: 2024
bibkey: shcherbakov2024multi
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.01233'}]
tags: [Evaluation, LREC, Datasets, Tools & Libraries, COLING]
short_authors: Viktor Shcherbakov, Fedor Krasnov
---
Product search is uniquely different from search for documents, Internet
resources or vacancies, therefore it requires the development of specialized
search systems. The present work describes the H1 embdedding model, designed
for an offline term indexing of product descriptions at e-commerce platforms.
The model is compared to other state-of-the-art (SoTA) embedding models within
a framework of hybrid product search system that incorporates the advantages of
lexical methods for product retrieval and semantic embedding-based methods. We
propose an approach to building semantically rich term vocabularies for search
indexes. Compared to other production semantic models, H1 paired with the
proposed approach stands out due to its ability to process multi-word product
terms as one token. As an example, for search queries "new balance shoes",
"gloria jeans kids wear" brand entity will be represented as one token - "new
balance", "gloria jeans". This results in an increased precision of the system
without affecting the recall. The hybrid search system with proposed model
scores mAP@12 = 56.1% and R@1k = 86.6% on the WANDS public dataset, beating
other SoTA analogues.