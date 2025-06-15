---
layout: publication
title: 'Tiger: Unifying Text-to-image Generation And Retrieval With Large Multimodal Models'
authors: Leigang Qu et al.
conference: "Arxiv"
year: 2024
citations: 0
bibkey: qu2024unifying
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2406.05814'}
tags: ['Cross-Modal', 'Retrieval Models', 'Evaluation', 'Shallow', 'Datasets', 'Vector Indexing', 'Supervised', 'Training Strategy', 'Applications']
---
How humans can effectively and efficiently acquire images has always been a
perennial question. A classic solution is text-to-image retrieval from an
existing database; however, the limited database typically lacks creativity. By
contrast, recent breakthroughs in text-to-image generation have made it
possible to produce attractive and counterfactual visual content, but it faces
challenges in synthesizing knowledge-intensive images. In this work, we rethink
the relationship between text-to-image generation and retrieval, proposing a
unified framework for both tasks with one single Large Multimodal Model (LMM).
Specifically, we first explore the intrinsic discriminative abilities of LMMs
and introduce an efficient generative retrieval method for text-to-image
retrieval in a training-free manner. Subsequently, we unify generation and
retrieval autoregressively and propose an autonomous decision mechanism to
choose the best-matched one between generated and retrieved images as the
response to the text prompt. To standardize the evaluation of unified
text-to-image generation and retrieval, we construct TIGeR-Bench, a benchmark
spanning both creative and knowledge-intensive domains. Extensive experiments
on TIGeR-Bench and two retrieval benchmarks, i.e., Flickr30K and MS-COCO,
demonstrate the superiority of our proposed framework.
