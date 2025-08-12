---
layout: publication
title: Improving Few-shot And Zero-shot Entity Linking With Coarse-to-fine Lexicon-based
  Retriever
authors: Shijue Huang, Bingbing Wang, Libo Qin, Qin Zhao, Ruifeng Xu
conference: Arxiv
year: 2023
bibkey: huang2023improving
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.03365'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Huang et al.
---
Few-shot and zero-shot entity linking focus on the tail and emerging
entities, which are more challenging but closer to real-world scenarios. The
mainstream method is the ''retrieve and rerank'' two-stage framework. In this
paper, we propose a coarse-to-fine lexicon-based retriever to retrieve entity
candidates in an effective manner, which operates in two layers. The first
layer retrieves coarse-grained candidates by leveraging entity names, while the
second layer narrows down the search to fine-grained candidates within the
coarse-grained ones. In addition, this second layer utilizes entity
descriptions to effectively disambiguate tail or new entities that share names
with existing popular entities. Experimental results indicate that our approach
can obtain superior performance without requiring extensive finetuning in the
retrieval stage. Notably, our approach ranks the 1st in NLPCC 2023 Shared Task
6 on Chinese Few-shot and Zero-shot Entity Linking.