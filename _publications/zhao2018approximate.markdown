---
    layout: publication
    title: "Approximate k-NN Graph Construction: a Generic Online Approach"
    authors: Zhao Wan-Lei, Wang Hui, Ngo Chong-Wah
    conference: Arxiv
    year: 2018
    bibkey: zhao2018approximate
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1804.03032"}
    tags: ['Arxiv', 'Graph']
    ---
    {% raw %}
    Nearest neighbor search and k-nearest neighbor graph construction are two fundamental issues arise from many disciplines such as multimedia information retrieval, data-mining and machine learning. They become more and more imminent given the big data emerge in various fields in recent years. In this paper, a simple but effective solution both for approximate k-nearest neighbor search and approximate k-nearest neighbor graph construction is presented. These two issues are addressed jointly in our solution. On the one hand, the approximate k-nearest neighbor graph construction is treated as a search task. Each sample along with its k-nearest neighbors are joined into the k-nearest neighbor graph by performing the nearest neighbor search sequentially on the graph under construction. On the other hand, the built k-nearest neighbor graph is used to support k-nearest neighbor search. Since the graph is built online, the dynamic update on the graph, which is not possible from most of the existing solutions, is supported. This solution is feasible for various distance measures. Its effectiveness both as k-nearest neighbor construction and k-nearest neighbor search approaches is verified across different types of data in different scales, various dimensions and under different metrics.
    {% endraw %}