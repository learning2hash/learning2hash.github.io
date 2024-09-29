---
layout: publication
title: Concepthash Interpretable Fine45;grained Hashing Via Concept Discovery
authors: Ng Kam Woh, Zhu Xiatian, Song Yi-zhe, Xiang Tao
conference: "Arxiv"
year: 2024
bibkey: ng2024concepthash
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2406.08457"}
  - {name: "Code", url: "https://github.com/kamwoh/concepthash"}
tags: ['ARXIV', 'Has Code', 'Image Retrieval', 'Independent']
---
Existing fine45;grained hashing methods typically lack code interpretability as they compute hash code bits holistically using both global and local features. To address this limitation we propose ConceptHash a novel method that achieves sub45;code level interpretability. In ConceptHash each sub45;code corresponds to a human45;understandable concept such as an object part and these concepts are automatically discovered without human annotations. Specifically we leverage a Vision Transformer architecture and introduce concept tokens as visual prompts along with image patch tokens as model inputs. Each concept is then mapped to a specific sub45;code at the model output providing natural sub45;code interpretability. To capture subtle visual differences among highly similar sub45;categories (e.g. bird species) we incorporate language guidance to ensure that the learned hash codes are distinguishable within fine45;grained object classes while maintaining semantic alignment. This approach allows us to develop hash codes that exhibit similarity within families of species while remaining distinct from species in other families. Extensive experiments on four fine45;grained image retrieval benchmarks demonstrate that ConceptHash outperforms previous methods by a significant margin offering unique sub45;code interpretability as an additional benefit. Code at https://github.com/kamwoh/concepthash.
