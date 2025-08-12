---
layout: publication
title: Fashion Image-to-image Translation For Complementary Item Retrieval
authors: Matteo Attimonelli, Claudio Pomo, Dietmar Jannach, Tommaso di Noia
conference: Arxiv
year: 2024
bibkey: attimonelli2024fashion
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.09847'}]
tags: ["Image Retrieval"]
short_authors: Attimonelli et al.
---
The increasing demand for online fashion retail has boosted research in
fashion compatibility modeling and item retrieval, focusing on matching user
queries (textual descriptions or reference images) with compatible fashion
items. A key challenge is top-bottom retrieval, where precise compatibility
modeling is essential. Traditional methods, often based on Bayesian
Personalized Ranking (BPR), have shown limited performance. Recent efforts have
explored using generative models in compatibility modeling and item retrieval,
where generated images serve as additional inputs. However, these approaches
often overlook the quality of generated images, which could be crucial for
model performance. Additionally, generative models typically require large
datasets, posing challenges when such data is scarce.
  To address these issues, we introduce the Generative Compatibility Model
(GeCo), a two-stage approach that improves fashion image retrieval through
paired image-to-image translation. First, the Complementary Item Generation
Model (CIGM), built on Conditional Generative Adversarial Networks (GANs),
generates target item images (e.g., bottoms) from seed items (e.g., tops),
offering conditioning signals for retrieval. These generated samples are then
integrated into GeCo, enhancing compatibility modeling and retrieval accuracy.
Evaluations on three datasets show that GeCo outperforms state-of-the-art
baselines. Key contributions include: (i) the GeCo model utilizing paired
image-to-image translation within the Composed Image Retrieval framework, (ii)
comprehensive evaluations on benchmark datasets, and (iii) the release of a new
Fashion Taobao dataset designed for top-bottom retrieval, promoting further
research.