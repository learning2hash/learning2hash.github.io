---
layout: publication
title: Finetuned Language Models Are Zero-shot Learners
authors: Jason Wei, Maarten Bosma, Vincent Y. Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan Du, Andrew M. Dai, Quoc V. Le
conference: "Arxiv"
year: 2021
bibkey: wei2021finetuned
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2109.01652v5"}
tags: ['ARXIV']
---
This paper explores a simple method for improving the zero-shot learning abilities of language models. We show that instruction tuning -- finetuning language models on a collection of tasks described via instructions -- substantially improves zero-shot performance on unseen tasks. We take a 137B parameter pretrained language model and instruction-tune it on over 60 NLP tasks verbalized via natural language instruction templates. We evaluate this instruction-tuned model which we call FLAN on unseen task types. FLAN substantially improves the performance of its unmodified counterpart and surpasses zero-shot 175B GPT-3 on 20 of 25 tasks that we evaluate. FLAN even outperforms few-shot GPT-3 by a large margin on ANLI RTE BoolQ AI2-ARC OpenbookQA and StoryCloze. Ablation studies reveal that number of finetuning datasets model scale and natural language instructions are key to the success of instruction tuning.
