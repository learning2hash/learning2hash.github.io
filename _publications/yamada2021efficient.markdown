---
layout: publication
title: Efficient Passage Retrieval With Hashing For Open-domain Question Answering
authors: Yamada Ikuya, Asai Akari, Hajishirzi Hannaneh
conference: "Arxiv"
year: 2021
bibkey: yamada2021efficient
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2106.00882"}
  - {name: "Code", url: "https://github.com/studio-ousia/bpr"}
tags: ['ARXIV', 'Has Code']
---
Most state-of-the-art open-domain question answering systems use a neural retrieval model to encode passages into continuous vectors and extract them from a knowledge source. However such retrieval models often require large memory to run because of the massive size of their passage index. In this paper we introduce Binary Passage Retriever (BPR) a memory-efficient neural retrieval model that integrates a learning-to-hash technique into the state-of-the-art Dense Passage Retriever (DPR) to represent the passage index using compact binary codes rather than continuous vectors. BPR is trained with a multi-task objective over two tasks efficient candidate generation based on binary codes and accurate reranking based on continuous vectors. Compared with DPR BPR substantially reduces the memory cost from 65GB to 2GB without a loss of accuracy on two standard open-domain question answering benchmarks Natural Questions and TriviaQA. Our code and trained models are available at https://github.com/studio-ousia/bpr.
