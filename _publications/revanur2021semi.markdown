---
layout: publication
title: Semi-supervised Visual Representation Learning For Fashion Compatibility
authors: Ambareesh Revanur, Vijay Kumar, Deepthi Sharma
conference: Fifteenth ACM Conference on Recommender Systems
year: 2021
bibkey: revanur2021semi
citations: 18
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.08052'}]
tags: []
short_authors: Ambareesh Revanur, Vijay Kumar, Deepthi Sharma
---
We consider the problem of complementary fashion prediction. Existing
approaches focus on learning an embedding space where fashion items from
different categories that are visually compatible are closer to each other.
However, creating such labeled outfits is intensive and also not feasible to
generate all possible outfit combinations, especially with large fashion
catalogs. In this work, we propose a semi-supervised learning approach where we
leverage large unlabeled fashion corpus to create pseudo-positive and
pseudo-negative outfits on the fly during training. For each labeled outfit in
a training batch, we obtain a pseudo-outfit by matching each item in the
labeled outfit with unlabeled items. Additionally, we introduce consistency
regularization to ensure that representation of the original images and their
transformations are consistent to implicitly incorporate colour and other
important attributes through self-supervision. We conduct extensive experiments
on Polyvore, Polyvore-D and our newly created large-scale Fashion Outfits
datasets, and show that our approach with only a fraction of labeled examples
performs on-par with completely supervised methods.