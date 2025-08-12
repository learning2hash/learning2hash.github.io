---
layout: publication
title: Exposing Image Classifier Shortcuts With Counterfactual Frequency (cof) Tables
authors: James Hinns, David Martens
conference: Arxiv
year: 2024
bibkey: hinns2024exposing
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.15661'}]
tags: []
short_authors: James Hinns, David Martens
---
The rise of deep learning in image classification has brought unprecedented
accuracy but also highlighted a key issue: the use of 'shortcuts' by models.
Such shortcuts are easy-to-learn patterns from the training data that fail to
generalise to new data. Examples include the use of a copyright watermark to
recognise horses, snowy background to recognise huskies, or ink markings to
detect malignant skin lesions. The explainable AI (XAI) community has suggested
using instance-level explanations to detect shortcuts without external data,
but this requires the examination of many explanations to confirm the presence
of such shortcuts, making it a labour-intensive process. To address these
challenges, we introduce Counterfactual Frequency (CoF) tables, a novel
approach that aggregates instance-based explanations into global insights, and
exposes shortcuts. The aggregation implies the need for some semantic concepts
to be used in the explanations, which we solve by labelling the segments of an
image. We demonstrate the utility of CoF tables across several datasets,
revealing the shortcuts learned from them.