---
layout: publication
title: 'J-viz: Sibling-first Recursive Graph Drawing For Visualizing Java Bytecode'
authors: Md. Jawaherul Alam, Michael T. Goodrich, Timothy Johnson
conference: Arxiv
year: 2016
bibkey: alam2016j
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1608.08970'}]
tags: ["Tools & Libraries"]
short_authors: Md. Jawaherul Alam, Michael T. Goodrich, Timothy Johnson
---
We describe a graph visualization tool for visualizing Java bytecode. Our
tool, which we call J-Viz, visualizes connected directed graphs according to a
canonical node ordering, which we call the sibling-first recursive (SFR)
numbering. The particular graphs we consider are derived from applying Shiver's
k-CFA framework to Java bytecode, and our visualizer includes helpful links
between the nodes of an input graph and the Java bytecode that produced it, as
well as a decompiled version of that Java bytecode. We show through several
case studies that the canonical drawing paradigm used in J-Viz is effective for
identifying potential security vulnerabilities and repeated use of the same
code in Java applications.