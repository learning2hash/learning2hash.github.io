---
layout: publication
title: 'Openscene: 3D Scene Understanding With Open Vocabularies'
authors: Songyou Peng, Kyle Genova, Chiyu "max" Jiang, Andrea Tagliasacchi, Marc Pollefeys,
  Thomas Funkhouser
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: peng2022openscene
citations: 139
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.15654'}]
tags: ["CVPR", "Datasets", "Evaluation", "Few Shot & Zero Shot"]
short_authors: Peng et al.
---
Traditional 3D scene understanding approaches rely on labeled 3D datasets to
train a model for a single task with supervision. We propose OpenScene, an
alternative approach where a model predicts dense features for 3D scene points
that are co-embedded with text and image pixels in CLIP feature space. This
zero-shot approach enables task-agnostic training and open-vocabulary queries.
For example, to perform SOTA zero-shot 3D semantic segmentation it first infers
CLIP features for every 3D point and later classifies them based on
similarities to embeddings of arbitrary class labels. More interestingly, it
enables a suite of open-vocabulary scene understanding applications that have
never been done before. For example, it allows a user to enter an arbitrary
text query and then see a heat map indicating which parts of a scene match. Our
approach is effective at identifying objects, materials, affordances,
activities, and room types in complex 3D scenes, all using a single model
trained without any labeled 3D data.