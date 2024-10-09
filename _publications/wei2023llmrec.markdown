---
layout: publication
title: Llmrec Large Language Models With Graph Augmentation For Recommendation
authors: Wei Wei, Xubin Ren, Jiabin Tang, Qinyong Wang, Lixin Su, Suqi Cheng, Junfeng Wang, Dawei Yin, Chao Huang
conference: "Arxiv"
year: 2023
bibkey: wei2023llmrec
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2311.00423v6"}
  - {name: "Code", url: "https://github.com/HKUDS/LLMRec.git"}
tags: ['ARXIV', 'Graph', 'Has Code']
---
The problem of data sparsity has long been a challenge in recommendation systems and previous studies have attempted to address this issue by incorporating side information. However this approach often introduces side effects such as noise availability issues and low data quality which in turn hinder the accurate modeling of user preferences and adversely impact recommendation performance. In light of the recent advancements in large language models (LLMs) which possess extensive knowledge bases and strong reasoning capabilities we propose a novel framework called LLMRec that enhances recommender systems by employing three simple yet effective LLM-based graph augmentation strategies. Our approach leverages the rich content available within online platforms (e.g. Netflix MovieLens) to augment the interaction graph in three ways (i) reinforcing user-item interaction egde (ii) enhancing the understanding of item node attributes and (iii) conducting user node profiling intuitively from the natural language perspective. By employing these strategies we address the challenges posed by sparse implicit feedback and low-quality side information in recommenders. Besides to ensure the quality of the augmentation we develop a denoised data robustification mechanism that includes techniques of noisy implicit feedback pruning and MAE-based feature enhancement that help refine the augmented data and improve its reliability. Furthermore we provide theoretical analysis to support the effectiveness of LLMRec and clarify the benefits of our method in facilitating model optimization. Experimental results on benchmark datasets demonstrate the superiority of our LLM-based augmentation approach over state-of-the-art techniques. To ensure reproducibility we have made our code and augmented data publicly available at https://github.com/HKUDS/LLMRec.git
