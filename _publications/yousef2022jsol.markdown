---
layout: publication
title: 'JSOL: Javascript Open-source Library For Grammar Of Graphics'
authors: Waleed A. Yousef, Hisham E. Mohammed, Andrew A. Naguib, Rafat S. Eid, Sherif
  E. Emabrak, Ahmed F. Hamed, Yusuf M. Khalifa, Shrouk T. Abdelrheem, Eman A. Awad,
  Sara G. Gaafar, Alaa M. Mamdoh, Nada A. Shawky
conference: Arxiv
year: 2022
bibkey: yousef2022jsol
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.04205'}]
tags: ["Tools & Libraries"]
short_authors: Yousef et al.
---
In this paper, we introduce the JavaScript Open-source Library (\libname), a
high-level grammar for representing data in visualization graphs and plots.
\libname~perspective on the grammar of graphics is unique; it provides
state-of-art rules for encoding visual primitives that can be used to generate
a known scene or to invent a new one. \libname~has ton rules developed
specifically for data-munging, mapping, and visualization through many layers,
such as algebra, scales, and geometries. Additionally, it has a compiler that
incorporates and combines all rules specified by a user and put them in a flow
to validate it as a visualization grammar and check its requisites. Users can
customize scenes through a pipeline that either puts customized rules or comes
with new ones. We evaluated \libname~on a multitude of plots to check rules
specification of customizing a specific plot. Although the project is still
under development and many enhancements are under construction, this paper
describes the first developed version of \libname, circa 2016, where an
open-source version of it is available. One immediate practical deployment for
JSOl is to be integrated with the open-source version of the Data Visualization
Platform (DVP) \citep\{Yousef2019DVP-arxiv\}