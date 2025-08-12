---
layout: publication
title: Fine-grained Visual Textual Alignment For Cross-modal Retrieval Using Transformer
  Encoders
authors: "Nicola Messina, Giuseppe Amato, Andrea Esuli, Fabrizio Falchi, Claudio Gennaro,\
  \ St\xE9phane Marchand-maillet"
conference: ACM Transactions on Multimedia Computing, Communications, and Applications
year: 2021
bibkey: messina2020fine
citations: 116
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2008.05231'}]
tags: ["Multimodal Retrieval"]
short_authors: Messina et al.
---
Despite the evolution of deep-learning-based visual-textual processing
systems, precise multi-modal matching remains a challenging task. In this work,
we tackle the task of cross-modal retrieval through image-sentence matching
based on word-region alignments, using supervision only at the global
image-sentence level. Specifically, we present a novel approach called
Transformer Encoder Reasoning and Alignment Network (TERAN). TERAN enforces a
fine-grained match between the underlying components of images and sentences,
i.e., image regions and words, respectively, in order to preserve the
informative richness of both modalities. TERAN obtains state-of-the-art results
on the image retrieval task on both MS-COCO and Flickr30k datasets. Moreover,
on MS-COCO, it also outperforms current approaches on the sentence retrieval
task.
  Focusing on scalable cross-modal information retrieval, TERAN is designed to
keep the visual and textual data pipelines well separated. Cross-attention
links invalidate any chance to separately extract visual and textual features
needed for the online search and the offline indexing steps in large-scale
retrieval systems. In this respect, TERAN merges the information from the two
domains only during the final alignment phase, immediately before the loss
computation. We argue that the fine-grained alignments produced by TERAN pave
the way towards the research for effective and efficient methods for
large-scale cross-modal information retrieval. We compare the effectiveness of
our approach against relevant state-of-the-art methods. On the MS-COCO 1K test
set, we obtain an improvement of 5.7% and 3.5% respectively on the image and
the sentence retrieval tasks on the Recall@1 metric. The code used for the
experiments is publicly available on GitHub at
https://github.com/mesnico/TERAN.