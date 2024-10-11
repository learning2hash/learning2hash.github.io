---
layout: publication
title: VISIR Visual And Semantic Image Label Refinement
authors: Chowdhury Sreyasi Nag, Tandon Niket, Ferhatosmanoglu Hakan, Weikum Gerhard
conference: "ACM ISBN"
year: 2019
bibkey: chowdhury2019visir
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1909.00741"}
tags: ['Deep Learning', 'Image Retrieval']
---
The social media explosion has populated the Internet with a wealth of images. There are two existing paradigms for image retrieval: 1) content-based image retrieval (CBIR), which has traditionally used visual features for similarity search (e.g., SIFT features), and 2) tag-based image retrieval (TBIR), which has relied on user tagging (e.g., Flickr tags). CBIR now gains semantic expressiveness by advances in deep-learning-based detection of visual labels. TBIR benefits from query-and-click logs to automatically infer more informative labels. However, learning-based tagging still yields noisy labels and is restricted to concrete objects, missing out on generalizations and abstractions. Click-based tagging is limited to terms that appear in the textual context of an image or in queries that lead to a click. This paper addresses the above limitations by semantically refining and expanding the labels suggested by learning-based object detection. We consider the semantic coherence between the labels for different objects, leverage lexical and commonsense knowledge, and cast the label assignment into a constrained optimization problem solved by an integer linear program. Experiments show that our method, called VISIR, improves the quality of the state-of-the-art visual labeling tools like LSDA and YOLO.
