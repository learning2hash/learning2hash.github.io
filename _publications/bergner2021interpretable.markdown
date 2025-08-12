---
layout: publication
title: Interpretable And Interactive Deep Multiple Instance Learning For Dental Caries
  Classification In Bitewing X-rays
authors: Benjamin Bergner, Csaba Rohrer, Aiham Taleb, Martha Duchrau, Guilherme de
  Leon, Jonas Almeida Rodrigues, Falk Schwendicke, Joachim Krois, Christoph Lippert
conference: Arxiv
year: 2021
bibkey: bergner2021interpretable
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.09694'}]
tags: []
short_authors: Bergner et al.
---
We propose a simple and efficient image classification architecture based on
deep multiple instance learning, and apply it to the challenging task of caries
detection in dental radiographs. Technically, our approach contributes in two
ways: First, it outputs a heatmap of local patch classification probabilities
despite being trained with weak image-level labels. Second, it is amenable to
learning from segmentation labels to guide training. In contrast to existing
methods, the human user can faithfully interpret predictions and interact with
the model to decide which regions to attend to. Experiments are conducted on a
large clinical dataset of \(\sim\)38k bitewings (\(\sim\)316k teeth), where we
achieve competitive performance compared to various baselines. When guided by
an external caries segmentation model, a significant improvement in
classification and localization performance is observed.