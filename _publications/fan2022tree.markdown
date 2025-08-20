---
layout: publication
title: Tree-based Search Graph For Approximate Nearest Neighbor Search
authors: Xiaobin Fan, Xiaoping Wang, Kai Lu, Lei Xue, Jinjing Zhao
conference: Arxiv
year: 2022
bibkey: fan2022tree
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.03237'}]
tags: [Datasets, Efficiency, Tree-based ANN, Evaluation, Graph-based ANN]
short_authors: Fan et al.
---
Nearest neighbor search supports important applications in many domains, such
as database, machine learning, computer vision. Since the computational cost
for accurate search is too high, the community turned to the research of
approximate nearest neighbor search (ANNS). Among them, graph-based algorithm
is one of the most important branches. Research by Fu et al. shows that the
algorithms based on Monotonic Search Network (MSNET), such as NSG and NSSG,
have achieved the state-of-the-art search performance in efficiency. The MSNET
is dedicated to achieving monotonic search with minimal out-degree of nodes to
pursue high efficiency. However, the current MSNET designs did not optimize the
probability of the monotonic search, and the lower bound of the probability is
only 50%. If they fail in monotonic search stage, they have to suffer
tremendous backtracking cost to achieve the required accuracy. This will cause
performance problems in search efficiency. To address this problem, we propose
(r,p)-MSNET, which achieves guaranteed probability on monotonic search. Due to
the high building complexity of a strict (r,p)-MSNET, we propose TBSG, which is
an approximation with low complexity. Experiment conducted on four
million-scaled datasets show that TBSG outperforms existing state-of-the-art
graph-based algorithms in search efficiency. Our code has been released on
Github.