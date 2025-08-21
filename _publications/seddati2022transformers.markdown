---
layout: publication
title: Transformers And Cnns Both Beat Humans On SBIR
authors: "Omar Seddati, St\xE9phane Dupont, Sa\xEFd Mahmoudi, Thierry Dutoit"
conference: Arxiv
year: 2022
bibkey: seddati2022transformers
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.06629'}]
tags: ["Evaluation", "Image Retrieval", "Scalability"]
short_authors: Seddati et al.
---
Sketch-based image retrieval (SBIR) is the task of retrieving natural images
(photos) that match the semantics and the spatial configuration of hand-drawn
sketch queries. The universality of sketches extends the scope of possible
applications and increases the demand for efficient SBIR solutions. In this
paper, we study classic triplet-based SBIR solutions and show that a persistent
invariance to horizontal flip (even after model finetuning) is harming
performance. To overcome this limitation, we propose several approaches and
evaluate in depth each of them to check their effectiveness. Our main
contributions are twofold: We propose and evaluate several intuitive
modifications to build SBIR solutions with better flip equivariance. We show
that vision transformers are more suited for the SBIR task, and that they
outperform CNNs with a large margin. We carried out numerous experiments and
introduce the first models to outperform human performance on a large-scale
SBIR benchmark (Sketchy). Our best model achieves a recall of 62.25% (at k = 1)
on the sketchy benchmark compared to previous state-of-the-art methods 46.2%.