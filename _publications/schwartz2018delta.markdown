---
layout: publication
title: 'Delta-encoder: An Effective Sample Synthesis Method For Few-shot Object Recognition'
authors: Eli Schwartz, Leonid Karlinsky, Joseph Shtok, Sivan Harary, Mattias Marder,
  Rogerio Feris, Abhishek Kumar, Raja Giryes, Alex M. Bronstein
conference: Arxiv
year: 2018
bibkey: schwartz2018delta
citations: 166
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1806.04734'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Schwartz et al.
---
Learning to classify new categories based on just one or a few examples is a
long-standing challenge in modern computer vision. In this work, we proposes a
simple yet effective method for few-shot (and one-shot) object recognition. Our
approach is based on a modified auto-encoder, denoted Delta-encoder, that
learns to synthesize new samples for an unseen category just by seeing few
examples from it. The synthesized samples are then used to train a classifier.
The proposed approach learns to both extract transferable intra-class
deformations, or "deltas", between same-class pairs of training examples, and
to apply those deltas to the few provided examples of a novel class (unseen
during training) in order to efficiently synthesize samples from that new
class. The proposed method improves over the state-of-the-art in one-shot
object-recognition and compares favorably in the few-shot case. Upon acceptance
code will be made available.