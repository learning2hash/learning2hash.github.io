---
layout: publication
title: Meta-personalizing Vision-language Models To Find Named Instances In Video
authors: Chun-Hsiao Yeh, Bryan Russell, Josef Sivic, Fabian Caba Heilbron, Simon Jenni
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: yeh2023meta
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.10169'}]
tags: ["CVPR", "Datasets", "Evaluation", "Scalability"]
short_authors: Yeh et al.
---
Large-scale vision-language models (VLM) have shown impressive results for
language-guided search applications. While these models allow category-level
queries, they currently struggle with personalized searches for moments in a
video where a specific object instance such as ``My dog Biscuit'' appears. We
present the following three contributions to address this problem. First, we
describe a method to meta-personalize a pre-trained VLM, i.e., learning how to
learn to personalize a VLM at test time to search in video. Our method extends
the VLM's token vocabulary by learning novel word embeddings specific to each
instance. To capture only instance-specific features, we represent each
instance embedding as a combination of shared and learned global category
features. Second, we propose to learn such personalization without explicit
human supervision. Our approach automatically identifies moments of named
visual instances in video using transcripts and vision-language similarity in
the VLM's embedding space. Finally, we introduce This-Is-My, a personal video
instance retrieval benchmark. We evaluate our approach on This-Is-My and
DeepFashion2 and show that we obtain a 15% relative improvement over the state
of the art on the latter dataset.