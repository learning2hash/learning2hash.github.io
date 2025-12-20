---
layout: publication
title: 'Towards Identity-aware Cross-modal Retrieval: A Dataset And A Baseline'
authors: Nicola Messina, Lucia Vadicamo, Leo Maltese, Claudio Gennaro
conference: Arxiv
year: 2024
bibkey: messina2024towards
citations: 0
additional_links: [{name: Code, url: 'https://github.com/mesnico/IdCLIP'}, {name: Paper,
    url: 'https://arxiv.org/abs/2412.21009'}]
tags: ["Datasets", "Evaluation", "Multimodal Retrieval", "Neural Hashing", "Scalability"]
short_authors: Messina et al.
---
Recent advancements in deep learning have significantly enhanced
content-based retrieval methods, notably through models like CLIP that map
images and texts into a shared embedding space. However, these methods often
struggle with domain-specific entities and long-tail concepts absent from their
training data, particularly in identifying specific individuals. In this paper,
we explore the task of identity-aware cross-modal retrieval, which aims to
retrieve images of persons in specific contexts based on natural language
queries. This task is critical in various scenarios, such as for searching and
browsing personalized video collections or large audio-visual archives
maintained by national broadcasters. We introduce a novel dataset, COCO Person
FaceSwap (COCO-PFS), derived from the widely used COCO dataset and enriched
with deepfake-generated faces from VGGFace2. This dataset addresses the lack of
large-scale datasets needed for training and evaluating models for this task.
Our experiments assess the performance of different CLIP variations repurposed
for this task, including our architecture, Identity-aware CLIP (Id-CLIP), which
achieves competitive retrieval performance through targeted fine-tuning. Our
contributions lay the groundwork for more robust cross-modal retrieval systems
capable of recognizing long-tail identities and contextual nuances. Data and
code are available at https://github.com/mesnico/IdCLIP.