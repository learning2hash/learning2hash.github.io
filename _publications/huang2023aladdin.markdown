---
layout: publication
title: 'Aladdin: Zero-shot Hallucination Of Stylized 3D Assets From Abstract Scene
  Descriptions'
authors: Ian Huang, Vrishab Krishna, Omoruyi Atekha, Leonidas Guibas
conference: Arxiv
year: 2023
bibkey: huang2023aladdin
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.06212'}]
tags: []
short_authors: Huang et al.
---
What constitutes the "vibe" of a particular scene? What should one find in "a
busy, dirty city street", "an idyllic countryside", or "a crime scene in an
abandoned living room"? The translation from abstract scene descriptions to
stylized scene elements cannot be done with any generality by extant systems
trained on rigid and limited indoor datasets. In this paper, we propose to
leverage the knowledge captured by foundation models to accomplish this
translation. We present a system that can serve as a tool to generate stylized
assets for 3D scenes described by a short phrase, without the need to enumerate
the objects to be found within the scene or give instructions on their
appearance. Additionally, it is robust to open-world concepts in a way that
traditional methods trained on limited data are not, affording more creative
freedom to the 3D artist. Our system demonstrates this using a foundation model
"team" composed of a large language model, a vision-language model and several
image diffusion models, which communicate using an interpretable and
user-editable intermediate representation, thus allowing for more versatile and
controllable stylized asset generation for 3D artists. We introduce novel
metrics for this task, and show through human evaluations that in 91% of the
cases, our system outputs are judged more faithful to the semantics of the
input scene description than the baseline, thus highlighting the potential of
this approach to radically accelerate the 3D content creation process for 3D
artists.