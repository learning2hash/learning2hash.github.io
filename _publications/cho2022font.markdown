---
layout: publication
title: Font Representation Learning Via Paired-glyph Matching
authors: Junho Cho, Kyuewang Lee, Jin Young Choi
conference: Arxiv
year: 2022
bibkey: cho2022font
citations: 0
additional_links: [{name: Code, url: 'https://github.com/junhocho/paired-glyph-matching'},
  {name: Paper, url: 'https://arxiv.org/abs/2211.10967'}]
tags: ["Evaluation"]
short_authors: Junho Cho, Kyuewang Lee, Jin Young Choi
---
Fonts can convey profound meanings of words in various forms of glyphs.
Without typography knowledge, manually selecting an appropriate font or
designing a new font is a tedious and painful task. To allow users to explore
vast font styles and create new font styles, font retrieval and font style
transfer methods have been proposed. These tasks increase the need for learning
high-quality font representations. Therefore, we propose a novel font
representation learning scheme to embed font styles into the latent space. For
the discriminative representation of a font from others, we propose a
paired-glyph matching-based font representation learning model that attracts
the representations of glyphs in the same font to one another, but pushes away
those of other fonts. Through evaluations on font retrieval with query glyphs
on new fonts, we show our font representation learning scheme achieves better
generalization performance than the existing font representation learning
techniques. Finally on the downstream font style transfer and generation tasks,
we confirm the benefits of transfer learning with the proposed method. The
source code is available at https://github.com/junhocho/paired-glyph-matching.