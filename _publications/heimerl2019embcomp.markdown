---
layout: publication
title: 'Embcomp: Visual Interactive Comparison Of Vector Embeddings'
authors: "Florian Heimerl, Christoph Kralj, Torsten M\xF6ller, Michael Gleicher"
conference: IEEE Transactions on Visualization and Computer Graphics
year: 2019
bibkey: heimerl2019embcomp
citations: 26
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.01542'}]
tags: ["Evaluation", "Survey Paper"]
short_authors: Heimerl et al.
---
This paper introduces embComp, a novel approach for comparing two embeddings
that capture the similarity between objects, such as word and document
embeddings. We survey scenarios where comparing these embedding spaces is
useful. From those scenarios, we derive common tasks, introduce visual analysis
methods that support these tasks, and combine them into a comprehensive system.
One of embComp's central features are overview visualizations that are based on
metrics for measuring differences in the local structure around objects.
Summarizing these local metrics over the embeddings provides global overviews
of similarities and differences. Detail views allow comparison of the local
structure around selected objects and relating this local information to the
global views. Integrating and connecting all of these components, embComp
supports a range of analysis workflows that help understand similarities and
differences between embedding spaces. We assess our approach by applying it in
several use cases, including understanding corpora differences via word vector
embeddings, and understanding algorithmic differences in generating embeddings.