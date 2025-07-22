---
layout: publication
title: Learning To Index For Nearest Neighbor Search
authors: Chiu Chih-yi, Prayoonwong Amorntip, Liao Yin-chih
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2019
bibkey: chiu2018learning
citations: 24
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1807.02962'}]
tags: ["Quantization", "Scalability", "Large-Scale-Search", "Datasets", "Evaluation"]
short_authors: Chiu Chih-yi, Prayoonwong Amorntip, Liao Yin-chih
---
In this study, we present a novel ranking model based on learning
neighborhood relationships embedded in the index space. Given a query point,
conventional approximate nearest neighbor search calculates the distances to
the cluster centroids, before ranking the clusters from near to far based on
the distances. The data indexed in the top-ranked clusters are retrieved and
treated as the nearest neighbor candidates for the query. However, the loss of
quantization between the data and cluster centroids will inevitably harm the
search accuracy. To address this problem, the proposed model ranks clusters
based on their nearest neighbor probabilities rather than the query-centroid
distances. The nearest neighbor probabilities are estimated by employing neural
networks to characterize the neighborhood relationships, i.e., the density
function of nearest neighbors with respect to the query. The proposed
probability-based ranking can replace the conventional distance-based ranking
for finding candidate clusters, and the predicted probability can be used to
determine the data quantity to be retrieved from the candidate cluster. Our
experimental results demonstrated that the proposed ranking model could boost
the search performance effectively in billion-scale datasets.