---
layout: publication
title: Dimension Reduction for Efficient Dense Retrieval via Conditional Autoencoder
authors: Liu Zhenghao, Zhang Han, Xiong Chenyan, Liu Zhiyuan, Gu Yu, Li Xiaohua
conference: "Arxiv"
year: 2022
bibkey: liu2022dimension
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2205.03284"}
tags: ['ARXIV']
---
Dense retrievers encode queries and documents and map them in an embedding space using pre-trained language models. These embeddings need to be high-dimensional to fit training signals and guarantee the retrieval effectiveness of dense retrievers. However these high-dimensional embeddings lead to larger index storage and higher retrieval latency. To reduce the embedding dimensions of dense retrieval this paper proposes a Conditional Autoencoder (ConAE) to compress the high-dimensional embeddings to maintain the same embedding distribution and better recover the ranking features. Our experiments show that ConAE is effective in compressing embeddings by achieving comparable ranking performance with its teacher model and making the retrieval system more efficient. Our further analyses show that ConAE can alleviate the redundancy of the embeddings of dense retrieval with only one linear layer. All codes of this work are available at httpsgithub.com/NEUIR/ConAE.
