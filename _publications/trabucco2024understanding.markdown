---
layout: publication
title: Understanding Visual Concepts Across Models
authors: Brandon Trabucco, Max Gurinas, Kyle Doherty, Ruslan Salakhutdinov
conference: Arxiv
year: 2024
bibkey: trabucco2024understanding
citations: 0
additional_links: [{name: Code, url: 'https://visual-words.github.io'}, {name: Paper,
    url: 'https://arxiv.org/abs/2406.07506'}]
tags: []
short_authors: Trabucco et al.
---
Large multimodal models such as Stable Diffusion can generate, detect, and
classify new visual concepts after fine-tuning just a single word embedding. Do
models learn similar words for the same concepts (i.e. <orange-cat> = orange +
cat)? We conduct a large-scale analysis on three state-of-the-art models in
text-to-image generation, open-set object detection, and zero-shot
classification, and find that new word embeddings are model-specific and
non-transferable. Across 4,800 new embeddings trained for 40 diverse visual
concepts on four standard datasets, we find perturbations within an
\(\epsilon\)-ball to any prior embedding that generate, detect, and classify an
arbitrary concept. When these new embeddings are spliced into new models,
fine-tuning that targets the original model is lost. We show popular soft
prompt-tuning approaches find these perturbative solutions when applied to
visual concept learning tasks, and embeddings for visual concepts are not
transferable. Code for reproducing our work is available at:
https://visual-words.github.io.