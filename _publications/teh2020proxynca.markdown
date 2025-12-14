---
layout: publication
title: 'Proxynca++: Revisiting And Revitalizing Proxy Neighborhood Component Analysis'
authors: Eu Wern Teh, Terrance Devries, Graham W. Taylor
conference: Lecture Notes in Computer Science
year: 2020
bibkey: teh2020proxynca
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.01113'}]
tags: [Evaluation, Distance Metric Learning, Few-shot & Zero-shot, Datasets]
short_authors: Eu Wern Teh, Terrance Devries, Graham W. Taylor
---
We consider the problem of distance metric learning (DML), where the task is
to learn an effective similarity measure between images. We revisit ProxyNCA
and incorporate several enhancements. We find that low temperature scaling is a
performance-critical component and explain why it works. Besides, we also
discover that Global Max Pooling works better in general when compared to
Global Average Pooling. Additionally, our proposed fast moving proxies also
addresses small gradient issue of proxies, and this component synergizes well
with low temperature scaling and Global Max Pooling. Our enhanced model, called
ProxyNCA++, achieves a 22.9 percentage point average improvement of Recall@1
across four different zero-shot retrieval datasets compared to the original
ProxyNCA algorithm. Furthermore, we achieve state-of-the-art results on the
CUB200, Cars196, Sop, and InShop datasets, achieving Recall@1 scores of 72.2,
90.1, 81.4, and 90.9, respectively.