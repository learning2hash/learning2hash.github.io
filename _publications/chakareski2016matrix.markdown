---
layout: publication
title: Matrix Factorization-based Clustering Of Image Features For Bandwidth-constrained
  Information Retrieval
authors: Jacob Chakareski, Immanuel Manohar, Shantanu Rane
conference: Arxiv
year: 2016
bibkey: chakareski2016matrix
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1605.02140'}]
tags: ["Efficiency", "Image Retrieval"]
short_authors: Jacob Chakareski, Immanuel Manohar, Shantanu Rane
---
We consider the problem of accurately and efficiently querying a remote
server to retrieve information about images captured by a mobile device. In
addition to reduced transmission overhead and computational complexity, the
retrieval protocol should be robust to variations in the image acquisition
process, such as translation, rotation, scaling, and sensor-related
differences. We propose to extract scale-invariant image features and then
perform clustering to reduce the number of features needed for image matching.
Principal Component Analysis (PCA) and Non-negative Matrix Factorization (NMF)
are investigated as candidate clustering approaches. The image matching
complexity at the database server is quadratic in the (small) number of
clusters, not in the (very large) number of image features. We employ an
image-dependent information content metric to approximate the model order,
i.e., the number of clusters, needed for accurate matching, which is preferable
to setting the model order using trial and error. We show how to combine the
hypotheses provided by PCA and NMF factor loadings, thereby obtaining more
accurate retrieval than using either approach alone. In experiments on a
database of urban images, we obtain a top-1 retrieval accuracy of 89% and a
top-3 accuracy of 92.5%.