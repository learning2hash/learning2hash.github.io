---
layout: publication
title: 'Synergizing Implicit And Explicit User Interests: A Multi-embedding Retrieval
  Framework At Pinterest'
authors: Fan et al.
conference: Social Cognitive and Affective Neuroscience
year: 2025
bibkey: fan2025synergizing
citations: 356
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2506.23060'}]
tags: ["Tools-&-Libraries"]
---
Industrial recommendation systems are typically composed of multiple stages, including retrieval, ranking, and blending. The retrieval stage plays a critical role in generating a high-recall set of candidate items that covers a wide range of diverse user interests. Effectively covering the diverse and long-tail user interests within this stage poses a significant challenge: traditional two-tower models struggle in this regard due to limited user-item feature interaction and often bias towards top use cases. To address these issues, we propose a novel multi-embedding retrieval framework designed to enhance user interest representation by generating multiple user embeddings conditioned on both implicit and explicit user interests. Implicit interests are captured from user history through a Differentiable Clustering Module (DCM), whereas explicit interests, such as topics that the user has followed, are modeled via Conditional Retrieval (CR). These methodologies represent a form of conditioned user representation learning that involves condition representation construction and associating the target item with the relevant conditions. Synergizing implicit and explicit user interests serves as a complementary approach to achieve more effective and comprehensive candidate retrieval as they benefit on different user segments and extract conditions from different but supplementary sources. Extensive experiments and A/B testing reveal significant improvements in user engagements and feed diversity metrics. Our proposed framework has been successfully deployed on Pinterest home feed.