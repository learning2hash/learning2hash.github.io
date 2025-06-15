---
layout: publication
title: 'SPAN: Learning Similarity Between Scene Graphs And Images With Transformers'
authors: Yuren Cong, Wentong Liao, Bodo Rosenhahn, Michael Ying Yang
conference: "Arxiv"
year: 2023
citations: 0
bibkey: cong2023learning
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2304.00590'}
tags: ['Cross-Modal', 'Deep', 'Model Design', 'Retrieval Models', 'Evaluation', 'Datasets', 'Vector Indexing', 'Supervised', 'Applications']
---
Learning similarity between scene graphs and images aims to estimate a
similarity score given a scene graph and an image. There is currently no
research dedicated to this task, although it is critical for scene graph
generation and downstream applications. Scene graph generation is
conventionally evaluated by Recall\\(@K\\) and mean Recall\\(@K\\), which measure the
ratio of predicted triplets that appear in the human-labeled triplet set.
However, such triplet-oriented metrics fail to demonstrate the overall semantic
difference between a scene graph and an image and are sensitive to annotation
bias and noise. Using generated scene graphs in the downstream applications is
therefore limited. To address this issue, for the first time, we propose a
Scene graPh-imAge coNtrastive learning framework, SPAN, that can measure the
similarity between scene graphs and images. Our novel framework consists of a
graph Transformer and an image Transformer to align scene graphs and their
corresponding images in the shared latent space. We introduce a novel graph
serialization technique that transforms a scene graph into a sequence with
structural encodings. Based on our framework, we propose R-Precision measuring
image retrieval accuracy as a new evaluation metric for scene graph generation.
We establish new benchmarks on the Visual Genome and Open Images datasets.
Extensive experiments are conducted to verify the effectiveness of SPAN, which
shows great potential as a scene graph encoder.
