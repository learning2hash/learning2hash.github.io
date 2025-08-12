---
layout: publication
title: 'Fast Bitmap Fit: A CPU Cache Line Friendly Memory Allocator For Single Object
  Allocations'
authors: Dhruv Matani, Gaurav Menghani
conference: Arxiv
year: 2021
bibkey: matani2021fast
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.10357'}]
tags: ["Efficiency"]
short_authors: Dhruv Matani, Gaurav Menghani
---
Applications making excessive use of single-object based data structures
(such as linked lists, trees, etc...) can see a drop in efficiency over a
period of time due to the randomization of nodes in memory. This slow down is
due to the ineffective use of the CPU's L1/L2 cache. We present a novel
approach for mitigating this by presenting the design of a single-object memory
allocator that preserves memory locality across randomly ordered memory
allocations and deallocations.