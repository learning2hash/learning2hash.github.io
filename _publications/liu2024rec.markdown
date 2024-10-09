---
layout: publication
title: Rec-gpt4v Multimodal Recommendation With Large Vision-language Models
authors: Yuqing Liu, Yu Wang, Lichao Sun, Philip S. Yu
conference: "Arxiv"
year: 2024
bibkey: liu2024rec
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2402.08670v1"}
tags: ['ARXIV', 'Cross Modal']
---
The development of large vision-language models (LVLMs) offers the potential to address challenges faced by traditional multimodal recommendations thanks to their proficient understanding of static images and textual dynamics. However the application of LVLMs in this field is still limited due to the following complexities First LVLMs lack user preference knowledge as they are trained from vast general datasets. Second LVLMs suffer setbacks in addressing multiple image dynamics in scenarios involving discrete noisy and redundant image sequences. To overcome these issues we propose the novel reasoning scheme named Rec-GPT4V Visual-Summary Thought (VST) of leveraging large vision-language models for multimodal recommendation. We utilize user history as in-context user preferences to address the first challenge. Next we prompt LVLMs to generate item image summaries and utilize image comprehension in natural language space combined with item titles to query the user preferences over candidate items. We conduct comprehensive experiments across four datasets with three LVLMs GPT4-V LLaVa-7b and LLaVa-13b. The numerical results indicate the efficacy of VST.
