---
layout: publication
title: 'Graph-based Approximate NN Search: A Revisit'
authors: Hui Wang, Yong Wang, Wan-Lei Zhao
conference: Arxiv
year: 2022
bibkey: wang2022graph
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.00824'}]
tags: ["Datasets", "Efficiency", "Evaluation", "Graph Based ANN", "Scalability"]
short_authors: Hui Wang, Yong Wang, Wan-Lei Zhao
---
Nearest neighbor search plays a fundamental role in many disciplines such as
multimedia information retrieval, data-mining, and machine learning. The
graph-based search approaches show superior performance over other types of
approaches in recent studies. In this paper, the graph-based NN search is
revisited. We optimize two key components in the approach, namely the search
procedure and the graph that supports the search. For the graph construction, a
two-stage graph diversification scheme is proposed, which makes a good
trade-off between the efficiency and reachability for the search procedure that
builds upon it. Moreover, the proposed diversification scheme allows the search
procedure to decide dynamically how many nodes should be visited in one node's
neighborhood. By this way, the computing power of the devices is fully utilized
when the search is carried out under different circumstances. Furthermore, two
NN search procedures are designed respectively for small and large batch
queries on the GPU. The optimized NN search, when being supported by the
two-stage diversified graph, outperforms all the state-of-the-art approaches on
both the CPU and the GPU across all the considered large-scale datasets.