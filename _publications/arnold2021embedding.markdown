---
layout: publication
title: Embedding Adaptation Is Still Needed For Few-shot Learning
authors: "S\xE9bastien M. R. Arnold, Fei Sha"
conference: Arxiv
year: 2021
bibkey: arnold2021embedding
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.07255'}]
tags: ["Few Shot & Zero Shot"]
short_authors: "S\xE9bastien M. R. Arnold, Fei Sha"
---
Constructing new and more challenging tasksets is a fruitful methodology to
analyse and understand few-shot classification methods. Unfortunately, existing
approaches to building those tasksets are somewhat unsatisfactory: they either
assume train and test task distributions to be identical -- which leads to
overly optimistic evaluations -- or take a "worst-case" philosophy -- which
typically requires additional human labor such as obtaining semantic class
relationships. We propose ATG, a principled clustering method to defining train
and test tasksets without additional human knowledge. ATG models train and test
task distributions while requiring them to share a predefined amount of
information. We empirically demonstrate the effectiveness of ATG in generating
tasksets that are easier, in-between, or harder than existing benchmarks,
including those that rely on semantic information. Finally, we leverage our
generated tasksets to shed a new light on few-shot classification:
gradient-based methods -- previously believed to underperform -- can outperform
metric-based ones when transfer is most challenging.