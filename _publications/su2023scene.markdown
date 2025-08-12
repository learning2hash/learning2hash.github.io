---
layout: publication
title: Scene Style Text Editing
authors: Tonghua Su, Fuxiang Yang, Xiang Zhou, Donglin di, Zhongjie Wang, Songze Li
conference: Arxiv
year: 2023
bibkey: su2023scene
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.10097'}]
tags: []
short_authors: Su et al.
---
In this work, we propose a task called "Scene Style Text Editing (SSTE)",
changing the text content as well as the text style of the source image while
keeping the original text scene. Existing methods neglect to fine-grained
adjust the style of the foreground text, such as its rotation angle, color, and
font type. To tackle this task, we propose a quadruple framework named
"QuadNet" to embed and adjust foreground text styles in the latent feature
space. Specifically, QuadNet consists of four parts, namely background
inpainting, style encoder, content encoder, and fusion generator. The
background inpainting erases the source text content and recovers the
appropriate background with a highly authentic texture. The style encoder
extracts the style embedding of the foreground text. The content encoder
provides target text representations in the latent feature space to implement
the content edits. The fusion generator combines the information yielded from
the mentioned parts and generates the rendered text images. Practically, our
method is capable of performing promisingly on real-world datasets with merely
string-level annotation. To the best of our knowledge, our work is the first to
finely manipulate the foreground text content and style by deeply semantic
editing in the latent feature space. Extensive experiments demonstrate that
QuadNet has the ability to generate photo-realistic foreground text and avoid
source text shadows in real-world scenes when editing text content.