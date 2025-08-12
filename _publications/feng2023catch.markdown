---
layout: publication
title: 'Catch You Everything Everywhere: Guarding Textual Inversion Via Concept Watermarking'
authors: Weitao Feng, Jiyan He, Jie Zhang, Tianwei Zhang, Wenbo Zhou, Weiming Zhang,
  Nenghai Yu
conference: Arxiv
year: 2023
bibkey: feng2023catch
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.05940'}]
tags: ["Privacy & Security", "Robustness"]
short_authors: Feng et al.
---
AIGC (AI-Generated Content) has achieved tremendous success in many
applications such as text-to-image tasks, where the model can generate
high-quality images with diverse prompts, namely, different descriptions in
natural languages. More surprisingly, the emerging personalization techniques
even succeed in describing unseen concepts with only a few personal images as
references, and there have been some commercial platforms for sharing the
valuable personalized concept. However, such an advanced technique also
introduces a severe threat, where malicious users can misuse the target concept
to generate highly-realistic illegal images. Therefore, it becomes necessary
for the platform to trace malicious users and hold them accountable.
  In this paper, we focus on guarding the most popular lightweight
personalization model, ie, Textual Inversion (TI). To achieve it, we propose
the novel concept watermarking, where watermark information is embedded into
the target concept and then extracted from generated images based on the
watermarked concept. Specifically, we jointly train a watermark encoder and a
watermark decoder with the sampler in the loop.
  It shows great resilience to different diffusion sampling processes possibly
chosen by malicious users, meanwhile preserving utility for normal use. In
practice, the concept owner can upload his concept with different watermarks
(ie, serial numbers) to the platform, and the platform allocates different
users with different serial numbers for subsequent tracing and forensics.