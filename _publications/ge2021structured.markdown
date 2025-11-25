---
layout: publication
title: Structured Multi-modal Feature Embedding And Alignment For Image-sentence Retrieval
authors: Xuri Ge, Fuhai Chen, Joemon M. Jose, Zhilong Ji, Zhongqin Wu, Xiao Liu
conference: Proceedings of the 29th ACM International Conference on Multimedia
year: 2021
bibkey: ge2021structured
citations: 47
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.02417'}]
tags: ["Evaluation", "Image Retrieval", "Multimodal Retrieval"]
short_authors: Ge et al.
---
The current state-of-the-art image-sentence retrieval methods implicitly
align the visual-textual fragments, like regions in images and words in
sentences, and adopt attention modules to highlight the relevance of
cross-modal semantic correspondences. However, the retrieval performance
remains unsatisfactory due to a lack of consistent representation in both
semantics and structural spaces. In this work, we propose to address the above
issue from two aspects: (i) constructing intrinsic structure (along with
relations) among the fragments of respective modalities, e.g., "dog \(\to\) play
\(\to\) ball" in semantic structure for an image, and (ii) seeking explicit
inter-modal structural and semantic correspondence between the visual and
textual modalities. In this paper, we propose a novel Structured Multi-modal
Feature Embedding and Alignment (SMFEA) model for image-sentence retrieval. In
order to jointly and explicitly learn the visual-textual embedding and the
cross-modal alignment, SMFEA creates a novel multi-modal structured module with
a shared context-aware referral tree. In particular, the relations of the
visual and textual fragments are modeled by constructing Visual Context-aware
Structured Tree encoder (VCS-Tree) and Textual Context-aware Structured Tree
encoder (TCS-Tree) with shared labels, from which visual and textual features
can be jointly learned and optimized. We utilize the multi-modal tree structure
to explicitly align the heterogeneous image-sentence data by maximizing the
semantic and structural similarity between corresponding inter-modal tree
nodes. Extensive experiments on Microsoft COCO and Flickr30K benchmarks
demonstrate the superiority of the proposed model in comparison to the
state-of-the-art methods.