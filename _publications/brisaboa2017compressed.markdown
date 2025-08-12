---
layout: publication
title: Compressed Representation Of Dynamic Binary Relations With Applications
authors: Nieves R. Brisaboa, Ana Cerdeira-Pena, Guillermo de Bernardo, Gonzalo Navarro
conference: Information Systems
year: 2017
bibkey: brisaboa2017compressed
citations: 23
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.02769'}]
tags: ["Compact Codes", "Efficiency"]
short_authors: Brisaboa et al.
---
We introduce a dynamic data structure for the compact representation of
binary relations \(\mathcal\{R\} \subseteq A \times B\). The data structure is a
dynamic variant of the k\(^2\)-tree, a static compact representation that takes
advantage of clustering in the binary relation to achieve compression. Our
structure can efficiently check whether two objects \((a,b) \in A \times B\) are
related, and list the objects of \(B\) related to some \(a \in A\) and vice versa.
Additionally, our structure allows inserting and deleting pairs \((a,b)\) in the
relation, as well as modifying the base sets \(A\) and \(B\). We test our dynamic
data structure in different contexts, including the representation of Web
graphs and RDF databases. Our experiments show that our dynamic data structure
achieves good compression ratios and fast query times, close to those of a
static representation, while also providing efficient support for updates in
the represented binary relation.