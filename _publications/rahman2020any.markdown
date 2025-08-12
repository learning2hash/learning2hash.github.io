---
layout: publication
title: Any-shot Object Detection
authors: Shafin Rahman, Salman Khan, Nick Barnes, Fahad Shahbaz Khan
conference: Lecture Notes in Computer Science
year: 2021
bibkey: rahman2020any
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2003.07003'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Rahman et al.
---
Previous work on novel object detection considers zero or few-shot settings
where none or few examples of each category are available for training. In real
world scenarios, it is less practical to expect that 'all' the novel classes
are either unseen or \{have\} few-examples. Here, we propose a more realistic
setting termed 'Any-shot detection', where totally unseen and few-shot
categories can simultaneously co-occur during inference. Any-shot detection
offers unique challenges compared to conventional novel object detection such
as, a high imbalance between unseen, few-shot and seen object classes,
susceptibility to forget base-training while learning novel classes and
distinguishing novel classes from the background. To address these challenges,
we propose a unified any-shot detection model, that can concurrently learn to
detect both zero-shot and few-shot object classes. Our core idea is to use
class semantics as prototypes for object detection, a formulation that
naturally minimizes knowledge forgetting and mitigates the class-imbalance in
the label space. Besides, we propose a rebalanced loss function that emphasizes
difficult few-shot cases but avoids overfitting on the novel classes to allow
detection of totally unseen classes. Without bells and whistles, our framework
can also be used solely for Zero-shot detection and Few-shot detection tasks.
We report extensive experiments on Pascal VOC and MS-COCO datasets where our
approach is shown to provide significant improvements.