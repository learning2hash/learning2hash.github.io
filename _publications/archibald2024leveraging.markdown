---
layout: publication
title: Leveraging Semantic Segmentation Masks With Embeddings For Fine-grained Form
  Classification
authors: Taylor Archibald, Tony Martinez
conference: Arxiv
year: 2024
bibkey: archibald2024leveraging
citations: 0
additional_links: [{name: Code, url: 'https://github.com/tahlor/census_forms'}, {
    name: Paper, url: 'https://arxiv.org/abs/2405.14162'}]
tags: []
short_authors: Taylor Archibald, Tony Martinez
---
Efficient categorization of historical documents is crucial for fields such
as genealogy, legal research, and historical scholarship, where manual
classification is impractical for large collections due to its labor-intensive
and error-prone nature. To address this, we propose a representational learning
strategy that integrates semantic segmentation and deep learning models such as
ResNet, CLIP, Document Image Transformer (DiT), and masked auto-encoders (MAE),
to generate embeddings that capture document features without predefined
labels. To the best of our knowledge, we are the first to evaluate embeddings
on fine-grained, unsupervised form classification. To improve these embeddings,
we propose to first employ semantic segmentation as a preprocessing step. We
contribute two novel datasets\(\unicode\{x2014\}\)the French 19th-century and U.S.
1950 Census records\(\unicode\{x2014\}\)to demonstrate our approach. Our results
show the effectiveness of these various embedding techniques in distinguishing
similar document types and indicate that applying semantic segmentation can
greatly improve clustering and classification results. The census datasets are
available at https://github.com/tahlor/census_forms