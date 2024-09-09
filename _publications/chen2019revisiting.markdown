---
layout: publication
title: "Revisiting Consistent Hashing with Bounded Loads"
authors: Chen John, Coleman Ben, Shrivastava Anshumali
conference: "Arxiv"
year: 2019
bibkey: chen2019revisiting
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1908.08762"}
tags: ['ARXIV', 'GAN']
---
Dynamic load balancing lies at the heart of distributed caching. Here, the goal
is to assign objects (load) to servers (computing nodes) in a way that provides
load balancing while at the same time dynamically adjusts to the addition or
removal of servers. One essential requirement is that the addition or removal of
small servers should not require us to recompute the complete assignment. A
popular and widely adopted solution is the two-decade-old Consistent Hashing
(CH). Recently, an elegant extension was provided to account for server bounds.
In this paper, we identify that existing methodologies for CH and its variants
suffer from cascaded overflow, leading to poor load balancing. This cascading
effect leads to decreasing performance of the hashing procedure with increasing
load. To overcome the cascading effect, we propose a simple solution to CH based
on recent advances in fast minwise hashing. We show, both theoretically and
empirically, that our proposed solution is significantly superior for load
balancing and is optimal in many senses. On the AOL search dataset and Indiana
University Clicks dataset with real user activity, our proposed solution reduces
cache misses by several magnitudes.
