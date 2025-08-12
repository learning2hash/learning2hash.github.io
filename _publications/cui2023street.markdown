---
layout: publication
title: 'Street Tryon: Learning In-the-wild Virtual Try-on From Unpaired Person Images'
authors: Aiyu Cui, Jay Mahajan, Viraj Shah, Preeti Gomathinayagam, Chang Liu, Svetlana
  Lazebnik
conference: Arxiv
year: 2023
bibkey: cui2023street
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.16094'}]
tags: ["Evaluation"]
short_authors: Cui et al.
---
Most virtual try-on research is motivated to serve the fashion business by
generating images to demonstrate garments on studio models at a lower cost.
However, virtual try-on should be a broader application that also allows
customers to visualize garments on themselves using their own casual photos,
known as in-the-wild try-on. Unfortunately, the existing methods, which achieve
plausible results for studio try-on settings, perform poorly in the in-the-wild
context. This is because these methods often require paired images (garment
images paired with images of people wearing the same garment) for training.
While such paired data is easy to collect from shopping websites for studio
settings, it is difficult to obtain for in-the-wild scenes.
  In this work, we fill the gap by (1) introducing a StreetTryOn benchmark to
support in-the-wild virtual try-on applications and (2) proposing a novel
method to learn virtual try-on from a set of in-the-wild person images directly
without requiring paired data. We tackle the unique challenges, including
warping garments to more diverse human poses and rendering more complex
backgrounds faithfully, by a novel DensePose warping correction method combined
with diffusion-based conditional inpainting. Our experiments show competitive
performance for standard studio try-on tasks and SOTA performance for street
try-on and cross-domain try-on tasks.