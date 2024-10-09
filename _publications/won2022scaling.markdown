---
layout: publication
title: Scaling Instruction-finetuned Language Models
authors: Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Yunxuan Li, Xuezhi Wang, Mostafa Dehghani, Siddhartha Brahma, Albert Webson, Shixiang Shane Gu, Zhuyun Dai, Mirac Suzgun, Xinyun Chen, Aakanksha Chowdhery, Alex Castro-ros, Marie Pellat, Kevin Robinson, Dasha Valter, Sharan Narang, Gaurav Mishra, Adams Yu, Vincent Zhao, Yanping Huang, Andrew Dai, Hongkun Yu, Slav Petrov, Ed H. Chi, Jeff Dean, Jacob Devlin, Adam Roberts, Denny Zhou, Quoc V. Le, Jason Wei
conference: "Arxiv"
year: 2022
bibkey: won2022scaling
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2210.11416v5"}
tags: ['ARXIV']
---
Finetuning language models on a collection of datasets phrased as instructions has been shown to improve model performance and generalization to unseen tasks. In this paper we explore instruction finetuning with a particular focus on (1) scaling the number of tasks (2) scaling the model size and (3) finetuning on chain-of-thought data. We find that instruction finetuning with the above aspects dramatically improves performance on a variety of model classes (PaLM T5 U-PaLM) prompting setups (zero-shot few-shot CoT) and evaluation benchmarks (MMLU BBH TyDiQA MGSM open-ended generation). For instance Flan-PaLM 540B instruction-finetuned on 1.8K tasks outperforms PALM 540B by a large margin (+9.437; on average). Flan-PaLM 540B achieves state-of-the-art performance on several benchmarks such as 75.237; on five-shot MMLU. We also publicly release Flan-T5 checkpoints which achieve strong few-shot performance even compared to much larger models such as PaLM 62B. Overall instruction finetuning is a general method for improving the performance and usability of pretrained language models.
