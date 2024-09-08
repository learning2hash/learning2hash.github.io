---
    layout: publication
    title: "FedHAP: Federated Hashing with Global Prototypes for Cross-silo Retrieval"
    authors: Yang Meilin, Xu Jian, Liu Yang, Ding Wenbo
    conference: Arxiv
    year: 2022
    bibkey: yang2022fedhap
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/2207.05525"}
    tags: ['Arxiv', 'ICIP']
    ---
    Deep hashing has been widely applied in large-scale data retrieval due to its superior retrieval efficiency and low storage cost. However, data are often scattered in data silos with privacy concerns, so performing centralized data storage and retrieval is not always possible. Leveraging the concept of federated learning (FL) to perform deep hashing is a recent research trend. However, existing frameworks mostly rely on the aggregation of the local deep hashing models, which are trained by performing similarity learning with local skewed data only. Therefore, they cannot work well for non-IID clients in a real federated environment. To overcome these challenges, we propose a novel federated hashing framework that enables participating clients to jointly train the shared deep hashing model by leveraging the prototypical hash codes for each class. Globally, the transmission of global prototypes with only one prototypical hash code per class will minimize the impact of communication cost and privacy risk. Locally, the use of global prototypes are maximized by jointly training a discriminator network and the local hashing network. Extensive experiments on benchmark datasets are conducted to demonstrate that our method can significantly improve the performance of the deep hashing model in the federated environments with non-IID data distributions.