---
layout: publication
title: Google Landmark Retrieval 2021 Competition Third Place Solution
authors: Qishen Ha, Bo Liu, Hongwei Zhang
conference: Arxiv
year: 2021
bibkey: ha2021google
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.04619'}]
tags: [Re-ranking]
short_authors: Qishen Ha, Bo Liu, Hongwei Zhang
---
We present our solutions to the Google Landmark Challenges 2021, for both the
retrieval and the recognition tracks. Both solutions are ensembles of
transformers and ConvNet models based on Sub-center ArcFace with dynamic
margins. Since the two tracks share the same training data, we used the same
pipeline and training approach, but with different model selections for the
ensemble and different post-processing. The key improvement over last year is
newer state-of-the-art vision architectures, especially transformers which
significantly outperform ConvNets for the retrieval task. We finished third and
fourth places for the retrieval and recognition tracks respectively.