---
layout: publication
title: Attention-based Vandalism Detection In Openstreetmap
authors: Nicolas Tempelmeier, Elena Demidova
conference: Proceedings of the ACM Web Conference 2022
year: 2022
bibkey: tempelmeier2022attention
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.10406'}]
tags: []
short_authors: Nicolas Tempelmeier, Elena Demidova
---
OpenStreetMap (OSM), a collaborative, crowdsourced Web map, is a unique
source of openly available worldwide map data, increasingly adopted in Web
applications. Vandalism detection is a critical task to support trust and
maintain OSM transparency. This task is remarkably challenging due to the large
scale of the dataset, the sheer number of contributors, various vandalism
forms, and the lack of annotated data. This paper presents Ovid - a novel
attention-based method for vandalism detection in OSM. Ovid relies on a novel
neural architecture that adopts a multi-head attention mechanism to summarize
information indicating vandalism from OSM changesets effectively. To facilitate
automated vandalism detection, we introduce a set of original features that
capture changeset, user, and edit information. Furthermore, we extract a
dataset of real-world vandalism incidents from the OSM edit history for the
first time and provide this dataset as open data. Our evaluation conducted on
real-world vandalism data demonstrates the effectiveness of Ovid.