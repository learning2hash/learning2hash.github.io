---
layout: publication
title: Cross-modal Scene Graph Matching For Relationship-aware Image-text Retrieval
authors: Sijin Wang, Ruiping Wang, Ziwei Yao, Shiguang Shan, Xilin Chen
conference: Arxiv
year: 2019
bibkey: wang2019cross
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1910.05134'}]
tags: ["Image Retrieval", "Multimodal Retrieval", "Text Retrieval"]
short_authors: Wang et al.
---
Image-text retrieval of natural scenes has been a popular research topic.
Since image and text are heterogeneous cross-modal data, one of the key
challenges is how to learn comprehensive yet unified representations to express
the multi-modal data. A natural scene image mainly involves two kinds of visual
concepts, objects and their relationships, which are equally essential to
image-text retrieval. Therefore, a good representation should account for both
of them. In the light of recent success of scene graph in many CV and NLP tasks
for describing complex natural scenes, we propose to represent image and text
with two kinds of scene graphs: visual scene graph (VSG) and textual scene
graph (TSG), each of which is exploited to jointly characterize objects and
relationships in the corresponding modality. The image-text retrieval task is
then naturally formulated as cross-modal scene graph matching. Specifically, we
design two particular scene graph encoders in our model for VSG and TSG, which
can refine the representation of each node on the graph by aggregating
neighborhood information. As a result, both object-level and relationship-level
cross-modal features can be obtained, which favorably enables us to evaluate
the similarity of image and text in the two levels in a more plausible way. We
achieve state-of-the-art results on Flickr30k and MSCOCO, which verifies the
advantages of our graph matching based approach for image-text retrieval.