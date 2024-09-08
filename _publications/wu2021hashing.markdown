---
    layout: publication
    title: "Hashing-Accelerated Graph Neural Networks for Link Prediction"
    authors: Wu Wei, Li Bin, Luo Chuan, Nejdl Wolfgang
    conference: The Web Conference
    year: 2021
    bibkey: wu2021hashing
    additional_links:
       - {name: "DOI", url: "10.1145/3442381.3449884"}
   - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/2105.14280"}
    tags: ['The Web Conference', 'Graph']
    ---
    {% raw %}
    Networks are ubiquitous in the real world. Link prediction, as one of the key problems for network-structured data, aims to predict whether there exists a link between two nodes. The traditional approaches are based on the explicit similarity computation between the compact node representation by embedding each node into a low-dimensional space. In order to efficiently handle the intensive similarity computation in link prediction, the hashing technique has been successfully used to produce the node representation in the Hamming space. However, the hashing-based link prediction algorithms face accuracy loss from the randomized hashing techniques or inefficiency from the learning to hash techniques in the embedding process. Currently, the Graph Neural Network (GNN) framework has been widely applied to the graph-related tasks in an end-to-end manner, but it commonly requires substantial computational resources and memory costs due to massive parameter learning, which makes the GNN-based algorithms impractical without the help of a powerful workhorse. In this paper, we propose a simple and effective model called #GNN, which balances the trade-off between accuracy and efficiency. #GNN is able to efficiently acquire node representation in the Hamming space for link prediction by exploiting the randomized hashing technique to implement message passing and capture high-order proximity in the GNN framework. Furthermore, we characterize the discriminative power of #GNN in probability. The extensive experimental results demonstrate that the proposed #GNN algorithm achieves accuracy comparable to the learning-based algorithms and outperforms the randomized algorithm, while running significantly faster than the learning-based algorithms. Also, the proposed algorithm shows excellent scalability on a large-scale network with the limited resources.
    {% endraw %}