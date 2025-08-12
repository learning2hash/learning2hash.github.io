---
layout: publication
title: 'Kairacters: Character-level-based Writer Retrieval For Greek Papyri'
authors: Marco Peer, Robert Sablatnig, Olga Serbaeva, Isabelle Marthot-Santaniello
conference: Lecture Notes in Computer Science
year: 2024
bibkey: peer2024kairacters
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.07536'}]
tags: ["Datasets", "Evaluation"]
short_authors: Peer et al.
---
This paper presents a character-based approach for enhancing writer retrieval
performance in the context of Greek papyri. Our contribution lies in
introducing character-level annotations for frequently used characters, in our
case the trigram kai and four additional letters (epsilon, kappa, mu, omega),
in Greek texts. We use a state-of-the-art writer retrieval approach based on
NetVLAD and compare a character-level-based feature aggregation method against
the current default baseline of using small patches located at SIFT keypoint
locations for building the page descriptors. We demonstrate that by using only
about 15 characters per page, we are able to boost the performance up to 4% mAP
(a relative improvement of 11%) on the GRK-120 dataset. Additionally, our
qualitative analysis offers insights into the similarity scores of SIFT patches
and specific characters. We publish the dataset with character-level
annotations, including a quality label and our binarized images for further
research.