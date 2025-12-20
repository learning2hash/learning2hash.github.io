---
layout: publication
title: 'Espresso: Robust Concept Filtering In Text-to-image Models'
authors: Anudeep Das, Vasisht Duddu, Rui Zhang, N. Asokan
conference: Arxiv
year: 2024
bibkey: das2024espresso
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.19227'}]
tags: ["Datasets", "Robustness"]
short_authors: Das et al.
---
Diffusion based text-to-image models are trained on large datasets scraped
from the Internet, potentially containing unacceptable concepts (e.g.,
copyright-infringing or unsafe). We need concept removal techniques (CRTs)
which are i) effective in preventing the generation of images with unacceptable
concepts, ii) utility-preserving on acceptable concepts, and, iii) robust
against evasion with adversarial prompts. No prior CRT satisfies all these
requirements simultaneously. We introduce Espresso, the first robust concept
filter based on Contrastive Language-Image Pre-Training (CLIP). We identify
unacceptable concepts by using the distance between the embedding of a
generated image to the text embeddings of both unacceptable and acceptable
concepts. This lets us fine-tune for robustness by separating the text
embeddings of unacceptable and acceptable concepts while preserving utility. We
present a pipeline to evaluate various CRTs to show that Espresso is more
effective and robust than prior CRTs, while retaining utility.