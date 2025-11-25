---
layout: publication
title: Do Vision-language Models Understand Compound Nouns?
authors: Sonal Kumar, Sreyan Ghosh, S Sakshi, Utkarsh Tyagi, Dinesh Manocha
conference: 'Proceedings of the 2024 Conference of the North American Chapter of the
  Association for Computational Linguistics: Human Language Technologies (Volume 2:
  Short Papers)'
year: 2024
bibkey: kumar2024do
citations: 0
additional_links: [{name: Code, url: 'https://github.com/sonalkum/Compun'}, {name: Paper,
    url: 'https://arxiv.org/abs/2404.00419'}]
tags: ["Evaluation", "Image Retrieval", "Multimodal Retrieval"]
short_authors: Kumar et al.
---
Open-vocabulary vision-language models (VLMs) like CLIP, trained using
contrastive loss, have emerged as a promising new paradigm for text-to-image
retrieval. However, do VLMs understand compound nouns (CNs) (e.g., lab coat) as
well as they understand nouns (e.g., lab)? We curate Compun, a novel benchmark
with 400 unique and commonly used CNs, to evaluate the effectiveness of VLMs in
interpreting CNs. The Compun benchmark challenges a VLM for text-to-image
retrieval where, given a text prompt with a CN, the task is to select the
correct image that shows the CN among a pair of distractor images that show the
constituent nouns that make up the CN. Next, we perform an in-depth analysis to
highlight CLIPs' limited understanding of certain types of CNs. Finally, we
present an alternative framework that moves beyond hand-written templates for
text prompts widely used by CLIP-like models. We employ a Large Language Model
to generate multiple diverse captions that include the CN as an object in the
scene described by the caption. Our proposed method improves CN understanding
of CLIP by 8.25% on Compun. Code and benchmark are available at:
https://github.com/sonalkum/Compun