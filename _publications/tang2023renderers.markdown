---
layout: publication
title: 'Renderers Are Good Zero-shot Representation Learners: Exploring Diffusion
  Latents For Metric Learning'
authors: Tang Michael, Shustin David
conference: Proceedings of the Twenty-Eighth International Joint Conference on Artificial
  Intelligence
year: 2023
bibkey: tang2023renderers
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.10721'}]
tags: ["Few Shot & Zero Shot", "Distance Metric Learning", "AAAI", "IJCAI"]
---
Can the latent spaces of modern generative neural rendering models serve as
representations for 3D-aware discriminative visual understanding tasks? We use
retrieval as a proxy for measuring the metric learning properties of the latent
spaces of Shap-E, including capturing view-independence and enabling the
aggregation of scene representations from the representations of individual
image views, and find that Shap-E representations outperform those of the
classical EfficientNet baseline representations zero-shot, and is still
competitive when both methods are trained using a contrative loss. These
findings give preliminary indication that 3D-based rendering and generative
models can yield useful representations for discriminative tasks in our
innately 3D-native world. Our code is available at
https://github.com/michaelwilliamtang/golden-retriever.