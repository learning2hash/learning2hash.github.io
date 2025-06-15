---
layout: publication
title: 'Content-based Sub-image Retrieval With Relevance Feedback'
authors: Jie Luo, Mario A. Nascimento
conference: "Arxiv"
year: 2009
citations: 12
bibkey: luo2009content
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/0904.4041'}
tags: ['Tools and Libraries', 'Evaluation Metrics', 'Hashing for Real-World Applications', 'Applications']
---
The typical content-based image retrieval problem is to find images within a
database that are similar to a given query image. This paper presents a
solution to a different problem, namely that of content based sub-image
retrieval, i.e., finding images from a database that contains another image.
Note that this is different from finding a region in a (segmented) image that
is similar to another image region given as a query. We present a technique for
CBsIR that explores relevance feedback, i.e., the user's input on intermediary
results, in order to improve retrieval efficiency. Upon modeling images as a
set of overlapping and recursive tiles, we use a tile re-weighting scheme that
assigns penalties to each tile of the database images and updates the tile
penalties for all relevant images retrieved at each iteration using both the
relevant and irrelevant images identified by the user. Each tile is modeled by
means of its color content using a compact but very efficient method which can,
indirectly, capture some notion of texture as well, despite the fact that only
color information is maintained. Performance evaluation on a largely
heterogeneous dataset of over 10,000 images shows that the system can achieve a
stable average recall value of 70% within the top 20 retrieved (and presented)
images after only 5 iterations, with each such iteration taking about 2 seconds
on an off-the-shelf desktop computer.
