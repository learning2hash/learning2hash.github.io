---
layout: publication
title: Multitask Prompted Training Enables Zero-shot Task Generalization
authors: Victor Sanh, Albert Webson, Colin Raffel, Stephen H. Bach, Lintang Sutawika, Zaid Alyafeai, Antoine Chaffin, Arnaud Stiegler, Teven Le Scao, Arun Raja, Manan Dey, M Saiful Bari, Canwen Xu, Urmish Thakker, Shanya Sharma Sharma, Eliza Szczechla, Taewoon Kim, Gunjan Chhablani, Nihal Nayak, Debajyoti Datta, Jonathan Chang, Mike Tian-jian Jiang, Han Wang, Matteo Manica, Sheng Shen, Zheng Xin Yong, Harshit Pandey, Rachel Bawden, Thomas Wang, Trishala Neeraj, Jos Rozen, Abheesht Sharma, Andrea Santilli, Thibault Fevry, Jason Alan Fries, Ryan Teehan, Tali Bers, Stella Biderman, Leo Gao, Thomas Wolf, Alexander M. Rush
conference: "Arxiv"
year: 2021
bibkey: sanh2021multitask
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2110.08207v3"}
  - {name: "Code", url: "https://github.com/bigscience-workshop/t-zero"}
  - {name: "Code", url: "https://github.com/bigscience-workshop/promptsource"}
tags: ['ARXIV', 'Has Code', 'Supervised']
---
Large language models have recently been shown to attain reasonable zero-shot generalization on a diverse set of tasks (Brown et al. 2020). It has been hypothesized that this is a consequence of implicit multitask learning in language models pretraining (Radford et al. 2019). Can zero-shot generalization instead be directly induced by explicit multitask learning To test this question at scale we develop a system for easily mapping any natural language tasks into a human-readable prompted form. We convert a large set of supervised datasets each with multiple prompts with diverse wording. These prompted datasets allow for benchmarking the ability of a model to perform completely held-out tasks. We fine-tune a pretrained encoder-decoder model (Raffel et al. 2020; Lester et al. 2021) on this multitask mixture covering a wide variety of tasks. The model attains strong zero-shot performance on several standard datasets often outperforming models up to 16x its size. Further our approach attains strong performance on a subset of tasks from the BIG-bench benchmark outperforming models up to 6x its size. All trained models are available at https://github.com/bigscience-workshop/t-zero and all prompts are available at https://github.com/bigscience-workshop/promptsource.
