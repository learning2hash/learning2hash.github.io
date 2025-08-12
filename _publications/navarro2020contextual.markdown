---
layout: publication
title: Contextual Pattern Matching
authors: Gonzalo Navarro
conference: Lecture Notes in Computer Science
year: 2020
bibkey: navarro2020contextual
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.07076'}]
tags: []
short_authors: Gonzalo Navarro
---
The research on indexing repetitive string collections has focused on the
same search problems used for regular string collections, though they can make
little sense in this scenario. For example, the basic pattern matching query
"list all the positions where pattern \(P\) appears" can produce huge outputs
when \(P\) appears in an area shared by many documents. All those occurrences are
essentially the same.
  In this paper we propose a new query that can be more appropriate in these
collections, which we call \{\em contextual pattern matching\}. The basic query
of this type gives, in addition to \(P\), a context length \(\ell\), and asks to
report the occurrences of all \{\em distinct\} strings \(XPY\), with
\(|X|=|Y|=\ell\).
  While this query is easily solved in optimal time and linear space, we focus
on using space related to the repetitiveness of the text collection and present
the first solution of this kind. Letting \(\ovr\) be the maximum of the number of
runs in the BWT of the text \(T[1..n]\) and of its reverse, our structure uses
\(O(\ovrlog(n/\ovr))\) space and finds the \(c\) contextual occurrences \(XPY\) of
\((P,\ell)\) in time \(O(|P| + c log n)\). We give other space/time tradeoffs as
well, for compressed and uncompressed indexes.