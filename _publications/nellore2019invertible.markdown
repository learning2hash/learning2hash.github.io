---
layout: publication
title: An Invertible Transform For Efficient String Matching In Labeled Digraphs
authors: Abhinav Nellore, Austin Nguyen, Reid F. Thompson
conference: CPM 2021
year: 2019
bibkey: nellore2019invertible
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1905.03424'}]
tags: ["Efficiency"]
short_authors: Abhinav Nellore, Austin Nguyen, Reid F. Thompson
---
Let \(G = (V, E)\) be a digraph where each vertex is unlabeled, each edge is
labeled by a character in some alphabet \(Ω\), and any two edges with both
the same head and the same tail have different labels. The powerset
construction gives a transform of \(G\) into a weakly connected digraph \(G' =
(V', E')\) that enables solving the decision problem of whether there is a walk
in \(G\) matching an arbitrarily long query string \(q\) in time linear in \(|q|\)
and independent of \(|E|\) and \(|V|\). We show \(G\) is uniquely determined by \(G'\)
when for every \(v_\ell \in V\), there is some distinct string \(s_\ell\) on
\(Ω\) such that \(v_\ell\) is the origin of a closed walk in \(G\) matching
\(s_\ell\), and no other walk in \(G\) matches \(s_\ell\) unless it starts and ends
at \(v_\ell\). We then exploit this invertibility condition to strategically
alter any \(G\) so its transform \(G'\) enables retrieval of all \(t\) terminal
vertices of walks in the unaltered \(G\) matching \(q\) in \(O(|q| + t log |V|)\)
time. We conclude by proposing two defining properties of a class of transforms
that includes the Burrows-Wheeler transform and the transform presented here.