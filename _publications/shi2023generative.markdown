---
layout: publication
title: Generative Multimodal Entity Linking
authors: Senbao Shi, Zhenran Xu, Baotian Hu, Min Zhang
conference: Arxiv
year: 2023
bibkey: shi2023generative
citations: 2
additional_links: [{name: Code, url: 'https://github.com/HITsz-TMG/GEMEL'}, {name: Paper,
    url: 'https://arxiv.org/abs/2306.12725'}]
tags: []
short_authors: Shi et al.
---
Multimodal Entity Linking (MEL) is the task of mapping mentions with
multimodal contexts to the referent entities from a knowledge base. Existing
MEL methods mainly focus on designing complex multimodal interaction mechanisms
and require fine-tuning all model parameters, which can be prohibitively costly
and difficult to scale in the era of Large Language Models (LLMs). In this
work, we propose GEMEL, a Generative Multimodal Entity Linking framework based
on LLMs, which directly generates target entity names. We keep the vision and
language model frozen and only train a feature mapper to enable cross-modality
interactions. To adapt LLMs to the MEL task, we leverage the in-context
learning capability of LLMs by retrieving multimodal instances as
demonstrations. Extensive experiments show that, with only ~0.3% of the model
parameters fine-tuned, GEMEL achieves state-of-the-art results on two
well-established MEL datasets (7.7% accuracy gains on WikiDiverse and 8.8%
accuracy gains on WikiMEL). The performance gain stems from mitigating the
popularity bias of LLM predictions and disambiguating less common entities
effectively. Further analysis verifies the generality and scalability of GEMEL.
Our framework is compatible with any off-the-shelf language model, paving the
way towards an efficient and general solution for utilizing LLMs in the MEL
task. Our code is available at https://github.com/HITsz-TMG/GEMEL.