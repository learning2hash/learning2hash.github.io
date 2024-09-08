---
    layout: publication
    title: "Online Hashing with Similarity Learning"
    authors: Weng Zhenyu, Zhu Yuesheng
    conference: Arxiv
    year: 2021
    bibkey: weng2021online
    additional_links:
       - {name: "License", url: "http://creativecommons.org/licenses/by/4.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/2108.02560"}
    tags: ['Streaming Data', 'Arxiv', 'Image Retrieval']
    ---
    {% raw %}
    Online hashing methods usually learn the hash functions online, aiming to efficiently adapt to the data variations in the streaming environment. However, when the hash functions are updated, the binary codes for the whole database have to be updated to be consistent with the hash functions, resulting in the inefficiency in the online image retrieval process. In this paper, we propose a novel online hashing framework without updating binary codes. In the proposed framework, the hash functions are fixed and a parametric similarity function for the binary codes is learnt online to adapt to the streaming data. Specifically, a parametric similarity function that has a bilinear form is adopted and a metric learning algorithm is proposed to learn the similarity function online based on the characteristics of the hashing methods. The experiments on two multi-label image datasets show that our method is competitive or outperforms the state-of-the-art online hashing methods in terms of both accuracy and efficiency for multi-label image retrieval.
    {% endraw %}