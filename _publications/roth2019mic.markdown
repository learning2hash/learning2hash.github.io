---
layout: publication
title: 'MIC: Mining Interclass Characteristics For Improved Metric Learning'
authors: "Roth Karsten, Brattoli Biagio, Ommer Bj\xF6rn"
conference: 2019 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2019
bibkey: roth2019mic
citations: 92
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.11574'}]
tags: ["Distance Metric Learning", "ICCV"]
short_authors: "Roth Karsten, Brattoli Biagio, Ommer Bj\xF6rn"
---
Metric learning seeks to embed images of objects suchthat class-defined
relations are captured by the embeddingspace. However, variability in images is
not just due to different depicted object classes, but also depends on other
latent characteristics such as viewpoint or illumination. In addition to these
structured properties, random noise further obstructs the visual relations of
interest. The common approach to metric learning is to enforce a representation
that is invariant under all factors but the ones of interest. In contrast, we
propose to explicitly learn the latent characteristics that are shared by and
go across object classes. We can then directly explain away structured visual
variability, rather than assuming it to be unknown random noise. We propose a
novel surrogate task to learn visual characteristics shared across classes with
a separate encoder. This encoder is trained jointly with the encoder for class
information by reducing their mutual information. On five standard image
retrieval benchmarks the approach significantly improves upon the
state-of-the-art.