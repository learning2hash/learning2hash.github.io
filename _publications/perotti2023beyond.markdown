---
layout: publication
title: 'Beyond One-hot-encoding: Injecting Semantics To Drive Image Classifiers'
authors: "Alan Perotti, Simone Bertolotto, Eliana Pastor, Andr\xE9 Panisson"
conference: Communications in Computer and Information Science
year: 2023
bibkey: perotti2023beyond
citations: 4
additional_links: [{name: Code, url: 'https://github.com/S1M0N38/semantic-encodings'},
  {name: Paper, url: 'https://arxiv.org/abs/2308.00607'}]
tags: ["Robustness"]
short_authors: Perotti et al.
---
Images are loaded with semantic information that pertains to real-world
ontologies: dog breeds share mammalian similarities, food pictures are often
depicted in domestic environments, and so on. However, when training machine
learning models for image classification, the relative similarities amongst
object classes are commonly paired with one-hot-encoded labels. According to
this logic, if an image is labelled as 'spoon', then 'tea-spoon' and 'shark'
are equally wrong in terms of training loss. To overcome this limitation, we
explore the integration of additional goals that reflect ontological and
semantic knowledge, improving model interpretability and trustworthiness. We
suggest a generic approach that allows to derive an additional loss term
starting from any kind of semantic information about the classification label.
First, we show how to apply our approach to ontologies and word embeddings, and
discuss how the resulting information can drive a supervised learning process.
Second, we use our semantically enriched loss to train image classifiers, and
analyse the trade-offs between accuracy, mistake severity, and learned internal
representations. Finally, we discuss how this approach can be further exploited
in terms of explainability and adversarial robustness. Code repository:
https://github.com/S1M0N38/semantic-encodings