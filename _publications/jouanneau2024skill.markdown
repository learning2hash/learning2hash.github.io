---
layout: publication
title: 'Skill Matching At Scale: Freelancer-project Alignment For Efficient Multilingual
  Candidate Retrieval'
authors: Warren Jouanneau, Marc Palyart, Emma Jouffroy
conference: Arxiv
year: 2024
bibkey: jouanneau2024skill
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.12097'}]
tags: [Distance Metric Learning]
short_authors: Warren Jouanneau, Marc Palyart, Emma Jouffroy
---
Finding the perfect match between a job proposal and a set of freelancers is
not an easy task to perform at scale, especially in multiple languages. In this
paper, we propose a novel neural retriever architecture that tackles this
problem in a multilingual setting. Our method encodes project descriptions and
freelancer profiles by leveraging pre-trained multilingual language models. The
latter are used as backbone for a custom transformer architecture that aims to
keep the structure of the profiles and project. This model is trained with a
contrastive loss on historical data. Thanks to several experiments, we show
that this approach effectively captures skill matching similarity and
facilitates efficient matching, outperforming traditional methods.