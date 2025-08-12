---
layout: publication
title: Fast And Lean Immutable Multi-maps On The JVM Based On Heterogeneous Hash-array
  Mapped Tries
authors: Michael J. Steindorfer, Jurgen J. Vinju
conference: Arxiv
year: 2016
bibkey: steindorfer2016fast
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1608.01036'}]
tags: ["Tools & Libraries"]
short_authors: Michael J. Steindorfer, Jurgen J. Vinju
---
An immutable multi-map is a many-to-many thread-friendly map data structure
with expected fast insert and lookup operations. This data structure is used
for applications processing graphs or many-to-many relations as applied in
static analysis of object-oriented systems. When processing such big data sets
the memory overhead of the data structure encoding itself is a memory usage
bottleneck. Motivated by reuse and type-safety, libraries for Java, Scala and
Clojure typically implement immutable multi-maps by nesting sets as the values
with the keys of a trie map. Like this, based on our measurements the expected
byte overhead for a sparse multi-map per stored entry adds up to around 65B,
which renders it unfeasible to compute with effectively on the JVM.
  In this paper we propose a general framework for Hash-Array Mapped Tries on
the JVM which can store type-heterogeneous keys and values: a Heterogeneous
Hash-Array Mapped Trie (HHAMT). Among other applications, this allows for a
highly efficient multi-map encoding by (a) not reserving space for empty value
sets and (b) inlining the values of singleton sets while maintaining a (c)
type-safe API.
  We detail the necessary encoding and optimizations to mitigate the overhead
of storing and retrieving heterogeneous data in a hash-trie. Furthermore, we
evaluate HHAMT specifically for the application to multi-maps, comparing them
to state-of-the-art encodings of multi-maps in Java, Scala and Clojure. We
isolate key differences using microbenchmarks and validate the resulting
conclusions on a real world case in static analysis. The new encoding brings
the per key-value storage overhead down to 30B: a 2x improvement. With
additional inlining of primitive values it reaches a 4x improvement.