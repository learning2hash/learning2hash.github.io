---
layout: publication
title: Boolean-aware Attention For Dense Retrieval
authors: Quan Mai, Susan Gauch, Douglas Adams
conference: Arxiv
year: 2025
bibkey: mai2025boolean
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2503.01753'}]
tags: ["Datasets"]
short_authors: Quan Mai, Susan Gauch, Douglas Adams
---
We present Boolean-aware attention, a novel attention mechanism that
dynamically adjusts token focus based on Boolean operators (e.g., and, or,
not). Our model employs specialized Boolean experts, each tailored to amplify
or suppress attention for operator-specific contexts. A predefined gating
mechanism activates the corresponding experts based on the detected Boolean
type. Experiments on Boolean retrieval datasets demonstrate that integrating
BoolAttn with BERT greatly enhances the model's capability to process Boolean
queries.