---
layout: publication
title: Text Descriptions Are Compressive And Invariant Representations For Visual
  Learning
authors: Zhili Feng, Anna Bair, J. Zico Kolter
conference: Arxiv
year: 2023
bibkey: feng2023text
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2307.04317'}]
tags: ["Evaluation"]
short_authors: Zhili Feng, Anna Bair, J. Zico Kolter
---
Modern image classification is based upon directly predicting classes via
large discriminative networks, which do not directly contain information about
the intuitive visual features that may constitute a classification decision.
Recently, work in vision-language models (VLM) such as CLIP has provided ways
to specify natural language descriptions of image classes, but typically
focuses on providing single descriptions for each class. In this work, we
demonstrate that an alternative approach, in line with humans' understanding of
multiple visual features per class, can also provide compelling performance in
the robust few-shot learning setting. In particular, we introduce a novel
method, \textit\{SLR-AVD (Sparse Logistic Regression using Augmented Visual
Descriptors)\}. This method first automatically generates multiple visual
descriptions of each class via a large language model (LLM), then uses a VLM to
translate these descriptions to a set of visual feature embeddings of each
image, and finally uses sparse logistic regression to select a relevant subset
of these features to classify each image. Core to our approach is the fact
that, information-theoretically, these descriptive features are more invariant
to domain shift than traditional image embeddings, even though the VLM training
process is not explicitly designed for invariant representation learning. These
invariant descriptive features also compose a better input compression scheme.
When combined with finetuning, we show that SLR-AVD is able to outperform
existing state-of-the-art finetuning approaches on both in-distribution and
out-of-distribution performance.