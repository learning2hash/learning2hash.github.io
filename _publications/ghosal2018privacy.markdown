---
layout: publication
title: Privacy Preserving Multi-server K-means Computation Over Horizontally Partitioned
  Data
authors: Riddhi Ghosal, Sanjit Chatterjee
conference: Lecture Notes in Computer Science
year: 2018
bibkey: ghosal2018privacy
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1808.03811'}]
tags: []
short_authors: Riddhi Ghosal, Sanjit Chatterjee
---
The k-means clustering is one of the most popular clustering algorithms in
data mining. Recently a lot of research has been concentrated on the algorithm
when the dataset is divided into multiple parties or when the dataset is too
large to be handled by the data owner. In the latter case, usually some servers
are hired to perform the task of clustering. The dataset is divided by the data
owner among the servers who together perform the k-means and return the cluster
labels to the owner. The major challenge in this method is to prevent the
servers from gaining substantial information about the actual data of the
owner. Several algorithms have been designed in the past that provide
cryptographic solutions to perform privacy preserving k-means. We provide a new
method to perform k-means over a large set using multiple servers. Our
technique avoids heavy cryptographic computations and instead we use a simple
randomization technique to preserve the privacy of the data. The k-means
computed has exactly the same efficiency and accuracy as the k-means computed
over the original dataset without any randomization. We argue that our
algorithm is secure against honest but curious and passive adversary.