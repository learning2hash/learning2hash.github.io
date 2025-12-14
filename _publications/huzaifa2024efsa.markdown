---
layout: publication
title: 'EFSA: Episodic Few-shot Adaptation For Text-to-image Retrieval'
authors: Muhammad Huzaifa, Yova Kementchedjhieva
conference: Arxiv
year: 2024
bibkey: huzaifa2024efsa
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.00139'}]
tags: [Evaluation, Image Retrieval, Few-shot & Zero-shot, Datasets, Robustness, Multimodal
    Retrieval, Tools & Libraries, Text Retrieval]
short_authors: Muhammad Huzaifa, Yova Kementchedjhieva
---
Text-to-image retrieval is a critical task for managing diverse visual
content, but common benchmarks for the task rely on small, single-domain
datasets that fail to capture real-world complexity. Pre-trained
vision-language models tend to perform well with easy negatives but struggle
with hard negatives--visually similar yet incorrect images--especially in
open-domain scenarios. To address this, we introduce Episodic Few-Shot
Adaptation (EFSA), a novel test-time framework that adapts pre-trained models
dynamically to a query's domain by fine-tuning on top-k retrieved candidates
and synthetic captions generated for them. EFSA improves performance across
diverse domains while preserving generalization, as shown in evaluations on
queries from eight highly distinct visual domains and an open-domain retrieval
pool of over one million images. Our work highlights the potential of episodic
few-shot adaptation to enhance robustness in the critical and understudied task
of open-domain text-to-image retrieval.