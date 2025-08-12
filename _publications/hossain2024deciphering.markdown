---
layout: publication
title: 'Deciphering Hate: Identifying Hateful Memes And Their Targets'
authors: Eftekhar Hossain, Omar Sharif, Mohammed Moshiul Hoque, Sarah M. Preum
conference: 'Proceedings of the 62nd Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)'
year: 2024
bibkey: hossain2024deciphering
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.10829'}]
tags: []
short_authors: Hossain et al.
---
Internet memes have become a powerful means for individuals to express
emotions, thoughts, and perspectives on social media. While often considered as
a source of humor and entertainment, memes can also disseminate hateful content
targeting individuals or communities. Most existing research focuses on the
negative aspects of memes in high-resource languages, overlooking the
distinctive challenges associated with low-resource languages like Bengali
(also known as Bangla). Furthermore, while previous work on Bengali memes has
focused on detecting hateful memes, there has been no work on detecting their
targeted entities. To bridge this gap and facilitate research in this arena, we
introduce a novel multimodal dataset for Bengali, BHM (Bengali Hateful Memes).
The dataset consists of 7,148 memes with Bengali as well as code-mixed
captions, tailored for two tasks: (i) detecting hateful memes, and (ii)
detecting the social entities they target (i.e., Individual, Organization,
Community, and Society). To solve these tasks, we propose DORA (Dual cO
attention fRAmework), a multimodal deep neural network that systematically
extracts the significant modality features from the memes and jointly evaluates
them with the modality-specific features to understand the context better. Our
experiments show that DORA is generalizable on other low-resource hateful meme
datasets and outperforms several state-of-the-art rivaling baselines.