---
layout: publication
title: 'Anypattern: Towards In-context Image Copy Detection'
authors: Wenhao Wang, Yifan Sun, Zhentao Tan, Yi Yang
conference: Arxiv
year: 2024
bibkey: wang2024anypattern
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.13788'}]
tags: []
short_authors: Wang et al.
---
This paper explores in-context learning for image copy detection (ICD), i.e.,
prompting an ICD model to identify replicated images with new tampering
patterns without the need for additional training. The prompts (or the
contexts) are from a small set of image-replica pairs that reflect the new
patterns and are used at inference time. Such in-context ICD has good realistic
value, because it requires no fine-tuning and thus facilitates fast reaction
against the emergence of unseen patterns. To accommodate the "seen
\(\rightarrow\) unseen" generalization scenario, we construct the first
large-scale pattern dataset named AnyPattern, which has the largest number of
tamper patterns (\(90\) for training and \(10\) for testing) among all the existing
ones. We benchmark AnyPattern with popular ICD methods and reveal that existing
methods barely generalize to novel patterns. We further propose a simple
in-context ICD method named ImageStacker. ImageStacker learns to select the
most representative image-replica pairs and employs them as the pattern prompts
in a stacking manner (rather than the popular concatenation manner).
Experimental results show (1) training with our large-scale dataset
substantially benefits pattern generalization (\(+26.66 %\) \(\mu AP\)), (2) the
proposed ImageStacker facilitates effective in-context ICD (another round of
\(+16.75 %\) \(\mu AP\)), and (3) AnyPattern enables in-context ICD, i.e., without
such a large-scale dataset, in-context learning does not emerge even with our
ImageStacker. Beyond the ICD task, we also demonstrate how AnyPattern can
benefit artists, i.e., the pattern retrieval method trained on AnyPattern can
be generalized to identify style mimicry by text-to-image models. The project
is publicly available at https://anypattern.github.io.