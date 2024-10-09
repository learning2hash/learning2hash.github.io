---
layout: publication
title: FAITHSCORE Evaluating Hallucinations In Large Vision-language Models
authors: Liqiang Jing, Ruosen Li, Yunmo Chen, Mengzhao Jia, Xinya Du
conference: "Arxiv"
year: 2023
bibkey: jing2023faithscore
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2311.01477v1"}
tags: ['ARXIV', 'Cross Modal']
---
We introduce FAITHSCORE (Faithfulness to Atomic Image Facts Score) a reference-free and fine-grained evaluation metric that measures the faithfulness of the generated free-form answers from large vision-language models (LVLMs). The FAITHSCORE evaluation first identifies sub-sentences containing descriptive statements that need to be verified then extracts a comprehensive list of atomic facts from these sub-sentences and finally conducts consistency verification between fine-grained atomic facts and the input image. Meta-evaluation demonstrates that our metric highly correlates with human judgments of faithfulness. We collect two benchmark datasets (i.e. LLaVA-1k and MSCOCO-Cap) for evaluating LVLMs instruction-following hallucinations. We measure hallucinations in state-of-the-art LVLMs with FAITHSCORE on the datasets. Results reveal that current systems are prone to generate hallucinated content unfaithful to the image which leaves room for future improvements. Further we find that current LVLMs despite doing well on color and counting still struggle with long answers relations and multiple objects.
