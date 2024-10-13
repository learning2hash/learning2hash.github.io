---
layout: publication
title: Distortion-resistant Hashing For Rapid Search Of Similar DNA Subsequence
authors: Duda Jarek
conference: "Arxiv"
year: 2016
bibkey: duda2016distortion
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1602.05889"}
tags: ['ARXIV', 'Independent']
---
<p>One of the basic tasks in bioinformatics is localizing a short
subsequence <span class="math inline">\(S\)</span>, read while
sequencing, in a long reference sequence <span
class="math inline">\(R\)</span>, like the human geneome. A natural
rapid approach would be finding a hash value for <span
class="math inline">\(S\)</span> and compare it with a prepared database
of hash values for each of length <span
class="math inline">\(|S|\)</span> subsequences of <span
class="math inline">\(R\)</span>. The problem with such approach is that
it would only spot a perfect match, while in reality there are lots of
small changes: substitutions, deletions and insertions. This issue could
be repaired if having a hash function designed to tolerate some small
distortion accordingly to an alignment metric (like Needleman-Wunch):
designed to make that two similar sequences should most likely give the
same hash value. This paper discusses construction of
Distortion-Resistant Hashing (DRH) to generate such fingerprints for
rapid search of similar subsequences. The proposed approach is based on
the rate distortion theory: in a nearly uniform subset of length <span
class="math inline">\(|S|\)</span> sequences, the hash value represents
the closest sequence to <span class="math inline">\(S\)</span>. This
gives some control of the distance of collisions: sequences having the
same hash value.</p>
