---
layout: publication
title: Multi-modal Retrieval Using Graph Neural Networks
authors: Aashish Kumar Misraa, Ajinkya Kale, Pranav Aggarwal, Ali Aminian
conference: Arxiv
year: 2020
bibkey: misraa2020multi
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.01666'}]
tags: ["Datasets", "Hybrid ANN Methods", "Image Retrieval", "Multimodal Retrieval", "Re-Ranking"]
short_authors: Misraa et al.
---
Most real world applications of image retrieval such as Adobe Stock, which is
a marketplace for stock photography and illustrations, need a way for users to
find images which are both visually (i.e. aesthetically) and conceptually (i.e.
containing the same salient objects) as a query image. Learning visual-semantic
representations from images is a well studied problem for image retrieval.
Filtering based on image concepts or attributes is traditionally achieved with
index-based filtering (e.g. on textual tags) or by re-ranking after an initial
visual embedding based retrieval. In this paper, we learn a joint vision and
concept embedding in the same high-dimensional space. This joint model gives
the user fine-grained control over the semantics of the result set, allowing
them to explore the catalog of images more rapidly. We model the visual and
concept relationships as a graph structure, which captures the rich information
through node neighborhood. This graph structure helps us learn multi-modal node
embeddings using Graph Neural Networks. We also introduce a novel inference
time control, based on selective neighborhood connectivity allowing the user
control over the retrieval algorithm. We evaluate these multi-modal embeddings
quantitatively on the downstream relevance task of image retrieval on MS-COCO
dataset and qualitatively on MS-COCO and an Adobe Stock dataset.