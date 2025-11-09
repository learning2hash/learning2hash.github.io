---
layout: default
title: Search Open Source Tools
description: A searchable list of open-source Learning to Hash tools
---

<h2 style="font-size: 1.8em; margin-bottom: 10px;">🧰 Open-Source Learning-to-Hash Tools</h2>
<p style="font-size: 1.05em;">
  Explore <strong>open-source repositories</strong> related to Learning to Hash. 
  Use the search bar to <strong>filter</strong> and <strong>sort</strong> by stars, 
  contributors, or recent activity to discover key projects in the field.
</p>

<!-- Slim Toolbar: search + visible count -->
<div id="toolsToolbar" class="toolbar" style="display:none;">
  <div class="left">
    <div class="search">
      <label for="toolsSearch"><strong>Search</strong></label>
      <input id="toolsSearch" type="search" placeholder="🔍 Search repo, category, description…" inputmode="search" />
      <button id="resetToolsSearch" type="button" aria-label="Clear search">Clear</button>
      <span id="toolsVisibleCount" class="small" aria-live="polite"></span>
    </div>
  </div>
</div>

<!-- Loading Indicator -->
<div id="loading" role="status" aria-live="polite">
  <p>Loading Tools Explorer …</p>
</div>

<!-- Cards View (only) -->
<div id="cardsGrid" class="cards" style="display:none;" aria-live="polite"></div>
<p id="emptyState" class="empty" style="display:none;">No tools match your search.</p>

<!-- Hidden Data Table (used as an efficient data engine) -->
<table id="tools-table" class="display stripe hover" style="width:100%; display:none;">
  <thead>
    <tr>
      <th>RepoHTML</th>    <!-- 0 -->
      <th>CategoryHTML</th><!-- 1 -->
      <th>Stars</th>       <!-- 2 -->
      <th>DescHTML</th>    <!-- 3 -->
      <th>cat_raw</th>     <!-- 4 -->
      <th>repo_raw</th>    <!-- 5 -->
      <th>url</th>         <!-- 6 -->
      <th>raw</th>         <!-- 7 -->
    </tr>
  </thead>
  <tbody></tbody>
</table>

