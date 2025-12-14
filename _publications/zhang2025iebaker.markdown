---
layout: publication
title: 'Iebaker: Improved Remote Sensing Image-text Retrieval Framework Via Eliminate
  Before Align And Keyword Explicit Reasoning'
authors: Yan Zhang, Zhong Ji, Changxu Meng, Yanwei Pang, Jungong Han
conference: Expert Systems with Applications
year: 2025
bibkey: zhang2025iebaker
citations: 0
additional_links: [{name: Code, url: 'https://github.com/zhangy0822/iEBAKER'}, {name: Paper,
    url: 'https://arxiv.org/abs/2504.05644'}]
tags: [Text Retrieval, Evaluation, Tools & Libraries, Datasets]
short_authors: Zhang et al.
---
Recent studies focus on the Remote Sensing Image-Text Retrieval (RSITR),
which aims at searching for the corresponding targets based on the given query.
Among these efforts, the application of Foundation Models (FMs), such as CLIP,
to the domain of remote sensing has yielded encouraging outcomes. However,
existing FM based methodologies neglect the negative impact of weakly
correlated sample pairs and fail to account for the key distinctions among
remote sensing texts, leading to biased and superficial exploration of sample
pairs. To address these challenges, we propose an approach named iEBAKER (an
Improved Eliminate Before Align strategy with Keyword Explicit Reasoning
framework) for RSITR. Specifically, we propose an innovative Eliminate Before
Align (EBA) strategy to filter out the weakly correlated sample pairs, thereby
mitigating their deviations from optimal embedding space during
alignment.Further, two specific schemes are introduced from the perspective of
whether local similarity and global similarity affect each other. On this
basis, we introduce an alternative Sort After Reversed Retrieval (SAR)
strategy, aims at optimizing the similarity matrix via reverse retrieval.
Additionally, we incorporate a Keyword Explicit Reasoning (KER) module to
facilitate the beneficial impact of subtle key concept distinctions. Without
bells and whistles, our approach enables a direct transition from FM to RSITR
task, eliminating the need for additional pretraining on remote sensing data.
Extensive experiments conducted on three popular benchmark datasets demonstrate
that our proposed iEBAKER method surpasses the state-of-the-art models while
requiring less training data. Our source code will be released at
https://github.com/zhangy0822/iEBAKER.