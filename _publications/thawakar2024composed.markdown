---
layout: publication
title: Composed Video Retrieval Via Enriched Context And Discriminative Embeddings
authors: Omkar Thawakar, Muzammal Naseer, Rao Muhammad Anwer, Salman Khan, Michael
  Felsberg, Mubarak Shah, Fahad Shahbaz Khan
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: thawakar2024composed
citations: 2
additional_links: [{name: Code, url: 'https://github.com/OmkarThawakar/composed-video-retrieval'},
  {name: Paper, url: 'https://arxiv.org/abs/2403.16997'}]
tags: ["CVPR", "Video Retrieval"]
short_authors: Thawakar et al.
---
Composed video retrieval (CoVR) is a challenging problem in computer vision
which has recently highlighted the integration of modification text with visual
queries for more sophisticated video search in large databases. Existing works
predominantly rely on visual queries combined with modification text to
distinguish relevant videos. However, such a strategy struggles to fully
preserve the rich query-specific context in retrieved target videos and only
represents the target video using visual embedding. We introduce a novel CoVR
framework that leverages detailed language descriptions to explicitly encode
query-specific contextual information and learns discriminative embeddings of
vision only, text only and vision-text for better alignment to accurately
retrieve matched target videos. Our proposed framework can be flexibly employed
for both composed video (CoVR) and image (CoIR) retrieval tasks. Experiments on
three datasets show that our approach obtains state-of-the-art performance for
both CovR and zero-shot CoIR tasks, achieving gains as high as around 7% in
terms of recall@K=1 score. Our code, models, detailed language descriptions for
WebViD-CoVR dataset are available at
https://github.com/OmkarThawakar/composed-video-retrieval