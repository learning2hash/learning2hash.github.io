---
layout: publication
title: Give Me A Hint! Navigating Image Databases Using Human-in-the-loop Feedback
authors: Plummer et al.
conference: 2019 IEEE Winter Conference on Applications of Computer Vision (WACV)
year: 2019
bibkey: plummer2019give
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1809.08714'}]
---
In this paper, we introduce an attribute-based interactive image search which
can leverage human-in-the-loop feedback to iteratively refine image search
results. We study active image search where human feedback is solicited
exclusively in visual form, without using relative attribute annotations used
by prior work which are not typically found in many datasets. In order to
optimize the image selection strategy, a deep reinforcement model is trained to
learn what images are informative rather than rely on hand-crafted measures
typically leveraged in prior work. Additionally, we extend the recently
introduced Conditional Similarity Network to incorporate global similarity in
training visual embeddings, which results in more natural transitions as the
user explores the learned similarity embeddings. Our experiments demonstrate
the effectiveness of our approach, producing compelling results on both active
image search and image attribute representation tasks.