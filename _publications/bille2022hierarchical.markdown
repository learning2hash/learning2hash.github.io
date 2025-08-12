---
layout: publication
title: Hierarchical Relative Lempel-ziv Compression
authors: "Philip Bille, Inge Li G\xF8rtz, Simon J. Puglisi, Simon R. Tarnow"
conference: Arxiv
year: 2023
bibkey: bille2022hierarchical
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.11371'}]
tags: ["Hashing Methods"]
short_authors: Bille et al.
---
Relative Lempel-Ziv (RLZ) parsing is a dictionary compression method in which
a string \\(S\\) is compressed relative to a second string \\(R\\) (called the
reference) by parsing \\(S\\) into a sequence of substrings that occur in \\(R\\). RLZ
is particularly effective at compressing sets of strings that have a high
degree of similarity to the reference string, such as a set of genomes of
individuals from the same species. With the now cheap cost of DNA sequencing,
such data sets have become extremely abundant and are rapidly growing. In this
paper, instead of using a single reference string for the entire collection, we
investigate the use of different reference strings for subsets of the
collection, with the aim of improving compression. In particular, we form a
rooted tree (or hierarchy) on the strings and then compressed each string using
RLZ with parent as reference, storing only the root of the tree in plain text.
To decompress, we traverse the tree in BFS order starting at the root,
decompressing children with respect to their parent. We show that this approach
leads to a twofold improvement in compression on bacterial genome data sets,
with negligible effect on decompression time compared to the standard single
reference approach. We show that an effective hierarchy for a given set of
strings can be constructed by computing the optimal arborescence of a completed
weighted digraph of the strings, with weights as the number of phrases in the
RLZ parsing of the source and destination vertices. We further show that
instead of computing the complete graph, a sparse graph derived using locality
sensitive hashing can significantly reduce the cost of computing a good
hierarchy, without adversely effecting compression performance.