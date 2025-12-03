---
layout: publication
title: 'Lazyvlm: Neuro-symbolic Approach To Video Analytics'
authors: "Xiangru Jian, Wei Pang, Zhengyuan Dong, Chao Zhang, M. Tamer \xD6zsu"
conference: Arxiv
year: 2025
bibkey: jian2025lazyvlm
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2505.21459'}]
tags: ["Efficiency", "Scalability", "Similarity Search"]
short_authors: Jian et al.
---
Current video analytics approaches face a fundamental trade-off between flexibility and efficiency. End-to-end Vision Language Models (VLMs) often struggle with long-context processing and incur high computational costs, while neural-symbolic methods depend heavily on manual labeling and rigid rule design. In this paper, we introduce LazyVLM, a neuro-symbolic video analytics system that provides a user-friendly query interface similar to VLMs, while addressing their scalability limitation. LazyVLM enables users to effortlessly drop in video data and specify complex multi-frame video queries using a semi-structured text interface for video analytics. To address the scalability limitations of VLMs, LazyVLM decomposes multi-frame video queries into fine-grained operations and offloads the bulk of the processing to efficient relational query execution and vector similarity search. We demonstrate that LazyVLM provides a robust, efficient, and user-friendly solution for querying open-domain video data at scale.