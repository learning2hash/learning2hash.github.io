---
layout: publication
title: Hallucidoctor Mitigating Hallucinatory Toxicity In Visual Instruction Data
authors: Qifan Yu, Juncheng Li, Longhui Wei, Liang Pang, Wentao Ye, Bosheng Qin, Siliang Tang, Qi Tian, Yueting Zhuang
conference: "Arxiv"
year: 2023
bibkey: yu2023hallucidoctor
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2311.13614v2"}
  - {name: "Code", url: "https://github.com/Yuqifan1117/HalluciDoctor}"}
tags: ['ARXIV', 'Has Code', 'Supervised']
---
Multi-modal Large Language Models (MLLMs) tuned on machine-generated instruction-following data have demonstrated remarkable performance in various multi-modal understanding and generation tasks. However the hallucinations inherent in machine-generated data which could lead to hallucinatory outputs in MLLMs remain under-explored. This work aims to investigate various hallucinations (i.e. object relation attribute hallucinations) and mitigate those hallucinatory toxicities in large-scale machine-generated visual instruction datasets. Drawing on the human ability to identify factual errors we present a novel hallucination detection and elimination framework HalluciDoctor based on the cross-checking paradigm. We use our framework to identify and eliminate hallucinations in the training data automatically. Interestingly HalluciDoctor also indicates that spurious correlations arising from long-tail object co-occurrences contribute to hallucinations. Based on that we execute counterfactual visual instruction expansion to balance data distribution thereby enhancing MLLMs resistance to hallucinations. Comprehensive experiments on hallucination evaluation benchmarks show that our method successfully mitigates 44.637; hallucinations relatively and maintains competitive performance compared to LLaVA. The data and code for this paper are publicly available. urlhttps://github.com/Yuqifan1117/HalluciDoctor\}.
