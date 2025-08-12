---
layout: publication
title: Controlling Style And Semantics In Weakly-supervised Image Generation
authors: Dario Pavllo, Aurelien Lucchi, Thomas Hofmann
conference: Lecture Notes in Computer Science
year: 2020
bibkey: pavllo2019controlling
citations: 32
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.03161'}]
tags: ["Supervised"]
short_authors: Dario Pavllo, Aurelien Lucchi, Thomas Hofmann
---
We propose a weakly-supervised approach for conditional image generation of
complex scenes where a user has fine control over objects appearing in the
scene. We exploit sparse semantic maps to control object shapes and classes, as
well as textual descriptions or attributes to control both local and global
style. In order to condition our model on textual descriptions, we introduce a
semantic attention module whose computational cost is independent of the image
resolution. To further augment the controllability of the scene, we propose a
two-step generation scheme that decomposes background and foreground. The label
maps used to train our model are produced by a large-vocabulary object
detector, which enables access to unlabeled data and provides structured
instance information. In such a setting, we report better FID scores compared
to fully-supervised settings where the model is trained on ground-truth
semantic maps. We also showcase the ability of our model to manipulate a scene
on complex datasets such as COCO and Visual Genome.