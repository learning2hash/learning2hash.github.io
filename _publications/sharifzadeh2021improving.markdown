---
layout: publication
title: Improving Scene Graph Classification By Exploiting Knowledge From Texts
authors: "Sahand Sharifzadeh, Sina Moayed Baharlou, Martin Schmitt, Hinrich Sch\xFC\
  tze, Volker Tresp"
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2022
bibkey: sharifzadeh2021improving
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.04760'}]
tags: ["AAAI"]
short_authors: Sharifzadeh et al.
---
Training scene graph classification models requires a large amount of
annotated image data. Meanwhile, scene graphs represent relational knowledge
that can be modeled with symbolic data from texts or knowledge graphs. While
image annotation demands extensive labor, collecting textual descriptions of
natural scenes requires less effort. In this work, we investigate whether
textual scene descriptions can substitute for annotated image data. To this
end, we employ a scene graph classification framework that is trained not only
from annotated images but also from symbolic data. In our architecture, the
symbolic entities are first mapped to their correspondent image-grounded
representations and then fed into the relational reasoning pipeline. Even
though a structured form of knowledge, such as the form in knowledge graphs, is
not always available, we can generate it from unstructured texts using a
transformer-based language model. We show that by fine-tuning the
classification pipeline with the extracted knowledge from texts, we can achieve
~8x more accurate results in scene graph classification, ~3x in object
classification, and ~1.5x in predicate classification, compared to the
supervised baselines with only 1% of the annotated images.