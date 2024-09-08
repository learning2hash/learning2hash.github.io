---
    layout: publication
    title: "Fine-Grained Embedding Dimension Optimization During Training for Recommender Systems"
    authors: Luo Qinyi, Wang Penghan, Zhang Wei, Lai Fan, Mao Jiachen, Wei Xiaohan, Song Jun, Tsai Wei-Yu, Yang Shuai, Hu Yuxi, Qian Xuehai
    conference: Arxiv
    year: 2024
    bibkey: luo2024fine
    additional_links:
       - {name: "License", url: "http://creativecommons.org/licenses/by/4.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/2401.04408"}
    tags: ['Deep Learning', 'Arxiv']
    ---
    Huge embedding tables in modern Deep Learning Recommender Models (DLRM) require prohibitively large memory during training and inference. Aiming to reduce the memory footprint of training, this paper proposes FIne-grained In-Training Embedding Dimension optimization (FIITED). Given the observation that embedding vectors are not equally important, FIITED adjusts the dimension of each individual embedding vector continuously during training, assigning longer dimensions to more important embeddings while adapting to dynamic changes in data. A novel embedding storage system based on virtually-hashed physically-indexed hash tables is designed to efficiently implement the embedding dimension adjustment and effectively enable memory saving. Experiments on two industry models show that FIITED is able to reduce the size of embeddings by more than 65% while maintaining the trained model's quality, saving significantly more memory than a state-of-the-art in-training embedding pruning method. On public click-through rate prediction datasets, FIITED is able to prune up to 93.75%-99.75% embeddings without significant accuracy loss.