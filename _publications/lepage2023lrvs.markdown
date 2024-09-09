---
layout: publication
title: LRVS-Fashion Extending Visual Search with Referring Instructions
authors: Lepage Simon, Mary Jérémie, Picard David
conference: "Arxiv"
year: 2023
bibkey: lepage2023lrvs
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2306.02928"}
tags: ['ARXIV', 'Supervised', 'Weakly Supervised']
---
This paper introduces a new challenge for image similarity search in the context of fashion, addressing the inherent ambiguity in this domain stemming from complex images. We present Referred Visual Search (RVS), a task allowing users to define more precisely the desired similarity, following recent interest in the industry. We release a new large public dataset, LRVS-Fashion, consisting of 272k fashion products with 842k images extracted from fashion catalogs, designed explicitly for this task. However, unlike traditional visual search methods in the industry, we demonstrate that superior performance can be achieved by bypassing explicit object detection and adopting weakly-supervised conditional contrastive learning on image tuples. Our method is lightweight and demonstrates robustness, reaching Recall at one superior to strong detection-based baselines against 2M distractors. The dataset is available at https//huggingface.co/datasets/Slep/LAION-RVS-Fashion .
