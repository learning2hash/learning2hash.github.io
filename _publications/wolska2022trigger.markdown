---
layout: publication
title: 'Trigger Warnings: Bootstrapping A Violence Detector For Fanfiction'
authors: "Magdalena Wolska, Christopher Schr\xF6der, Ole Borchardt, Benno Stein, Martin\
  \ Potthast"
conference: Arxiv
year: 2022
bibkey: wolska2022trigger
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.04409'}]
tags: ["Datasets", "Evaluation"]
short_authors: Wolska et al.
---
We present the first dataset and evaluation results on a newly defined
computational task of trigger warning assignment. Labeled corpus data has been
compiled from narrative works hosted on Archive of Our Own (AO3), a well-known
fanfiction site. In this paper, we focus on the most frequently assigned
trigger type--violence--and define a document-level binary classification task
of whether or not to assign a violence trigger warning to a fanfiction,
exploiting warning labels provided by AO3 authors. SVM and BERT models trained
in four evaluation setups on the corpora we compiled yield \(F_1\) results
ranging from 0.585 to 0.798, proving the violence trigger warning assignment to
be a doable, however, non-trivial task.