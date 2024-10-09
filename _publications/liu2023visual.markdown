---
layout: publication
title: Visual Instruction Tuning
authors: Haotian Liu, Chunyuan Li, Qingyang Wu, Yong Jae Lee
conference: "Arxiv"
year: 2023
bibkey: liu2023visual
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2304.08485v2"}
tags: ['ARXIV', 'Cross Modal']
---
Instruction tuning large language models (LLMs) using machine-generated instruction-following data has improved zero-shot capabilities on new tasks but the idea is less explored in the multimodal field. In this paper we present the first attempt to use language-only GPT-4 to generate multimodal language-image instruction-following data. By instruction tuning on such generated data we introduce LLaVA Large Language and Vision Assistant an end-to-end trained large multimodal model that connects a vision encoder and LLM for general-purpose visual and language understanding.Our early experiments show that LLaVA demonstrates impressive multimodel chat abilities sometimes exhibiting the behaviors of multimodal GPT-4 on unseen images/instructions and yields a 85.137; relative score compared with GPT-4 on a synthetic multimodal instruction-following dataset. When fine-tuned on Science QA the synergy of LLaVA and GPT-4 achieves a new state-of-the-art accuracy of 92.5337;. We make GPT-4 generated visual instruction tuning data our model and code base publicly available.
