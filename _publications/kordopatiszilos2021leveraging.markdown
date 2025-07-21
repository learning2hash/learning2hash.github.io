---
layout: publication
title: Leveraging EfficientNet and Contrastive Learning for Accurate Global-scale
  Location Estimation
authors: Kordopatis-zilos et al.
conference: Proceedings of the 2021 International Conference on Multimedia Retrieval
year: 2021
bibkey: kordopatiszilos2021leveraging
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.07645'}]
tags: ["Self-Supervised", "Multimodal-Retrieval"]
---
In this paper, we address the problem of global-scale image geolocation,
proposing a mixed classification-retrieval scheme. Unlike other methods that
strictly tackle the problem as a classification or retrieval task, we combine
the two practices in a unified solution leveraging the advantages of each
approach with two different modules. The first leverages the EfficientNet
architecture to assign images to a specific geographic cell in a robust way.
The second introduces a new residual architecture that is trained with
contrastive learning to map input images to an embedding space that minimizes
the pairwise geodesic distance of same-location images. For the final location
estimation, the two modules are combined with a search-within-cell scheme,
where the locations of most similar images from the predicted geographic cell
are aggregated based on a spatial clustering scheme. Our approach demonstrates
very competitive performance on four public datasets, achieving new
state-of-the-art performance in fine granularity scales, i.e., 15.0% at 1km
range on Im2GPS3k.