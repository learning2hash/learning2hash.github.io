---
layout: publication
title: 'Colonmapper: Topological Mapping And Localization For Colonoscopy'
authors: "Javier Morlana, Juan D. Tard\xF3s, J. M. M. Montiel"
conference: 2024 IEEE International Conference on Robotics and Automation (ICRA)
year: 2024
bibkey: morlana2023colonmapper
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.05546'}]
tags: ["ICRA"]
short_authors: "Javier Morlana, Juan D. Tard\xF3s, J. M. M. Montiel"
---
We propose a topological mapping and localization system able to operate on
real human colonoscopies, despite significant shape and illumination changes.
The map is a graph where each node codes a colon location by a set of real
images, while edges represent traversability between nodes. For close-in-time
images, where scene changes are minor, place recognition can be successfully
managed with the recent transformers-based local feature matching algorithms.
However, under long-term changes -- such as different colonoscopies of the same
patient -- feature-based matching fails. To address this, we train on real
colonoscopies a deep global descriptor achieving high recall with significant
changes in the scene. The addition of a Bayesian filter boosts the accuracy of
long-term place recognition, enabling relocalization in a previously built map.
Our experiments show that ColonMapper is able to autonomously build a map and
localize against it in two important use cases: localization within the same
colonoscopy or within different colonoscopies of the same patient. Code:
https://github.com/jmorlana/ColonMapper.