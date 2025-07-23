---
layout: publication
title: Bridging Language And Items For Retrieval And Recommendation
authors: Hou Yupeng, Li Jiacheng, He Zhankui, Yan An, Chen Xiusi, Mcauley Julian
conference: Arxiv
year: 2024
bibkey: hou2024bridging
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.03952'}]
tags: ["Datasets", "Evaluation", "Multimodal Retrieval", "Recommender Systems"]
short_authors: Hou et al.
---
This paper introduces BLaIR, a series of pretrained sentence embedding models
specialized for recommendation scenarios. BLaIR is trained to learn
correlations between item metadata and potential natural language context,
which is useful for retrieving and recommending items. To pretrain BLaIR, we
collect Amazon Reviews 2023, a new dataset comprising over 570 million reviews
and 48 million items from 33 categories, significantly expanding beyond the
scope of previous versions. We evaluate the generalization ability of BLaIR
across multiple domains and tasks, including a new task named complex product
search, referring to retrieving relevant items given long, complex natural
language contexts. Leveraging large language models like ChatGPT, we
correspondingly construct a semi-synthetic evaluation set, Amazon-C4. Empirical
results on the new task, as well as conventional retrieval and recommendation
tasks, demonstrate that BLaIR exhibit strong text and item representation
capacity. Our datasets, code, and checkpoints are available at:
https://github.com/hyp1231/AmazonReviews2023.