<style>
  :root{
    --bg:#ffffff;
    --card:#fff;
    --muted:#6b7280;
    --line:#e5e7eb;
    --shadow:0 1px 2px rgba(0,0,0,.06), 0 8px 24px rgba(0,0,0,.04);
    --brand:#1a73e8;
  }

  .toolbar{
    position:sticky; top:0; z-index:20;
    background: linear-gradient(#fff, rgba(255,255,255,.92));
    backdrop-filter: blur(4px);
    border:1px solid var(--line);
    border-radius:12px; padding:10px 12px; margin:8px 0 12px;
    display:flex; align-items:center; justify-content:flex-start; gap:12px;
    box-shadow: var(--shadow);
  }

  .search{ display:flex; align-items:center; gap:.6rem; flex-wrap:wrap; }
  .search label{ font-weight:700; font-size:.85rem; }
  .search input{
    width:clamp(220px, 32vw, 560px); padding:.45rem .6rem;
    border:1px solid #cbd5e1; border-radius:8px; font-size:.95rem; background-color:#f8fafc;
  }
  .search input:focus{ outline:none; border-color:var(--brand); box-shadow:0 0 0 2px rgba(26,115,232,.18); }
  .search button{
    padding:.45rem .6rem; font-size:.85rem; border:1px solid #cbd5e1; border-radius:8px; background:#f8fafc; cursor:pointer;
  }
  .search button:hover{ background:#eef2f7; }
  .small{ color:var(--muted); font-size:.9em; }

  .cards{
    display:grid; gap:14px;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  }
  .card{
    border:1px solid var(--line); border-radius:14px; background:var(--card);
    padding:14px; box-shadow: var(--shadow); transition: transform .06s ease;
  }
  .card:hover{ transform: translateY(-1px); }
  .meta{ display:flex; align-items:center; gap:10px; margin-bottom:8px; color:var(--muted); font-size:.9rem; }
  .stars{ font-variant-numeric: tabular-nums; }
  .title{ font-weight:700; line-height:1.25; margin:0 0 6px; }
  .title a{ text-decoration:none; color:#0f172a; }
  .title a:hover{ text-decoration:underline; }
  .desc{ color:#374151; font-size:.95rem; line-height:1.45; display:-webkit-box; -webkit-box-orient:vertical; -webkit-line-clamp:4; overflow:hidden; }
  .badges{ display:flex; align-items:center; gap:6px; margin-top:10px; flex-wrap:wrap; }
  .badge{
    font-size:.75rem; border:1px solid var(--line); color:#0f172a; padding:.2rem .45rem; border-radius:999px; background:#f7f7fb;
  }

  .empty{ color:var(--muted); text-align:center; padding:24px 8px; }

  .dataTables_wrapper{ width:100%; overflow-x:hidden; }
  #tools-table{ width:100%; border-collapse:collapse; table-layout:auto; }
  #tools-table td{ white-space: normal !important; word-break: break-word; overflow-wrap:anywhere; vertical-align: top; }
  #tools-table th{ white-space: nowrap !important; overflow: hidden; text-overflow: ellipsis; vertical-align: middle; }
  .dataTables_filter{ display:none !important; }

  #loading{
    position:fixed; top:50%; left:50%; transform:translate(-50%,-50%);
    font-size:1.05em; text-align:center; z-index:1000;
    background:white; padding:.8em 1.2em; border:1px solid #ccc; border-radius:8px;
    box-shadow:0 2px 10px rgba(0,0,0,.08);
  }

  @media (max-width: 640px){
    .toolbar{ border-radius:10px; }
    .desc{ -webkit-line-clamp: 6; }
  }
</style>

<link rel="stylesheet" href="{{ '/assets/vendor/datatables-1.13.6.min.css' | relative_url }}">
<link rel="stylesheet" href="{{ '/assets/vendor/dataTables.responsive-2.5.0.min.css' | relative_url }}">
<script src="{{ '/assets/vendor/jquery-3.6.0.min.js' | relative_url }}" defer></script>
<script src="{{ '/assets/vendor/datatables-1.13.6.min.js' | relative_url }}" defer></script>
<script src="{{ '/assets/vendor/dataTables.responsive-2.5.0.min.js' | relative_url }}" defer></script>
<script src="{{ '/assets/vendor/d3.v7.min.js' | relative_url }}" defer></script>

<script>
(function(){
  // ---- Hash deep-link helpers (/#query) ----
  function readHashQuery(){
    const raw = window.location.hash ? window.location.hash.slice(1) : '';
    if (!raw) return '';
    try { return decodeURIComponent(raw.replace(/\+/g,' ')); } catch { return raw; }
  }
  function setHash(q){
    if (q && q.trim().length) history.replaceState(null, '', '#' + encodeURIComponent(q.trim()));
    else history.replaceState(null, '', location.pathname + location.search);
  }

  // ---- Utilities ----
  function escapeHtml(s){
    return String(s)
      .replace(/&/g,'&amp;').replace(/</g,'&lt;')
      .replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;');
  }
  function kFormat(n){
    if (!n && n !== 0) return '';
    const x = +n || 0;
    if (x < 1000) return String(x);
    if (x < 1e6) return (x/1e3).toFixed(x % 1000 === 0 ? 0 : 1) + 'k';
    return (x/1e6).toFixed(x % 1e6 === 0 ? 0 : 1) + 'M';
  }
  function debounce(fn, ms=120){ let t; return (...a)=>{ clearTimeout(t); t=setTimeout(()=>fn(...a), ms); }; }

  // ---- DOM refs ----
  const loadingEl = document.getElementById('loading');
  const toolbarEl = document.getElementById('toolsToolbar');
  const inputEl   = document.getElementById('toolsSearch');
  const resetEl   = document.getElementById('resetToolsSearch');
  const countEl   = document.getElementById('toolsVisibleCount');
  const gridEl    = document.getElementById('cardsGrid');
  const emptyEl   = document.getElementById('emptyState');

  let datatable;

  function updateVisibleCount(){
    if (!datatable || !countEl) return;
    countEl.textContent = datatable.rows({ filter:'applied' }).count() + ' repos';
  }

  function renderCards(){
    if (!datatable) return;
    const rows = datatable.rows({ filter:'applied' }).data().toArray();
    gridEl.innerHTML = '';

    if (!rows.length){
      gridEl.style.display='none';
      emptyEl.style.display='';
      updateVisibleCount();
      return;
    }
    emptyEl.style.display='none';
    gridEl.style.display='grid';

    rows.forEach(r => {
      const repoHTML   = r[0];
      const catHTML    = r[1];
      const stars      = +r[2] || 0;
      const descHTML   = r[3];
      const url        = r[6] || '';

      const card = document.createElement('article');
      card.className = 'card';
      card.innerHTML = `
        <div class="meta">
          <span class="stars" title="GitHub Stars">★ ${kFormat(stars)}</span>
        </div>
        <h3 class="title">${repoHTML}</h3>
        <div class="desc">${descHTML}</div>
        <div class="badges">
          ${catHTML}
        </div>
      `;

      // Ensure clickable title if not already linked
      if (url){
        const a = card.querySelector('.title a');
        if (!a){
          const h3 = card.querySelector('.title');
          h3.innerHTML = `<a href="${url}" target="_blank" rel="noopener">${escapeHtml(h3.textContent)}</a>`;
        }
      }

      gridEl.appendChild(card);
    });

    updateVisibleCount();
  }

  async function start(){
    try{
      if (!window.jQuery || !jQuery.fn || !jQuery.fn.dataTable) {
        if (loadingEl) loadingEl.innerHTML = '<p style="color:#b00020">Failed to load: DataTables missing.</p>';
        return;
      }
      if (!window.d3 || !d3.csv) {
        if (loadingEl) loadingEl.innerHTML = '<p style="color:#b00020">Failed to load: D3 missing.</p>';
        return;
      }

      const initialQuery = readHashQuery();
      if (inputEl && initialQuery) inputEl.value = initialQuery;

      // If you maintain a dedicated CSV for hashing tools, change this path:
      const CSV_URL = "{{ '/github_topics.csv' | relative_url }}";

      const data = await d3.csv(CSV_URL);

      const rows = data.map(tool => {
        const repo = (tool.repo || '').trim();               // owner/name
        const url  = repo ? ('https://github.com/' + repo) : '';
        const descFull  = (tool.description || '').trim();
        const descShort = descFull.length > 400 ? (descFull.substring(0,400) + '…') : descFull;
        const starsNum  = tool.stars ? +tool.stars : 0;
        const category  = (tool.category || '').trim() || 'Uncategorized';

        const titleHTML = url
          ? `<a href="${url}" target="_blank" rel="noopener noreferrer">${escapeHtml(repo || '(unknown)')}</a>`
          : escapeHtml(repo || '(unknown)');

        const catChip  = `<span class="badge" title="${escapeHtml(category)}">${escapeHtml(category)}</span>`;
        const descHTML = `<div class="desc" title="${escapeHtml(descFull)}">${escapeHtml(descShort)}</div>`;

        const raw = [
          repo, category, descFull,
          (tool.all_tags || ''), (tool.top_devs || ''), (tool.contributors || '')
        ].join(' ').toLowerCase();

        return [
          titleHTML,  // 0
          catChip,    // 1
          starsNum,   // 2
          descHTML,   // 3
          category,   // 4
          repo,       // 5
          url,        // 6
          raw         // 7
        ];
      });

      const dt = jQuery('#tools-table').DataTable({
        data: rows,
        columns: [
          { title: "Repo" },
          { title: "Category" },
          { title: "Stars" },
          { title: "Description" },
          { title: "cat_raw" },
          { title: "repo_raw" },
          { title: "url" },
          { title: "raw" }
        ],
        responsive: { details: false },
        autoWidth: false,
        paging: false,
        searching: true,
        order: [[2, 'desc']],
        columnDefs: [
          { targets: [4,5,6,7], visible: false, searchable: false },
          { targets: 2, type: 'num' }
        ],
        initComplete: function(){
          datatable = this.api();

          // Show UI
          if (loadingEl) loadingEl.style.display='none';
          toolbarEl.style.display='';
          gridEl.style.display='grid';

          // Initial filter from hash
          if (initialQuery) datatable.search(initialQuery).draw();

          // First paint
          renderCards();

          // Re-render cards when filter changes
          datatable.on('draw', renderCards);

          // Search wiring + deep-link hash
          const apply = debounce(() => {
            const q = inputEl ? (inputEl.value || '') : '';
            datatable.search(q).draw(false);
            setHash(q);
          }, 120);

          inputEl.addEventListener('input', apply);
          inputEl.addEventListener('keydown', (e) => { if (e.key === 'Enter'){ e.preventDefault(); apply(); } });

          resetEl.addEventListener('click', () => {
            inputEl.value='';
            datatable.search('').draw(false);
            setHash('');
            inputEl.focus();
          });

          window.addEventListener('hashchange', () => {
            const q = readHashQuery();
            inputEl.value = q;
            datatable.search(q).draw(false);
          });

          // Keyboard shortcuts
          document.addEventListener('keydown', (e) => {
            if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
              e.preventDefault(); inputEl.focus();
            } else if (e.key === 'Escape') {
              inputEl.value=''; datatable.search('').draw(false); setHash('');
            }
          });

          // Adjust after first paint
          setTimeout(() => datatable.columns.adjust().draw(false), 60);
          updateVisibleCount();
        }
      });

    } catch (err){
      console.error(err);
      if (loadingEl) loadingEl.innerHTML = '<p style="color:#b00020">Failed to load tools.</p>';
    }
  }

  if (document.readyState === 'loading'){
    document.addEventListener('DOMContentLoaded', start, { once:true });
  } else {
    start();
  }
})();
</script>
