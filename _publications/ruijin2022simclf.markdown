---
layout: publication
title: 'Simclf: A Simple Contrastive Learning Framework For Function-level Binary
  Embeddings'
authors: Sun Ruijin, Guo Shize, Guo Jinhong, Li Wei, Zhan Dazhi, Sun Meng, Pan Zhisong
conference: Arxiv
year: 2022
bibkey: ruijin2022simclf
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.02442'}]
tags: ["Few Shot & Zero Shot", "Robustness", "Self-Supervised", "Unsupervised"]
short_authors: Ruijin et al.
---
Function-level binary code similarity detection is a crucial aspect of
cybersecurity. It enables the detection of bugs and patent infringements in
released software and plays a pivotal role in preventing supply chain attacks.
A practical embedding learning framework relies on the robustness of the
assembly code representation and the accuracy of function-pair annotation,
which is traditionally accomplished using supervised learning-based frameworks.
However, annotating different function pairs with accurate labels poses
considerable challenges. These supervised learning methods can be easily
overtrained and suffer from representation robustness problems. To address
these challenges, we propose SimCLF: A Simple Contrastive Learning Framework
for Function-level Binary Embeddings. We take an unsupervised learning approach
and formulate binary code similarity detection as instance discrimination.
SimCLF directly operates on disassembled binary functions and could be
implemented with any encoder. It does not require manually annotated
information but only augmented data. Augmented data is generated using compiler
optimization options and code obfuscation techniques. The experimental results
demonstrate that SimCLF surpasses the state-of-the-art in accuracy and has a
significant advantage in few-shot settings.