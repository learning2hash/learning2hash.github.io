---
layout: publication
title: Constructing Antidictionaries In Output-sensitive Space
authors: "Lorraine A. K. Ayad, Golnaz Badkobeh, Gabriele Fici, Alice H\xE9liou, Solon\
  \ P. Pissis"
conference: 2019 Data Compression Conference (DCC)
year: 2019
bibkey: ayad2019constructing
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1902.04785'}]
tags: []
short_authors: Ayad et al.
---
A word \(x\) that is absent from a word \(y\) is called minimal if all its proper
factors occur in \(y\). Given a collection of \(k\) words \(y_1,y_2,\ldots,y_k\) over
an alphabet \(\Sigma\), we are asked to compute the set
\(\mathrm\{M\}^\{\ell\}_\{y_\{1\}\#\ldots\#y_\{k\}\}\) of minimal absent words of length at
most \(\ell\) of word \(y=y_1\#y_2\#\ldots\#y_k\), \(\#\notin\Sigma\). In data
compression, this corresponds to computing the antidictionary of \(k\) documents.
In bioinformatics, it corresponds to computing words that are absent from a
genome of \(k\) chromosomes. This computation generally requires \(Ω(n)\)
space for \(n=|y|\) using any of the plenty available \(\mathcal\{O\}(n)\)-time
algorithms. This is because an \(Ω(n)\)-sized text index is constructed over
\(y\) which can be impractical for large \(n\). We do the identical computation
incrementally using output-sensitive space. This goal is reasonable when
\(||\mathrm\{M\}^\{\ell\}_\{y_\{1\}\#\ldots\#y_\{N\}\}||=o(n)\), for all \(N\in[1,k]\). For
instance, in the human genome, \(n \approx 3\times 10^9\) but
\(||\mathrm\{M\}^\{12\}_\{y_\{1\}\#\ldots\#y_\{k\}\}|| \approx 10^6\). We consider a
constant-sized alphabet for stating our results. We show that all
\(\mathrm\{M\}^\{\ell\}_\{y_\{1\}\},\ldots,\mathrm\{M\}^\{\ell\}_\{y_\{1\}\#\ldots\#y_\{k\}\}\) can
be computed in
\(\mathcal\{O\}(kn+\sum^\{k\}_\{N=1\}||\mathrm\{M\}^\{\ell\}_\{y_\{1\}\#\ldots\#y_\{N\}\}||)\)
total time using \(\mathcal\{O\}(\mathrm\{MaxIn\}+\mathrm\{MaxOut\})\) space, where
\(\mathrm\{MaxIn\}\) is the length of the longest word in \(\\{y_1,\ldots,y_\{k\}\\}\)
and
\(\mathrm\{MaxOut\}=\max\\{||\mathrm\{M\}^\{\ell\}_\{y_\{1\}\#\ldots\#y_\{N\}\}||:N\in[1,k]\\}\).
Proof-of-concept experimental results are also provided confirming our
theoretical findings and justifying our contribution.