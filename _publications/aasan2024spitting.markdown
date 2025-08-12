---
layout: publication
title: 'A Spitting Image: Modular Superpixel Tokenization In Vision Transformers'
authors: "Marius Aasan, Odd Kolbj\xF8rnsen, Anne Schistad Solberg, Ad\xEDn Ramirez\
  \ Rivera"
conference: Lecture Notes in Computer Science
year: 2025
bibkey: aasan2024spitting
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.07680'}]
tags: []
short_authors: Aasan et al.
---
Vision Transformer (ViT) architectures traditionally employ a grid-based
approach to tokenization independent of the semantic content of an image. We
propose a modular superpixel tokenization strategy which decouples tokenization
and feature extraction; a shift from contemporary approaches where these are
treated as an undifferentiated whole. Using on-line content-aware tokenization
and scale- and shape-invariant positional embeddings, we perform experiments
and ablations that contrast our approach with patch-based tokenization and
randomized partitions as baselines. We show that our method significantly
improves the faithfulness of attributions, gives pixel-level granularity on
zero-shot unsupervised dense prediction tasks, while maintaining predictive
performance in classification tasks. Our approach provides a modular
tokenization framework commensurable with standard architectures, extending the
space of ViTs to a larger class of semantically-rich models.