---
layout: publication
title: From Coarse To Fine-grained Concept Based Discrimination For Phrase Detection
authors: Maan Qraitem, Bryan A. Plummer
conference: Arxiv
year: 2021
bibkey: qraitem2021coarse
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.03237'}]
tags: []
short_authors: Maan Qraitem, Bryan A. Plummer
---
Phrase detection requires methods to identify if a phrase is relevant to an
image and localize it, if applicable. A key challenge for training more
discriminative detection models is sampling negatives. Sampling techniques from
prior work focus primarily on hard, often noisy, negatives disregarding the
broader distribution of negative samples. Our proposed CFCD-Net addresses this
through two novels methods. First, we generate groups of semantically similar
words we call concepts (\eg, \\{dog, cat, horse\\} and \ \\{car, truck, SUV\\}),
and then train our CFCD-Net to discriminate between a region of interest and
its unrelated concepts. Second, for phrases containing fine-grained
mutually-exclusive words (\eg, colors), we force the model to select only one
applicable phrase for each region using our novel fine-grained module (FGM). We
evaluate our approach on Flickr30K Entities and RefCOCO+, where we improve mAP
over the state-of-the-art by 1.5-2 points. When considering only the phrases
affected by our FGM module, we improve by 3-4 points on both datasets.