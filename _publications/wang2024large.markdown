---
layout: publication
title: Large Language Models As Data Augmenters For Cold-start Item Recommendation
authors: Jianling Wang, Haokai Lu, James Caverlee, Ed Chi, Minmin Chen
conference: "Arxiv"
year: 2024
bibkey: wang2024large
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2402.11724v1"}
tags: ['ARXIV']
---
The reasoning and generalization capabilities of LLMs can help us better understand user preferences and item characteristics offering exciting prospects to enhance recommendation systems. Though effective while user-item interactions are abundant conventional recommendation systems struggle to recommend cold-start items without historical interactions. To address this we propose utilizing LLMs as data augmenters to bridge the knowledge gap on cold-start items during training. We employ LLMs to infer user preferences for cold-start items based on textual description of user historical behaviors and new item descriptions. The augmented training signals are then incorporated into learning the downstream recommendation models through an auxiliary pairwise loss. Through experiments on public Amazon datasets we demonstrate that LLMs can effectively augment the training signals for cold-start items leading to significant improvements in cold-start item recommendation for various recommendation models.
