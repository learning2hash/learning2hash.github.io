---
layout: publication
title: 'Less Is More: Pre-train A Strong Text Encoder For Dense Retrieval Using A
  Weak Decoder'
authors: Lu et al.
conference: Proceedings of the 2021 Conference on Empirical Methods in Natural Language
  Processing
year: 2021
bibkey: lu2021less
citations: 24
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.09206'}]
tags: [EMNLP]
---
Dense retrieval requires high-quality text sequence embeddings to support
effective search in the representation space. Autoencoder-based language models
are appealing in dense retrieval as they train the encoder to output
high-quality embedding that can reconstruct the input texts. However, in this
paper, we provide theoretical analyses and show empirically that an autoencoder
language model with a low reconstruction loss may not provide good sequence
representations because the decoder may take shortcuts by exploiting language
patterns. To address this, we propose a new self-learning method that
pre-trains the autoencoder using a \textit\{weak\} decoder, with restricted
capacity and attention flexibility to push the encoder to provide better text
representations. Our experiments on web search, news recommendation, and open
domain question answering show that our pre-trained model significantly boosts
the effectiveness and few-shot ability of dense retrieval models. Our code is
available at https://github.com/microsoft/SEED-Encoder/.