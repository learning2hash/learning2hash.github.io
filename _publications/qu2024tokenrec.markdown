---
layout: publication
title: 'Tokenrec: Learning To Tokenize ID For Llm-based Generative Recommendation'
authors: Haohao Qu, Wenqi Fan, Zihuai Zhao, Qing Li
conference: Arxiv
year: 2024
bibkey: qu2024tokenrec
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.10450'}]
tags: ["Recommender Systems", "Scalability", "Similarity Search", "Tools & Libraries"]
short_authors: Qu et al.
---
There is a growing interest in utilizing large-scale language models (LLMs)
to advance next-generation Recommender Systems (RecSys), driven by their
outstanding language understanding and in-context learning capabilities. In
this scenario, tokenizing (i.e., indexing) users and items becomes essential
for ensuring a seamless alignment of LLMs with recommendations. While several
studies have made progress in representing users and items through textual
contents or latent representations, challenges remain in efficiently capturing
high-order collaborative knowledge into discrete tokens that are compatible
with LLMs. Additionally, the majority of existing tokenization approaches often
face difficulties in generalizing effectively to new/unseen users or items that
were not in the training corpus. To address these challenges, we propose a
novel framework called TokenRec, which introduces not only an effective ID
tokenization strategy but also an efficient retrieval paradigm for LLM-based
recommendations. Specifically, our tokenization strategy, Masked
Vector-Quantized (MQ) Tokenizer, involves quantizing the masked user/item
representations learned from collaborative filtering into discrete tokens, thus
achieving a smooth incorporation of high-order collaborative knowledge and a
generalizable tokenization of users and items for LLM-based RecSys. Meanwhile,
our generative retrieval paradigm is designed to efficiently recommend top-\\(K\\)
items for users to eliminate the need for the time-consuming auto-regressive
decoding and beam search processes used by LLMs, thus significantly reducing
inference time. Comprehensive experiments validate the effectiveness of the
proposed methods, demonstrating that TokenRec outperforms competitive
benchmarks, including both traditional recommender systems and emerging
LLM-based recommender systems.