---
layout: publication
title: Glam Efficient Scaling Of Language Models With Mixture-of-experts
authors: Nan Du, Yanping Huang, Andrew M. Dai, Simon Tong, Dmitry Lepikhin, Yuanzhong Xu, Maxim Krikun, Yanqi Zhou, Adams Wei Yu, Orhan Firat, Barret Zoph, Liam Fedus, Maarten Bosma, Zongwei Zhou, Tao Wang, Yu Emma Wang, Kellie Webster, Marie Pellat, Kevin Robinson, Kathleen Meier-hellstern, Toju Duke, Lucas Dixon, Kun Zhang, Quoc V Le, Yonghui Wu, Zhifeng Chen, Claire Cui
conference: "Arxiv"
year: 2021
bibkey: du2021glam
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2112.06905v2"}
tags: ['ARXIV']
---
Scaling language models with more data compute and parameters has driven significant progress in natural language processing. For example thanks to scaling GPT-3 was able to achieve strong results on in-context learning tasks. However training these large dense models requires significant amounts of computing resources. In this paper we propose and develop a family of language models named GLaM (Generalist Language Model) which uses a sparsely activated mixture-of-experts architecture to scale the model capacity while also incurring substantially less training cost compared to dense variants. The largest GLaM has 1.2 trillion parameters which is approximately 7x larger than GPT-3. It consumes only 1/3 of the energy used to train GPT-3 and requires half of the computation flops for inference while still achieving better overall zero-shot and one-shot performance across 29 NLP tasks.
