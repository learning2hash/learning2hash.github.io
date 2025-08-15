---
layout: publication
title: Optimizing CLIP Models For Image Retrieval With Maintained Joint-embedding
  Alignment
authors: Konstantin Schall, Kai Uwe Barthel, Nico Hezel, Klaus Jung
conference: Arxiv
year: 2024
bibkey: schall2024optimizing
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.01936'}]
tags: ["Evaluation", "Few Shot & Zero Shot", "Image Retrieval", "Multimodal Retrieval", "Robustness", "Similarity Search"]
short_authors: Schall et al.
---
Contrastive Language and Image Pairing (CLIP), a transformative method in
multimedia retrieval, typically trains two neural networks concurrently to
generate joint embeddings for text and image pairs. However, when applied
directly, these models often struggle to differentiate between visually
distinct images that have similar captions, resulting in suboptimal performance
for image-based similarity searches. This paper addresses the challenge of
optimizing CLIP models for various image-based similarity search scenarios,
while maintaining their effectiveness in text-based search tasks such as
text-to-image retrieval and zero-shot classification. We propose and evaluate
two novel methods aimed at refining the retrieval capabilities of CLIP without
compromising the alignment between text and image embeddings. The first method
involves a sequential fine-tuning process: initially optimizing the image
encoder for more precise image retrieval and subsequently realigning the text
encoder to these optimized image embeddings. The second approach integrates
pseudo-captions during the retrieval-optimization phase to foster direct
alignment within the embedding space. Through comprehensive experiments, we
demonstrate that these methods enhance CLIP's performance on various
benchmarks, including image retrieval, k-NN classification, and zero-shot
text-based classification, while maintaining robustness in text-to-image
retrieval. Our optimized models permit maintaining a single embedding per
image, significantly simplifying the infrastructure needed for large-scale
multi-modal similarity search systems.