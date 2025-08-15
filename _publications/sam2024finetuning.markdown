---
layout: publication
title: Finetuning CLIP To Reason About Pairwise Differences
authors: Dylan Sam, Devin Willmott, Joao D. Semedo, J. Zico Kolter
conference: Arxiv
year: 2024
bibkey: sam2024finetuning
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.09721'}]
tags: ["Datasets", "Evaluation", "Self-Supervised"]
short_authors: Sam et al.
---
Vision-language models (VLMs) such as CLIP are trained via contrastive learning between text and image pairs, resulting in aligned image and text embeddings that are useful for many downstream tasks. A notable drawback of CLIP, however, is that the resulting embedding space seems to lack some of the structure of its purely text-based alternatives. For instance, while text embeddings have long been noted to satisfy analogies in embedding space using vector arithmetic, CLIP has no such property. In this paper, we propose an approach to natively train CLIP in a contrastive manner to reason about differences in embedding space. We finetune CLIP so that text descriptions of differences between images correspond to their difference in image embedding space, using synthetically generated data with large language models on image-caption paired datasets. We first demonstrate that our approach yields significantly improved capabilities in ranking images by a certain attribute (e.g., elephants are larger than cats), which is useful in retrieval or constructing attribute-based classifiers, and improved zeroshot classification performance on many downstream image classification tasks. In addition, our approach enables a new mechanism for inference that we refer to as comparative prompting, where we leverage prior knowledge of text descriptions of differences between classes of interest, achieving even larger performance gains in classification. Finally, we illustrate that the resulting embeddings obey a larger degree of geometric properties in embedding space, such as in text-to-image generation.