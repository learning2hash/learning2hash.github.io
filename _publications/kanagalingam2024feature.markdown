---
layout: publication
title: A Feature Generator For Few-shot Learning
authors: Heethanjan Kanagalingam, Thenukan Pathmanathan, Navaneethan Ketheeswaran,
  Mokeeshan Vathanakumar, Mohamed Afham, Ranga Rodrigo
conference: Lecture Notes in Computer Science
year: 2024
bibkey: kanagalingam2024feature
citations: 0
additional_links: [{name: Code, url: 'https://github.com/heethanjan/Feature-Generator-for-FSL'},
  {name: Paper, url: 'https://arxiv.org/abs/2409.14141'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Kanagalingam et al.
---
Few-shot learning (FSL) aims to enable models to recognize novel objects or
classes with limited labelled data. Feature generators, which synthesize new
data points to augment limited datasets, have emerged as a promising solution
to this challenge. This paper investigates the effectiveness of feature
generators in enhancing the embedding process for FSL tasks. To address the
issue of inaccurate embeddings due to the scarcity of images per class, we
introduce a feature generator that creates visual features from class-level
textual descriptions. By training the generator with a combination of
classifier loss, discriminator loss, and distance loss between the generated
features and true class embeddings, we ensure the generation of accurate
same-class features and enhance the overall feature representation. Our results
show a significant improvement in accuracy over baseline methods, with our
approach outperforming the baseline model by 10% in 1-shot and around 5% in
5-shot approaches. Additionally, both visual-only and visual + textual
generators have also been tested in this paper. The code is publicly available
at https://github.com/heethanjan/Feature-Generator-for-FSL.