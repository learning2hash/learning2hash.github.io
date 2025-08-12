---
layout: publication
title: Meta Learning For Few-shot One-class Classification
authors: "Gabriel Dahia, Maur\xEDcio Pamplona Segundo"
conference: AI
year: 2021
bibkey: dahia2020meta
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2009.05353'}]
tags: ["Few Shot & Zero Shot"]
short_authors: "Gabriel Dahia, Maur\xEDcio Pamplona Segundo"
---
We propose a method that can perform one-class classification given only a
small number of examples from the target class and none from the others. We
formulate the learning of meaningful features for one-class classification as a
meta-learning problem in which the meta-training stage repeatedly simulates
one-class classification, using the classification loss of the chosen algorithm
to learn a feature representation. To learn these representations, we require
only multiclass data from similar tasks. We show how the Support Vector Data
Description method can be used with our method, and also propose a simpler
variant based on Prototypical Networks that obtains comparable performance,
indicating that learning feature representations directly from data may be more
important than which one-class algorithm we choose. We validate our approach by
adapting few-shot classification datasets to the few-shot one-class
classification scenario, obtaining similar results to the state-of-the-art of
traditional one-class classification, and that improves upon that of one-class
classification baselines employed in the few-shot setting. Our code is
available at https://github.com/gdahia/meta_occ