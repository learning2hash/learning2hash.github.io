---
layout: publication
title: 'The Curious Layperson: Fine-grained Image Recognition Without Expert Labels'
authors: Subhabrata Choudhury, Iro Laina, Christian Rupprecht, Andrea Vedaldi
conference: International Journal of Computer Vision
year: 2023
bibkey: choudhury2021curious
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.03651'}]
tags: ["Datasets"]
short_authors: Choudhury et al.
---
Most of us are not experts in specific fields, such as ornithology.
Nonetheless, we do have general image and language understanding capabilities
that we use to match what we see to expert resources. This allows us to expand
our knowledge and perform novel tasks without ad-hoc external supervision. On
the contrary, machines have a much harder time consulting expert-curated
knowledge bases unless trained specifically with that knowledge in mind. Thus,
in this paper we consider a new problem: fine-grained image recognition without
expert annotations, which we address by leveraging the vast knowledge available
in web encyclopedias. First, we learn a model to describe the visual appearance
of objects using non-expert image descriptions. We then train a fine-grained
textual similarity model that matches image descriptions with documents on a
sentence-level basis. We evaluate the method on two datasets and compare with
several strong baselines and the state of the art in cross-modal retrieval.
Code is available at: https://github.com/subhc/clever