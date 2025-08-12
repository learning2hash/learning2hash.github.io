---
layout: publication
title: Boosting Entity-aware Image Captioning With Multi-modal Knowledge Graph
authors: Wentian Zhao, Yao Hu, Heda Wang, Xinxiao Wu, Jiebo Luo
conference: IEEE Transactions on Multimedia
year: 2023
bibkey: zhao2021boosting
citations: 35
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2107.11970'}]
tags: ["Datasets"]
short_authors: Zhao et al.
---
Entity-aware image captioning aims to describe named entities and events
related to the image by utilizing the background knowledge in the associated
article. This task remains challenging as it is difficult to learn the
association between named entities and visual cues due to the long-tail
distribution of named entities. Furthermore, the complexity of the article
brings difficulty in extracting fine-grained relationships between entities to
generate informative event descriptions about the image. To tackle these
challenges, we propose a novel approach that constructs a multi-modal knowledge
graph to associate the visual objects with named entities and capture the
relationship between entities simultaneously with the help of external
knowledge collected from the web. Specifically, we build a text sub-graph by
extracting named entities and their relationships from the article, and build
an image sub-graph by detecting the objects in the image. To connect these two
sub-graphs, we propose a cross-modal entity matching module trained using a
knowledge base that contains Wikipedia entries and the corresponding images.
Finally, the multi-modal knowledge graph is integrated into the captioning
model via a graph attention mechanism. Extensive experiments on both GoodNews
and NYTimes800k datasets demonstrate the effectiveness of our method.