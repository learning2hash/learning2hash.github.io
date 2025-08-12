---
layout: publication
title: Rifflescrambler - A Memory-hard Password Storing Function
authors: Karol Gotfryd, Pawel Lorek, Filip Zagorski
conference: Lecture Notes in Computer Science
year: 2018
bibkey: gotfryd2018rifflescrambler
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1807.06443'}]
tags: ["Efficiency", "Hashing Methods"]
short_authors: Karol Gotfryd, Pawel Lorek, Filip Zagorski
---
We introduce RiffleScrambler: a new family of directed acyclic graphs and a
corresponding data-independent memory hard function with password independent
memory access. We prove its memory hardness in the random oracle model.
  RiffleScrambler is similar to Catena -- updates of hashes are determined by a
graph (bit-reversal or double-butterfly graph in Catena). The advantage of the
RiffleScrambler over Catena is that the underlying graphs are not predefined
but are generated per salt, as in Balloon Hashing. Such an approach leads to
higher immunity against practical parallel attacks. RiffleScrambler offers
better efficiency than Balloon Hashing since the in-degree of the underlying
graph is equal to 3 (and is much smaller than in Ballon Hashing). At the same
time, because the underlying graph is an instance of a Superconcentrator, our
construction achieves the same time-memory trade-offs.