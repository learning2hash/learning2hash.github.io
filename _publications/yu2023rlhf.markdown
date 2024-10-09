---
layout: publication
title: RLHF-V Towards Trustworthy Mllms Via Behavior Alignment From Fine-grained Correctional Human Feedback
authors: Tianyu Yu, Yuan Yao, Haoye Zhang, Taiwen He, Yifeng Han, Ganqu Cui, Jinyi Hu, Zhiyuan Liu, Hai-tao Zheng, Maosong Sun, Tat-seng Chua
conference: "Arxiv"
year: 2023
bibkey: yu2023rlhf
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2312.00849v2"}
  - {name: "Code", url: "https://github.com/RLHF-V/RLHF-V"}
tags: ['ARXIV', 'Cross Modal', 'Has Code']
---
Multimodal Large Language Models (MLLMs) have recently demonstrated impressive capabilities in multimodal understanding reasoning and interaction. However existing MLLMs prevalently suffer from serious hallucination problems generating text that is not factually grounded in associated images. The problem makes existing MLLMs untrustworthy and thus impractical in real-world (especially high-stakes) applications. To address the challenge we present RLHF-V which enhances MLLM trustworthiness via behavior alignment from fine-grained correctional human feedback. Specifically RLHF-V collects human preference in the form of segment-level corrections on hallucinations and performs dense direct preference optimization over the human feedback. Comprehensive experiments on five benchmarks in both automatic and human evaluation show that RLHF-V can enable substantially more trustworthy MLLM behaviors with promising data and computation efficiency. Remarkably using 1.4k annotated data samples RLHF-V significantly reduces the hallucination rate of the base MLLM by 34.837; outperforming the concurrent LLaVA-RLHF trained on 10k annotated data. The final model achieves state-of-the-art performance in trustworthiness among open-source MLLMs and shows better robustness than GPT-4V in preventing hallucinations aroused from over-generalization. We open-source our code model and data at https://github.com/RLHF-V/RLHF-V.
