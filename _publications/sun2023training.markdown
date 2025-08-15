---
layout: publication
title: Training-free Zero-shot Composed Image Retrieval With Local Concept Reranking
authors: Shitong Sun, Fanghua Ye, Shaogang Gong
conference: Arxiv
year: 2023
bibkey: sun2023training
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.08924'}]
tags: ["Efficiency", "Few Shot & Zero Shot", "Image Retrieval", "Re-Ranking", "Self-Supervised"]
short_authors: Shitong Sun, Fanghua Ye, Shaogang Gong
---
Composed image retrieval attempts to retrieve an image of interest from
gallery images through a composed query of a reference image and its
corresponding modified text. It has recently attracted attention due to the
collaboration of information-rich images and concise language to precisely
express the requirements of target images. Most current composed image
retrieval methods follow a supervised learning approach to training on a costly
triplet dataset composed of a reference image, modified text, and a
corresponding target image. To avoid difficult to-obtain labeled triplet
training data, zero-shot composed image retrieval (ZS-CIR) has been introduced,
which aims to retrieve the target image by learning from image-text pairs
(self-supervised triplets), without the need for human-labeled triplets.
However, this self-supervised triplet learning approach is computationally less
effective and less understandable as it assumes the interaction between image
and text is conducted with implicit query embedding without explicit semantical
interpretation. In this work, we present a new training-free zero-shot composed
image retrieval method which translates the query into explicit
human-understandable text. This helps improve model learning efficiency to
enhance the generalization capacity of foundation models. Further, we introduce
a Local Concept Re-ranking (LCR) mechanism to focus on discriminative local
information extracted from the modified instructions. Extensive experiments on
four ZS-CIR benchmarks show that our method achieves comparable performances to
that of the state of-the-art triplet training based methods, but significantly
outperforms other training-free methods on the open domain datasets (CIRR,
CIRCO and COCO), as well as the fashion domain dataset (FashionIQ).