---
layout: publication
title: A Multimodal Approach For Cross-domain Image Retrieval
authors: Lucas Iijima, Nikolaos Giakoumoglou, Tania Stathaki
conference: Arxiv
year: 2024
bibkey: iijima2024multimodal
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.15152'}]
tags: ["Datasets", "Evaluation", "Image Retrieval", "Multimodal Retrieval", "Supervised", "Unsupervised"]
short_authors: Lucas Iijima, Nikolaos Giakoumoglou, Tania Stathaki
---
Cross-Domain Image Retrieval (CDIR) is a challenging task in computer vision,
aiming to match images across different visual domains such as sketches,
paintings, and photographs. Traditional approaches focus on visual image
features and rely heavily on supervised learning with labeled data and
cross-domain correspondences, which leads to an often struggle with the
significant domain gap. This paper introduces a novel unsupervised approach to
CDIR that incorporates textual context by leveraging pre-trained
vision-language models. Our method, dubbed as Caption-Matching (CM), uses
generated image captions as a domain-agnostic intermediate representation,
enabling effective cross-domain similarity computation without the need for
labeled data or fine-tuning. We evaluate our method on standard CDIR benchmark
datasets, demonstrating state-of-the-art performance in unsupervised settings
with improvements of 24.0% on Office-Home and 132.2% on DomainNet over previous
methods. We also demonstrate our method's effectiveness on a dataset of
AI-generated images from Midjourney, showcasing its ability to handle complex,
multi-domain queries.