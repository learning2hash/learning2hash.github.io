---
layout: publication
title: Decompose Semantic Shifts For Composed Image Retrieval
authors: Xingyu Yang, Daqing Liu, Heng Zhang, Yong Luo, Chaoyue Wang, Jing Zhang
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2024
bibkey: yang2023decompose
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.09531'}]
tags: ["AAAI", "Image Retrieval"]
short_authors: Yang et al.
---
Composed image retrieval is a type of image retrieval task where the user
provides a reference image as a starting point and specifies a text on how to
shift from the starting point to the desired target image. However, most
existing methods focus on the composition learning of text and reference images
and oversimplify the text as a description, neglecting the inherent structure
and the user's shifting intention of the texts. As a result, these methods
typically take shortcuts that disregard the visual cue of the reference images.
To address this issue, we reconsider the text as instructions and propose a
Semantic Shift network (SSN) that explicitly decomposes the semantic shifts
into two steps: from the reference image to the visual prototype and from the
visual prototype to the target image. Specifically, SSN explicitly decomposes
the instructions into two components: degradation and upgradation, where the
degradation is used to picture the visual prototype from the reference image,
while the upgradation is used to enrich the visual prototype into the final
representations to retrieve the desired target image. The experimental results
show that the proposed SSN demonstrates a significant improvement of 5.42% and
1.37% on the CIRR and FashionIQ datasets, respectively, and establishes a new
state-of-the-art performance. Codes will be publicly available.