---
layout: publication
title: Large Language Models Are Better Reasoners With Self-verification
authors: Yixuan Weng, Minjun Zhu, Fei Xia, Bin Li, Shizhu He, Shengping Liu, Bin Sun, Kang Liu, Jun Zhao
conference: "Arxiv"
year: 2022
bibkey: weng2022large
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2212.09561v5"}
  - {name: "Code", url: "https://github.com/WENGSYX/Self-Verification"}
tags: ['ARXIV', 'Has Code']
---
Recently with the chain of thought (CoT) prompting large language models (LLMs) e.g. GPT-3 have shown strong reasoning ability in several natural language processing tasks such as arithmetic commonsense and logical reasoning. However LLMs with CoT require multi-step prompting and multi-token prediction which is highly sensitive to individual mistakes and vulnerable to error accumulation. The above issues make the LLMs need the ability to verify the answers. In fact after inferring conclusions in some thinking decision tasks people often check them by re-verifying steps to avoid some mistakes. In this paper we propose and prove that LLMs also have similar self-verification abilities. We take the conclusion obtained by CoT as one of the conditions for solving the original problem. By performing a backward verification of the answers that LLM deduced for itself we can obtain interpretable answer validation scores to select the candidate answer with the highest score. Experimental results demonstrate that the proposed method can improve the reasoning performance on various arithmetic commonsense and logical reasoning datasets. Our code is publicly available at https://github.com/WENGSYX/Self-Verification.
