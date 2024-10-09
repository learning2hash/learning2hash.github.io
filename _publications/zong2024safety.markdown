---
layout: publication
title: Safety Fine-tuning At (almost) No Cost A Baseline For Vision Large Language Models
authors: Yongshuo Zong, Ondrej Bohdal, Tingyang Yu, Yongxin Yang, Timothy Hospedales
conference: "Arxiv"
year: 2024
bibkey: zong2024safety
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2402.02207v2"}
  - {name: "Code", url: "https://github.com/ys-zong/VLGuard"}
tags: ['ARXIV', 'Cross Modal', 'Has Code']
---
Current vision large language models (VLLMs) exhibit remarkable capabilities yet are prone to generate harmful content and are vulnerable to even the simplest jailbreaking attacks. Our initial analysis finds that this is due to the presence of harmful data during vision-language instruction fine-tuning and that VLLM fine-tuning can cause forgetting of safety alignment previously learned by the underpinning LLM. To address this issue we first curate a vision-language safe instruction-following dataset VLGuard covering various harmful categories. Our experiments demonstrate that integrating this dataset into standard vision-language fine-tuning or utilizing it for post-hoc fine-tuning effectively safety aligns VLLMs. This alignment is achieved with minimal impact on or even enhancement of the models helpfulness. The versatility of our safety fine-tuning dataset makes it a valuable resource for safety-testing existing VLLMs training new models or safeguarding pre-trained VLLMs. Empirical results demonstrate that fine-tuned VLLMs effectively reject unsafe instructions and substantially reduce the success rates of several black-box adversarial attacks which approach zero in many cases. The code and dataset are available at https://github.com/ys-zong/VLGuard.
