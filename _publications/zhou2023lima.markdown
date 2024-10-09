---
layout: publication
title: LIMA Less Is More For Alignment
authors: Chunting Zhou, Pengfei Liu, Puxin Xu, Srini Iyer, Jiao Sun, Yuning Mao, Xuezhe Ma, Avia Efrat, Ping Yu, Lili Yu, Susan Zhang, Gargi Ghosh, Mike Lewis, Luke Zettlemoyer, Omer Levy
conference: "Arxiv"
year: 2023
bibkey: zhou2023lima
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2305.11206v1"}
tags: ['ARXIV', 'Unsupervised']
---
Large language models are trained in two stages (1) unsupervised pretraining from raw text to learn general-purpose representations and (2) large scale instruction tuning and reinforcement learning to better align to end tasks and user preferences. We measure the relative importance of these two stages by training LIMA a 65B parameter LLaMa language model fine-tuned with the standard supervised loss on only 1000 carefully curated prompts and responses without any reinforcement learning or human preference modeling. LIMA demonstrates remarkably strong performance learning to follow specific response formats from only a handful of examples in the training data including complex queries that range from planning trip itineraries to speculating about alternate history. Moreover the model tends to generalize well to unseen tasks that did not appear in the training data. In a controlled human study responses from LIMA are either equivalent or strictly preferred to GPT-4 in 4337; of cases; this statistic is as high as 5837; when compared to Bard and 6537; versus DaVinci003 which was trained with human feedback. Taken together these results strongly suggest that almost all knowledge in large language models is learned during pretraining and only limited instruction tuning data is necessary to teach models to produce high quality output.
