---
layout: publication
title: Fine-grained Video-text Retrieval With Hierarchical Graph Reasoning
authors: Shizhe Chen, Yida Zhao, Qin Jin, Qi Wu
conference: 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2020
bibkey: chen2020fine
citations: 274
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2003.00392'}]
tags: ["CVPR", "Datasets", "Multimodal Retrieval", "Text Retrieval"]
short_authors: Chen et al.
---
Cross-modal retrieval between videos and texts has attracted growing
attentions due to the rapid emergence of videos on the web. The current
dominant approach for this problem is to learn a joint embedding space to
measure cross-modal similarities. However, simple joint embeddings are
insufficient to represent complicated visual and textual details, such as
scenes, objects, actions and their compositions. To improve fine-grained
video-text retrieval, we propose a Hierarchical Graph Reasoning (HGR) model,
which decomposes video-text matching into global-to-local levels. To be
specific, the model disentangles texts into hierarchical semantic graph
including three levels of events, actions, entities and relationships across
levels. Attention-based graph reasoning is utilized to generate hierarchical
textual embeddings, which can guide the learning of diverse and hierarchical
video representations. The HGR model aggregates matchings from different
video-text levels to capture both global and local details. Experimental
results on three video-text datasets demonstrate the advantages of our model.
Such hierarchical decomposition also enables better generalization across
datasets and improves the ability to distinguish fine-grained semantic
differences.