---
layout: publication
title: Improving Cross-modal Retrieval With Set Of Diverse Embeddings
authors: Dongwon Kim, Namyup Kim, Suha Kwak
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: kim2022improving
citations: 29
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.16761'}]
tags: ["CVPR", "Datasets", "Multimodal Retrieval"]
short_authors: Dongwon Kim, Namyup Kim, Suha Kwak
---
Cross-modal retrieval across image and text modalities is a challenging task
due to its inherent ambiguity: An image often exhibits various situations, and
a caption can be coupled with diverse images. Set-based embedding has been
studied as a solution to this problem. It seeks to encode a sample into a set
of different embedding vectors that capture different semantics of the sample.
In this paper, we present a novel set-based embedding method, which is distinct
from previous work in two aspects. First, we present a new similarity function
called smooth-Chamfer similarity, which is designed to alleviate the side
effects of existing similarity functions for set-based embedding. Second, we
propose a novel set prediction module to produce a set of embedding vectors
that effectively captures diverse semantics of input by the slot attention
mechanism. Our method is evaluated on the COCO and Flickr30K datasets across
different visual backbones, where it outperforms existing methods including
ones that demand substantially larger computation at inference.