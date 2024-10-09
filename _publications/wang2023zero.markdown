---
layout: publication
title: Zero-shot Next-item Recommendation Using Large Pretrained Language Models
authors: Lei Wang, Ee-peng Lim
conference: "Arxiv"
year: 2023
bibkey: wang2023zero
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2304.03153v1"}
  - {name: "Code", url: "https://github.com/AGI-Edgerunners/LLM-Next-Item-Rec"}
tags: ['ARXIV', 'Has Code', 'Supervised']
---
Large language models (LLMs) have achieved impressive zero-shot performance in various natural language processing (NLP) tasks demonstrating their capabilities for inference without training examples. Despite their success no research has yet explored the potential of LLMs to perform next-item recommendations in the zero-shot setting. We have identified two major challenges that must be addressed to enable LLMs to act effectively as recommenders. First the recommendation space can be extremely large for LLMs and LLMs do not know about the target users past interacted items and preferences. To address this gap we propose a prompting strategy called Zero-Shot Next-Item Recommendation (NIR) prompting that directs LLMs to make next-item recommendations. Specifically the NIR-based strategy involves using an external module to generate candidate items based on user-filtering or item-filtering. Our strategy incorporates a 3-step prompting that guides GPT-3 to carry subtasks that capture the users preferences select representative previously watched movies and recommend a ranked list of 10 movies. We evaluate the proposed approach using GPT-3 on MovieLens 100K dataset and show that it achieves strong zero-shot performance even outperforming some strong sequential recommendation models trained on the entire training dataset. These promising results highlight the ample research opportunities to use LLMs as recommenders. The code can be found at https://github.com/AGI-Edgerunners/LLM-Next-Item-Rec.
