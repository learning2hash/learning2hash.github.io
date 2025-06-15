---
layout: publication
title: 'Nested Hash Layer: A Plug-and-play Module For Multiple-length Hash Code Learning'
authors: Liyang He et al.
conference: "Arxiv"
year: 2024
citations: 0
bibkey: he2024nested
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2412.08922'}
tags: ['Cross-Modal', 'Deep', 'Model Design', 'Independent', 'Efficiency', 'Retrieval Models', 'Hashing', 'Training Strategy', 'Supervised Hashing', 'Applications']
---
Deep supervised hashing is essential for efficient storage and search in large-scale image retrieval. Traditional deep supervised hashing models generate single-length hash codes, but this creates a trade-off between efficiency and effectiveness for different code lengths. To find the optimal length for a task, multiple models must be trained, increasing time and computation. Furthermore, relationships between hash codes of different lengths are often ignored. To address these issues, we propose the Nested Hash Layer (NHL), a plug-and-play module for deep supervised hashing models. NHL generates hash codes of multiple lengths simultaneously in a nested structure. To resolve optimization conflicts from multiple learning objectives, we introduce a dominance-aware dynamic weighting strategy to adjust gradients. Additionally, we propose a long-short cascade self-distillation method, where long hash codes guide the learning of shorter ones, improving overall code quality. Experiments indicate that the NHL achieves an overall training speed improvement of approximately 5 to 8 times across various deep supervised hashing models and enhances the average performance of these models by about 3.4%.
