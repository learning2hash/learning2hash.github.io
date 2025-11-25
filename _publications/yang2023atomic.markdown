---
layout: publication
title: 'Atomic: An Image/text Retrieval Test Collection To Support Multimedia Content
  Creation'
authors: "Jheng-Hong Yang, Carlos Lassance, Rafael Sampaio de Rezende, Krishna Srinivasan,\
  \ Miriam Redi, St\xE9phane Clinchant, Jimmy Lin"
conference: Proceedings of the 46th International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2023
bibkey: yang2023atomic
citations: 6
additional_links: [{name: Code, url: 'https://github.com/TREC-AToMiC/AToMiC'}, {name: Paper,
    url: 'https://arxiv.org/abs/2304.01961'}]
tags: ["Datasets", "Multimodal Retrieval", "SIGIR", "Scalability", "Text Retrieval"]
short_authors: Yang et al.
---
This paper presents the AToMiC (Authoring Tools for Multimedia Content)
dataset, designed to advance research in image/text cross-modal retrieval.
While vision-language pretrained transformers have led to significant
improvements in retrieval effectiveness, existing research has relied on
image-caption datasets that feature only simplistic image-text relationships
and underspecified user models of retrieval tasks. To address the gap between
these oversimplified settings and real-world applications for multimedia
content creation, we introduce a new approach for building retrieval test
collections. We leverage hierarchical structures and diverse domains of texts,
styles, and types of images, as well as large-scale image-document associations
embedded in Wikipedia. We formulate two tasks based on a realistic user model
and validate our dataset through retrieval experiments using baseline models.
AToMiC offers a testbed for scalable, diverse, and reproducible multimedia
retrieval research. Finally, the dataset provides the basis for a dedicated
track at the 2023 Text Retrieval Conference (TREC), and is publicly available
at https://github.com/TREC-AToMiC/AToMiC.