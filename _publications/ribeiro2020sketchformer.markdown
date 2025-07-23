---
layout: publication
title: 'Sketchformer: Transformer-based Representation For Sketched Structure'
authors: Ribeiro Leo Sampaio Ferraz, Bui Tu, Collomosse John, Ponti Moacir
conference: 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2020
bibkey: ribeiro2020sketchformer
citations: 83
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.10381'}]
tags: ["CVPR", "Image Retrieval", "Transformer-based ANN"]
short_authors: Ribeiro et al.
---
Sketchformer is a novel transformer-based representation for encoding
free-hand sketches input in a vector form, i.e. as a sequence of strokes.
Sketchformer effectively addresses multiple tasks: sketch classification,
sketch based image retrieval (SBIR), and the reconstruction and interpolation
of sketches. We report several variants exploring continuous and tokenized
input representations, and contrast their performance. Our learned embedding,
driven by a dictionary learning tokenization scheme, yields state of the art
performance in classification and image retrieval tasks, when compared against
baseline representations driven by LSTM sequence to sequence architectures:
SketchRNN and derivatives. We show that sketch reconstruction and interpolation
are improved significantly by the Sketchformer embedding for complex sketches
with longer stroke sequences.