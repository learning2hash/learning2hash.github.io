---
layout: publication
title: Hashreid Dynamic Network With Binary Codes For Efficient Person Re-identification
authors: Nikhal Kshitij, Ma Yujunrong, Bhattacharyya Shuvra S., Riggan Benjamin S.
conference: "Arxiv"
year: 2023
bibkey: nikhal2023hashreid
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2308.11900"}
tags: ['ARXIV', 'Independent']
---
Biometric applications, such as person re-identification (ReID), are often deployed on energy constrained devices. While recent ReID methods prioritize high retrieval performance, they often come with large computational costs and high search time, rendering them less practical in real-world settings. In this work, we propose an input-adaptive network with multiple exit blocks, that can terminate computation early if the retrieval is straightforward or noisy, saving a lot of computation. To assess the complexity of the input, we introduce a temporal-based classifier driven by a new training strategy. Furthermore, we adopt a binary hash code generation approach instead of relying on continuous-valued features, which significantly improves the search process by a factor of 20. To ensure similarity preservation, we utilize a new ranking regularizer that bridges the gap between continuous and binary features. Extensive analysis of our proposed method is conducted on three datasets: Market1501, MSMT17 (Multi-Scene Multi-Time), and the BGC1 (BRIAR Government Collection). Using our approach, more than 70&#37; of the samples with compact hash codes exit early on the Market1501 dataset, saving 80&#37; of the networks computational cost and improving over other hash-based methods by 60&#37;. These results demonstrate a significant improvement over dynamic networks and showcase comparable accuracy performance to conventional ReID methods. Code will be made available.
