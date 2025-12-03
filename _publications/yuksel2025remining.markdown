---
layout: publication
title: Remining Hard Negatives For Generative Pseudo Labeled Domain Adaptation
authors: Goksenin Yuksel, David Rau, Jaap Kamps
conference: Arxiv
year: 2025
bibkey: yuksel2025remining
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2501.14434'}]
tags: ["Datasets", "Evaluation", "Few Shot & Zero Shot", "Robustness"]
short_authors: Goksenin Yuksel, David Rau, Jaap Kamps
---
Dense retrievers have demonstrated significant potential for neural
information retrieval; however, they exhibit a lack of robustness to domain
shifts, thereby limiting their efficacy in zero-shot settings across diverse
domains. A state-of-the-art domain adaptation technique is Generative Pseudo
Labeling (GPL). GPL uses synthetic query generation and initially mined hard
negatives to distill knowledge from cross-encoder to dense retrievers in the
target domain. In this paper, we analyze the documents retrieved by the
domain-adapted model and discover that these are more relevant to the target
queries than those of the non-domain-adapted model. We then propose refreshing
the hard-negative index during the knowledge distillation phase to mine better
hard negatives. Our remining R-GPL approach boosts ranking performance in 13/14
BEIR datasets and 9/12 LoTTe datasets. Our contributions are (i) analyzing hard
negatives returned by domain-adapted and non-domain-adapted models and (ii)
applying the GPL training with and without hard-negative re-mining in LoTTE and
BEIR datasets.