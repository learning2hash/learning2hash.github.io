---
layout: publication
title: Understanding The Moments Of Tabulation Hashing Via Chaoses
authors: "Houen Jakob B\xE6k Tejs, Thorup Mikkel"
conference: Proceedings of the Twenty-Fourth Annual ACM-SIAM Symposium on Discrete
  Algorithms
year: 2022
bibkey: houen2022understanding
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.01453'}]
tags: [Hashing Methods]
---
Simple tabulation hashing dates back to Zobrist in 1970 and is defined as
follows: Each key is viewed as \\(c\\) characters from some alphabet \\(\Sigma\\), we
have \\(c\\) fully random hash functions \\(h_0, \ldots, h_\{c - 1\} \colon \Sigma \to
\\{0, \ldots, 2^l - 1\\}\\), and a key \\(x = (x_0, \ldots, x_\{c - 1\})\\) is hashed to
\\(h(x) = h_0(x_0) \oplus \ldots \oplus h_\{c - 1\}(x_\{c - 1\})\\) where \\(\oplus\\) is
the bitwise XOR operation. The previous results on tabulation hashing by P\{\v
a\}tra\{\c s\}cu and Thorup~[J.ACM'11] and by Aamand et al.~[STOC'20] focused on
proving Chernoff-style tail bounds on hash-based sums, e.g., the number keys
hashing to a given value, for simple tabulation hashing, but their bounds do
not cover the entire tail.
  Chaoses are random variables of the form \\(\sum a_\{i_0, \ldots, i_\{c - 1\}\}
X_\{i_0\} \cdot \ldots \cdot X_\{i_\{c - 1\}\}\\) where \\(X_i\\) are independent random
variables. Chaoses are a well-studied concept from probability theory, and
tight analysis has been proven in several instances, e.g., when the independent
random variables are standard Gaussian variables and when the independent
random variables have logarithmically convex tails. We notice that hash-based
sums of simple tabulation hashing can be seen as a sum of chaoses that are not
independent. This motivates us to use techniques from the theory of chaoses to
analyze hash-based sums of simple tabulation hashing.
  In this paper, we obtain bounds for all the moments of hash-based sums for
simple tabulation hashing which are tight up to constants depending only on
\\(c\\). In contrast with the previous attempts, our approach will mostly be
analytical and does not employ intricate combinatorial arguments. The improved
analysis of simple tabulation hashing allows us to obtain bounds for the
moments of hash-based sums for the mixed tabulation hashing introduced by
Dahlgaard et al.~[FOCS'15].