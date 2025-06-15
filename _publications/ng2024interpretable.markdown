---
layout: publication
title: 'Concepthash: Interpretable Fine-grained Hashing Via Concept Discovery'
authors: Kam Woh Ng, Xiatian Zhu, Yi-zhe Song, Tao Xiang
conference: "Arxiv"
year: 2024
citations: 0
bibkey: ng2024interpretable
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2406.08457'}
  - {name: "Code", url: 'https://github.com/kamwoh/concepthash'}
tags: ['Cross-Modal', 'Independent', 'Retrieval Models', 'Shallow', 'Vector Indexing', 'Has Code', 'Hashing', 'Applications']
---
Existing fine-grained hashing methods typically lack code interpretability as
they compute hash code bits holistically using both global and local features.
To address this limitation, we propose ConceptHash, a novel method that
achieves sub-code level interpretability. In ConceptHash, each sub-code
corresponds to a human-understandable concept, such as an object part, and
these concepts are automatically discovered without human annotations.
Specifically, we leverage a Vision Transformer architecture and introduce
concept tokens as visual prompts, along with image patch tokens as model
inputs. Each concept is then mapped to a specific sub-code at the model output,
providing natural sub-code interpretability. To capture subtle visual
differences among highly similar sub-categories (e.g., bird species), we
incorporate language guidance to ensure that the learned hash codes are
distinguishable within fine-grained object classes while maintaining semantic
alignment. This approach allows us to develop hash codes that exhibit
similarity within families of species while remaining distinct from species in
other families. Extensive experiments on four fine-grained image retrieval
benchmarks demonstrate that ConceptHash outperforms previous methods by a
significant margin, offering unique sub-code interpretability as an additional
benefit. Code at: https://github.com/kamwoh/concepthash.
