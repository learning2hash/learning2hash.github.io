---
layout: publication
title: Accurate Bundle Matching And Generation Via Multitask Learning With Partially
  Shared Parameters
authors: Hyunsik Jeon, Jun-gi Jang, Taehun Kim, U Kang
conference: PLOS ONE
year: 2023
bibkey: jeon2022accurate
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.15460'}]
tags: []
short_authors: Jeon et al.
---
How can we recommend existing bundles to users accurately? How can we
generate new tailored bundles for users? Recommending a bundle, or a group of
various items, has attracted widespread attention in e-commerce owing to the
increased satisfaction of both users and providers. Bundle matching and bundle
generation are two representative tasks in bundle recommendation. The bundle
matching task is to correctly match existing bundles to users while the bundle
generation is to generate new bundles that users would prefer. Although many
recent works have developed bundle recommendation models, they fail to achieve
high accuracy since they do not handle heterogeneous data effectively and do
not learn a method for customized bundle generation. In this paper, we propose
BundleMage, an accurate approach for bundle matching and generation. BundleMage
effectively mixes user preferences of items and bundles using an adaptive gate
technique to achieve high accuracy for the bundle matching. BundleMage also
generates a personalized bundle by learning a generation module that exploits a
user preference and the characteristic of a given incomplete bundle to be
completed. BundleMage further improves its performance using multi-task
learning with partially shared parameters. Through extensive experiments, we
show that BundleMage achieves up to 6.6% higher nDCG in bundle matching and
6.3x higher nDCG in bundle generation than the best competitors. We also
provide qualitative analysis that BundleMage effectively generates bundles
considering both the tastes of users and the characteristics of target bundles.