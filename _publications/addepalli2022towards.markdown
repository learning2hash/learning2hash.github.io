---
layout: publication
title: Towards Efficient And Effective Self-supervised Learning Of Visual Representations
authors: Sravanti Addepalli, Kaushal Bhogale, Priyam Dey, R. Venkatesh Babu
conference: Lecture Notes in Computer Science
year: 2022
bibkey: addepalli2022towards
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.09866'}]
tags: ["Efficiency", "Self-Supervised"]
short_authors: Addepalli et al.
---
Self-supervision has emerged as a propitious method for visual representation
learning after the recent paradigm shift from handcrafted pretext tasks to
instance-similarity based approaches. Most state-of-the-art methods enforce
similarity between various augmentations of a given image, while some methods
additionally use contrastive approaches to explicitly ensure diverse
representations. While these approaches have indeed shown promising direction,
they require a significantly larger number of training iterations when compared
to the supervised counterparts. In this work, we explore reasons for the slow
convergence of these methods, and further propose to strengthen them using
well-posed auxiliary tasks that converge significantly faster, and are also
useful for representation learning. The proposed method utilizes the task of
rotation prediction to improve the efficiency of existing state-of-the-art
methods. We demonstrate significant gains in performance using the proposed
method on multiple datasets, specifically for lower training epochs.