---
layout: publication
title: 'SAC: Semantic Attention Composition For Text-conditioned Image Retrieval'
authors: Surgan Jandial, Pinkesh Badjatiya, Pranit Chawla, Ayush Chopra, Mausoom Sarkar,
  Balaji Krishnamurthy
conference: Arxiv
year: 2020
bibkey: jandial2020sac
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2009.01485'}]
tags: ["Evaluation", "Image Retrieval", "Multimodal Retrieval", "Text Retrieval"]
short_authors: Jandial et al.
---
The ability to efficiently search for images is essential for improving the
user experiences across various products. Incorporating user feedback, via
multi-modal inputs, to navigate visual search can help tailor retrieved results
to specific user queries. We focus on the task of text-conditioned image
retrieval that utilizes support text feedback alongside a reference image to
retrieve images that concurrently satisfy constraints imposed by both inputs.
The task is challenging since it requires learning composite image-text
features by incorporating multiple cross-granular semantic edits from text
feedback and then applying the same to visual features. To address this, we
propose a novel framework SAC which resolves the above in two major steps:
"where to see" (Semantic Feature Attention) and "how to change" (Semantic
Feature Modification). We systematically show how our architecture streamlines
the generation of text-aware image features by removing the need for various
modules required by other state-of-art techniques. We present extensive
quantitative, qualitative analysis, and ablation studies, to show that our
architecture SAC outperforms existing techniques by achieving state-of-the-art
performance on 3 benchmark datasets: FashionIQ, Shoes, and Birds-to-Words,
while supporting natural language feedback of varying lengths.