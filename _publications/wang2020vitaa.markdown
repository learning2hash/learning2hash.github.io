---
layout: publication
title: 'Vitaa: Visual-textual Attributes Alignment In Person Search By Natural Language'
authors: Zhe Wang, Zhiyuan Fang, Jun Wang, Yezhou Yang
conference: Lecture Notes in Computer Science
year: 2020
bibkey: wang2020vitaa
citations: 145
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2005.07327'}]
tags: [Scalability, Tools & Libraries, Evaluation]
short_authors: Wang et al.
---
Person search by natural language aims at retrieving a specific person in a
large-scale image pool that matches the given textual descriptions. While most
of the current methods treat the task as a holistic visual and textual feature
matching one, we approach it from an attribute-aligning perspective that allows
grounding specific attribute phrases to the corresponding visual regions. We
achieve success as well as the performance boosting by a robust feature
learning that the referred identity can be accurately bundled by multiple
attribute visual cues. To be concrete, our Visual-Textual Attribute Alignment
model (dubbed as ViTAA) learns to disentangle the feature space of a person
into subspaces corresponding to attributes using a light auxiliary attribute
segmentation computing branch. It then aligns these visual features with the
textual attributes parsed from the sentences by using a novel contrastive
learning loss. Upon that, we validate our ViTAA framework through extensive
experiments on tasks of person search by natural language and by
attribute-phrase queries, on which our system achieves state-of-the-art
performances. Code will be publicly available upon publication.