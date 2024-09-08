---
    layout: publication
    title: "Deep Reinforcement Learning with Label Embedding Reward for Supervised Image Hashing"
    authors: Wang Zhenzhen, Hong Weixiang, Yuan Junsong
    conference: Arxiv
    year: 2020
    bibkey: wang2020deep
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/2008.03973"}
    tags: ['Supervised', 'Arxiv', 'CNN', 'Image Retrieval']
    ---
    {% raw %}
    Deep hashing has shown promising results in image retrieval and recognition. Despite its success, most existing deep hashing approaches are rather similar: either multi-layer perceptron or CNN is applied to extract image feature, followed by different binarization activation functions such as sigmoid, tanh or autoencoder to generate binary code. In this work, we introduce a novel decision-making approach for deep supervised hashing. We formulate the hashing problem as travelling across the vertices in the binary code space, and learn a deep Q-network with a novel label embedding reward defined by Bose-Chaudhuri-Hocquenghem (BCH) codes to explore the best path. Extensive experiments and analysis on the CIFAR-10 and NUS-WIDE dataset show that our approach outperforms state-of-the-art supervised hashing methods under various code lengths.
    {% endraw %}