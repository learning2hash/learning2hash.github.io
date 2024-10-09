---
layout: publication
title: Llm-based Federated Recommendation
authors: Jujia Zhao, Wenjie Wang, Chen Xu, Zhaochun Ren, See-kiong Ng, Tat-seng Chua
conference: "Arxiv"
year: 2024
bibkey: zhao2024llm
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2402.09959v2"}
tags: ['ARXIV']
---
Large Language Models (LLMs) with their advanced contextual understanding abilities have demonstrated considerable potential in enhancing recommendation systems via fine-tuning methods. However fine-tuning requires users behavior data which poses considerable privacy risks due to the incorporation of sensitive user information. The unintended disclosure of such data could infringe upon data protection laws and give rise to ethical issues. To mitigate these privacy issues Federated Learning for Recommendation (Fed4Rec) has emerged as a promising approach. Nevertheless applying Fed4Rec to LLM-based recommendation presents two main challenges first an increase in the imbalance of performance across clients affecting the systems efficiency over time and second a high demand on clients computational and storage resources for local training and inference of LLMs. To address these challenges we introduce a Privacy-Preserving LLM-based Recommendation (PPLR) framework. The PPLR framework employs two primary strategies. First it implements a dynamic balance strategy which involves the design of dynamic parameter aggregation and adjustment of learning speed for different clients during the training phase to ensure relatively balanced performance across all clients. Second PPLR adopts a flexible storage strategy selectively retaining certain sensitive layers of the language model on the client side while offloading non-sensitive layers to the server. This approach aims to preserve user privacy while efficiently saving computational and storage resources. Experimental results demonstrate that PPLR not only achieves a balanced performance among clients but also enhances overall system performance in a manner that is both computationally and storage-efficient while effectively protecting user privacy.
