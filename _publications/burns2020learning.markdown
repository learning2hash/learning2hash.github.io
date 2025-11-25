---
layout: publication
title: Learning To Scale Multilingual Representations For Vision-language Tasks
authors: Andrea Burns, Donghyun Kim, Derry Wijaya, Kate Saenko, Bryan A. Plummer
conference: Lecture Notes in Computer Science
year: 2020
bibkey: burns2020learning
citations: 21
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.04312'}]
tags: ["Evaluation", "Image Retrieval", "Multimodal Retrieval", "Scalability"]
short_authors: Burns et al.
---
Current multilingual vision-language models either require a large number of
additional parameters for each supported language, or suffer performance
degradation as languages are added. In this paper, we propose a Scalable
Multilingual Aligned Language Representation (SMALR) that supports many
languages with few model parameters without sacrificing downstream task
performance. SMALR learns a fixed size language-agnostic representation for
most words in a multilingual vocabulary, keeping language-specific features for
just a few. We use a masked cross-language modeling loss to align features with
context from other languages. Additionally, we propose a cross-lingual
consistency module that ensures predictions made for a query and its machine
translation are comparable. The effectiveness of SMALR is demonstrated with ten
diverse languages, over twice the number supported in vision-language tasks to
date. We evaluate on multilingual image-sentence retrieval and outperform prior
work by 3-4% with less than 1/5th the training parameters compared to other
word embedding methods.