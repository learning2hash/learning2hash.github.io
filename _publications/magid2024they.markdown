---
layout: publication
title: 'They''re All Doctors: Synthesizing Diverse Counterfactuals To Mitigate Associative
  Bias'
authors: Salma Abdel Magid, Jui-Hsien Wang, Kushal Kafle, Hanspeter Pfister
conference: Arxiv
year: 2024
bibkey: magid2024they
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.11331'}]
tags: ["Datasets", "Evaluation", "Image Retrieval", "Tools & Libraries", "Video Retrieval"]
short_authors: Magid et al.
---
Vision Language Models (VLMs) such as CLIP are powerful models; however they
can exhibit unwanted biases, making them less safe when deployed directly in
applications such as text-to-image, text-to-video retrievals, reverse search,
or classification tasks. In this work, we propose a novel framework to generate
synthetic counterfactual images to create a diverse and balanced dataset that
can be used to fine-tune CLIP. Given a set of diverse synthetic base images
from text-to-image models, we leverage off-the-shelf segmentation and
inpainting models to place humans with diverse visual appearances in context.
We show that CLIP trained on such datasets learns to disentangle the human
appearance from the context of an image, i.e., what makes a doctor is not
correlated to the person's visual appearance, like skin color or body type, but
to the context, such as background, the attire they are wearing, or the objects
they are holding. We demonstrate that our fine-tuned CLIP model, \(CF_\alpha\),
improves key fairness metrics such as MaxSkew, MinSkew, and NDKL by 40-66% for
image retrieval tasks, while still achieving similar levels of performance in
downstream tasks. We show that, by design, our model retains maximal
compatibility with the original CLIP models, and can be easily controlled to
support different accuracy versus fairness trade-offs in a plug-n-play fashion.