---
layout: publication
title: Compactness Of Hashing Modes And Efficiency Beyond Merkle Tree
authors: Andreeva Elena, Bhattacharyya Rishiraj, Roy Arnab
conference: "Arxiv"
year: 2021
bibkey: andreeva2021compactness
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2104.15055"}
tags: ['ARXIV', 'Graph', 'Independent']
---
<p>We revisit the classical problem of designing optimally efficient
cryptographically secure hash functions. Hash functions are
traditionally designed via applying modes of operation on primitives
with smaller domains. The results of Shrimpton and Stam (ICALP 2008),
Rogaway and Steinberger (CRYPTO 2008), and Mennink and Preneel (CRYPTO
2012) show how to achieve optimally efficient designs of <span
class="math inline">\(2n\)</span>-to-<span
class="math inline">\(n\)</span>-bit compression functions from
non-compressing primitives with asymptotically optimal <span
class="math inline">\(2^{n/2-\epsilon}\)</span>-query collision
resistance. Designing optimally efficient and secure hash functions for
larger domains (<span class="math inline">\(&gt; 2n\)</span> bits) is
still an open problem. In this work we propose the new efficiency
notion. It allows us to focus on asymptotically optimally collision
resistant hash function and normalize their parameters based on Stam’s
bound from CRYPTO 2008 to obtain maximal efficiency. We then present two
tree-based modes of operation -Our first construction is an ugmented
inary Tee (ABR) mode. The design is a <span
class="math inline">\((2^{\ell}+2^{\ell-1}
-1)n\)</span>-to-<span class="math inline">\(n\)</span>-bit hash
function making a total of <span
class="math inline">\((2^{\ell}-1)\)</span> calls to <span
class="math inline">\(2n\)</span>-to-<span
class="math inline">\(n\)</span>-bit compression functions for any <span
class="math inline">\(\ell\geq 2\)</span>. Our construction is optimally
compact with asymptotically (optimal) <span
class="math inline">\(2^{n/2-\epsilon}\)</span>-query collision
resistance in the ideal model. For a tree of height <span
class="math inline">\(\ell\)</span>, in comparison with Merkle tree, the
<span class="math inline">\(ABR\)</span> mode processes additional <span
class="math inline">\((2^{\ell-1}-1)\)</span> data blocks making the
same number of internal compression function calls. -While the <span
class="math inline">\(ABR\)</span> mode achieves collision resistance,
it fails to achieve indifferentiability from a random oracle within
<span class="math inline">\(2^{n/3}\)</span> queries. <span
class="math inline">\(ABR^{+}\)</span> compresses only <span
class="math inline">\(1\)</span> less data block than <span
class="math inline">\(ABR\)</span> with the same number of compression
calls and achieves in addition indifferentiability up to <span
class="math inline">\(2^{n/2-\epsilon}\)</span> queries.</p>
