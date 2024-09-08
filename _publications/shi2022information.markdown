---
    layout: publication
    title: "Information-Theoretic Hashing for Zero-Shot Cross-Modal Retrieval"
    authors: Shi Yufeng, Yu Shujian, Xu Duanquan, You Xinge
    conference: Arxiv
    year: 2022
    bibkey: shi2022information
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/2209.12491"}
    tags: ['Arxiv', 'Cross-Modal']
    ---
    Zero-shot cross-modal retrieval (ZS-CMR) deals with the retrieval problem among heterogenous data from unseen classes. Typically, to guarantee generalization, the pre-defined class embeddings from natural language processing (NLP) models are used to build a common space. In this paper, instead of using an extra NLP model to define a common space beforehand, we consider a totally different way to construct (or learn) a common hamming space from an information-theoretic perspective. We term our model the Information-Theoretic Hashing (ITH), which is composed of two cascading modules: an Adaptive Information Aggregation (AIA) module; and a Semantic Preserving Encoding (SPE) module. Specifically, our AIA module takes the inspiration from the Principle of Relevant Information (PRI) to construct a common space that adaptively aggregates the intrinsic semantics of different modalities of data and filters out redundant or irrelevant information. On the other hand, our SPE module further generates the hashing codes of different modalities by preserving the similarity of intrinsic semantics with the element-wise Kullback-Leibler (KL) divergence. A total correlation regularization term is also imposed to reduce the redundancy amongst different dimensions of hash codes. Sufficient experiments on three benchmark datasets demonstrate the superiority of the proposed ITH in ZS-CMR. Source code is available in the supplementary material.