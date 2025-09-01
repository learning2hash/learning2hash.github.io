---
layout: publication
title: 'Shop The Look: Building A Large Scale Visual Shopping System At Pinterest'
authors: Raymond Shiau, Hao-Yu Wu, Eric Kim, Yue Li Du, Anqi Guo, Zhiyuan Zhang, Eileen
  Li, Kunlong Gu, Charles Rosenberg, Andrew Zhai
conference: 'KDD ''20: The 26th ACM SIGKDD Conference on Knowledge Discovery and Data
  Mining'
year: 2020
bibkey: shiau2020shop
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.10866'}]
tags: ["Datasets", "Evaluation", "Image Retrieval", "KDD"]
short_authors: Shiau et al.
---
As online content becomes ever more visual, the demand for searching by
visual queries grows correspondingly stronger. Shop The Look is an online
shopping discovery service at Pinterest, leveraging visual search to enable
users to find and buy products within an image. In this work, we provide a
holistic view of how we built Shop The Look, a shopping oriented visual search
system, along with lessons learned from addressing shopping needs. We discuss
topics including core technology across object detection and visual embeddings,
serving infrastructure for realtime inference, and data labeling methodology
for training/evaluation data collection and human evaluation. The user-facing
impacts of our system design choices are measured through offline evaluations,
human relevance judgements, and online A/B experiments. The collective
improvements amount to cumulative relative gains of over 160% in end-to-end
human relevance judgements and over 80% in engagement. Shop The Look is
deployed in production at Pinterest.