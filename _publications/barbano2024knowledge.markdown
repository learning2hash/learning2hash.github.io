---
layout: publication
title: Knowledge Transfer Across Modalities With Natural Language Supervision
authors: Carlo Alberto Barbano, Luca Molinaro, Emanuele Aiello, Marco Grangetto
conference: Arxiv
year: 2024
bibkey: barbano2024knowledge
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.15611'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Barbano et al.
---
We present a way to learn novel concepts by only using their textual
description. We call this method Knowledge Transfer. Similarly to human
perception, we leverage cross-modal interaction to introduce new concepts. We
hypothesize that in a pre-trained visual encoder there are enough low-level
features already learned (e.g. shape, appearance, color) that can be used to
describe previously unknown high-level concepts. Provided with a textual
description of the novel concept, our method works by aligning the known
low-level features of the visual encoder to its high-level textual description.
We show that Knowledge Transfer can successfully introduce novel concepts in
multimodal models, in a very efficient manner, by only requiring a single
description of the target concept. Our approach is compatible with both
separate textual and visual encoders (e.g. CLIP) and shared parameters across
modalities. We also show that, following the same principle, Knowledge Transfer
can improve concepts already known by the model. Leveraging Knowledge Transfer
we improve zero-shot performance across different tasks such as classification,
segmentation, image-text retrieval, and captioning.