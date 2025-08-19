---
layout: publication
title: 'Deepdiffusion: Unsupervised Learning Of Retrieval-adapted Representations
  Via Diffusion-based Ranking On Latent Feature Manifold'
authors: Takahiko Furuya, Ryutarou Ohbuchi
conference: IEEE Access
year: 2022
bibkey: furuya2021deepdiffusion
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.07082'}]
tags: [Distance Metric Learning, Evaluation, Unsupervised]
short_authors: Takahiko Furuya, Ryutarou Ohbuchi
---
Unsupervised learning of feature representations is a challenging yet
important problem for analyzing a large collection of multimedia data that do
not have semantic labels. Recently proposed neural network-based unsupervised
learning approaches have succeeded in obtaining features appropriate for
classification of multimedia data. However, unsupervised learning of feature
representations adapted to content-based matching, comparison, or retrieval of
multimedia data has not been explored well. To obtain such retrieval-adapted
features, we introduce the idea of combining diffusion distance on a feature
manifold with neural network-based unsupervised feature learning. This idea is
realized as a novel algorithm called DeepDiffusion (DD). DD simultaneously
optimizes two components, a feature embedding by a deep neural network and a
distance metric that leverages diffusion on a latent feature manifold,
together. DD relies on its loss function but not encoder architecture. It can
thus be applied to diverse multimedia data types with their respective encoder
architectures. Experimental evaluation using 3D shapes and 2D images
demonstrates versatility as well as high accuracy of the DD algorithm. Code is
available at https://github.com/takahikof/DeepDiffusion