---
layout: publication
title: Document Listing On Repetitive Collections With Guaranteed Performance
authors: Gonzalo Navarro
conference: Theoretical Computer Science
year: 2018
bibkey: navarro2017document
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.06374'}]
tags: ["Evaluation"]
short_authors: Gonzalo Navarro
---
We consider document listing on string collections, that is, finding in which
strings a given pattern appears. In particular, we focus on repetitive
collections: a collection of size \\(N\\) over alphabet \\([1,\sigma]\\) is composed of
\\(D\\) copies of a string of size \\(n\\), and \\(s\\) edits are applied on ranges of
copies. We introduce the first document listing index with size
\\(\tilde\{O\}(n+s)\\), precisely \\(O((nlog\sigma+slog^2 N)log D)\\) bits, and with
useful worst-case time guarantees: Given a pattern of length \\(m\\), the index
reports the \\(\ndoc>0\\) strings where it appears in time \\(O(mlog^\{1+\epsilon\} N
\cdot \ndoc)\\), for any constant \\(\epsilon>0\\) (and tells in time \\(O(mlog N)\\) if
\\(\ndoc=0\\)). Our technique is to augment a range data structure that is commonly
used on grammar-based indexes, so that instead of retrieving all the pattern
occurrences, it computes useful summaries on them. We show that the idea has
independent interest: we introduce the first grammar-based index that, on a
text \\(T[1,N]\\) with a grammar of size \\(r\\), uses \\(O(rlog N)\\) bits and counts the
number of occurrences of a pattern \\(P[1,m]\\) in time \\(O(m^2 + mlog^\{2+\epsilon\}
r)\\), for any constant \\(\epsilon>0\\). We also give the first index using
\\(O(zlog(N/z)log N)\\) bits, where \\(T\\) is parsed by Lempel-Ziv into \\(z\\) phrases,
counting occurrences in time \\(O(mlog^\{2+\epsilon\} N)\\).