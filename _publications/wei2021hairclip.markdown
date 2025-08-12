---
layout: publication
title: 'Hairclip: Design Your Hair By Text And Reference Image'
authors: Tianyi Wei, Dongdong Chen, Wenbo Zhou, Jing Liao, Zhentao Tan, Lu Yuan, Weiming
  Zhang, Nenghai Yu
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: wei2021hairclip
citations: 68
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.05142'}]
tags: ["CVPR"]
short_authors: Wei et al.
---
Hair editing is an interesting and challenging problem in computer vision and
graphics. Many existing methods require well-drawn sketches or masks as
conditional inputs for editing, however these interactions are neither
straightforward nor efficient. In order to free users from the tedious
interaction process, this paper proposes a new hair editing interaction mode,
which enables manipulating hair attributes individually or jointly based on the
texts or reference images provided by users. For this purpose, we encode the
image and text conditions in a shared embedding space and propose a unified
hair editing framework by leveraging the powerful image text representation
capability of the Contrastive Language-Image Pre-Training (CLIP) model. With
the carefully designed network structures and loss functions, our framework can
perform high-quality hair editing in a disentangled manner. Extensive
experiments demonstrate the superiority of our approach in terms of
manipulation accuracy, visual realism of editing results, and irrelevant
attribute preservation. Project repo is https://github.com/wty-ustc/HairCLIP.