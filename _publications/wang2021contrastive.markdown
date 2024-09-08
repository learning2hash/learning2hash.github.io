---
    layout: publication
    title: "Contrastive Quantization with Code Memory for Unsupervised Image Retrieval"
    authors: Wang Jinpeng, Zeng Ziyun, Chen Bin, Dai Tao, Xia Shu-Tao
    conference: Arxiv
    year: 2021
    bibkey: wang2021contrastive
    additional_links:
       - {name: "License", url: "http://creativecommons.org/licenses/by/4.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/2109.05205"}
   - {name: "Code", url: "https://github.com/gimpong/AAAI22-MeCoQ."}
    tags: ['Arxiv', 'Image Retrieval', 'Supervised', 'AAAI', 'Quantisation', 'Unsupervised']
    ---
    The high efficiency in computation and storage makes hashing (including binary hashing and quantization) a common strategy in large-scale retrieval systems. To alleviate the reliance on expensive annotations, unsupervised deep hashing becomes an important research problem. This paper provides a novel solution to unsupervised deep quantization, namely Contrastive Quantization with Code Memory (MeCoQ). Different from existing reconstruction-based strategies, we learn unsupervised binary descriptors by contrastive learning, which can better capture discriminative visual semantics. Besides, we uncover that codeword diversity regularization is critical to prevent contrastive learning-based quantization from model degeneration. Moreover, we introduce a novel quantization code memory module that boosts contrastive learning with lower feature drift than conventional feature memories. Extensive experiments on benchmark datasets show that MeCoQ outperforms state-of-the-art methods. Code and configurations are publicly available at https://github.com/gimpong/AAAI22-MeCoQ.