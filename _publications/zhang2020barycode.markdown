---
layout: publication
title: Barycode-based GJK Algorithm
authors: Yu Zhang, Yangming Wu, Xigui Wang, Xiaocheng Zhou
conference: Arxiv
year: 2020
bibkey: zhang2020barycode
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2011.09117'}]
tags: []
short_authors: Zhang et al.
---
In this paper, we present a more efficient GJK algorithm to solve the
collision detection and distance query problems in 2D. We contribute in two
aspects: First, we propose a new barycode-based sub-distance algorithm that
does not only provide a simple and unified condition to determine the minimum
simplex but also improve the efficiency in distant, touching, and overlap cases
in distance query. Second, we provide a highly efficient implementation
subroutine for collision detection by optimizing the exit conditions of our GJK
distance algorithm, which shows dramatic improvements in run-time for
applications that only need binary results. We benchmark our methods along with
that of the well-known open-source collision detection libraries, such as
Bullet, FCL, OpenGJK, Box2D, and Apollo over a range of random datasets. The
results indicate that our methods and implementations outperform the
state-of-the-art in both collision detection and distance query.