---
layout: publication
title: Mining For Strong Gravitational Lenses With Self-supervised Learning
authors: George Stein, Jacqueline Blaum, Peter Harrington, Tomislav Medan, Zarija
  Lukic
conference: The Astrophysical Journal
year: 2021
bibkey: stein2021mining
citations: 42
additional_links: [{name: Code, url: 'https://github.com/georgestein/ssl-legacysurvey'},
  {name: Paper, url: 'https://arxiv.org/abs/2110.00023'}]
tags: ["Efficiency", "Self-Supervised", "Similarity Search", "Supervised", "Survey Paper"]
short_authors: Stein et al.
---
We employ self-supervised representation learning to distill information from
76 million galaxy images from the Dark Energy Spectroscopic Instrument Legacy
Imaging Surveys' Data Release 9. Targeting the identification of new strong
gravitational lens candidates, we first create a rapid similarity search tool
to discover new strong lenses given only a single labelled example. We then
show how training a simple linear classifier on the self-supervised
representations, requiring only a few minutes on a CPU, can automatically
classify strong lenses with great efficiency. We present 1192 new strong lens
candidates that we identified through a brief visual identification campaign,
and release an interactive web-based similarity search tool and the top network
predictions to facilitate crowd-sourcing rapid discovery of additional strong
gravitational lenses and other rare objects:
https://github.com/georgestein/ssl-legacysurvey.