---
layout: default
title: Search Open Source Learning to Hash Tools
description: A searchable list of open-source Learning to Hash tools
---

<h2 style="font-size: 1.8em; margin-bottom: 10px;">🧰 Open Source Learning to Hash Tools</h2>
<p style="font-size: 1.05em;">
  Search, filter, and sort to find relevant repositories.
</p>

<!-- Loading Indicator -->
<div id="loading" role="status" aria-live="polite">
  <p>Loading Open Source Learning to Hash Tools ...</p>
</div>

<!-- Styled search bar -->
<div class="controls" id="toolsControls" style="display:none;">
  <div class="search">
    <label for="toolsSearch"><strong>Search</strong></label>
    <input id="toolsSearch" type="search" placeholder="🔍 Search repo, tags, description…" inputmode="search" />
    <button id="resetToolsSearch" type="button" aria-label="Clear search">Clear</button>
    <span id="toolsVisibleCount" class="small" aria-live="polite"></span>
  </div>
</div>

<!-- Tag Cloud / Filter -->
<div id="tagFilter" aria-label="Filter by Tag" style="display:none;"></div>

<!-- Data Table -->
<table id="tools-table" class="display stripe hover" style="width:100%; display:none;">
  <thead>
    <tr>
      <th data-priority="1">Repo</th>
      <th data-priority="3">Tags</th>
      <th data-priority="2">Stars</th>
      <th data-priority="1">Description</th>
    </tr>
  </thead>
  <tbody></tbody>
</table>

<style>
  .dataTables_wrapper{ width:100%; overflow-x:hidden; }
  #loading{
    position:fixed; top:50%; left:50%; transform:translate(-50%,-50%);
    font-size:1.05em; text-align:center; z-index:1000;
    background:white; padding:.8em 1.2em; border:1px solid #ccc; border-radius:8px;
    box-shadow:0 2px 10px rgba(0,0,0,.08);
  }

  #tools-table{
    display:none;
    width:100%;
    border-collapse:collapse;
    table-layout:fixed;
  }

  /* Column widths (4 columns now) */
  #tools-table th:nth-child(1), #tools-table td:nth-child(1){ width:26%; } /* Repo */
  #tools-table th:nth-child(2), #tools-table td:nth-child(2){ width:24%; } /* Tags */
  #tools-table th:nth-child(3), #tools-table td:nth-child(3){ width:10%; } /* Stars */
  #tools-table th:nth-child(4), #tools-table td:nth-child(4){ width:40%; } /* Description */

  #tools-table th:not(:nth-child(4)), #tools-table td:not(:nth-child(4)){
    white-space:nowrap; vertical-align:top; overflow:hidden; text-overflow:ellipsis;
  }

  /* Make Description a single-column block and clamp lines */
  #tools-table td:nth-child(4){
    white-space:normal;
    line-height:1.35;
    display:-webkit-box;
    -webkit-box-orient:vertical;
    -webkit-line-clamp:3;
    overflow:hidden;

    /* prevent accidental multi-column layout from any global CSS */
    -webkit-column-count:1; column-count:1;
    -webkit-column-gap:normal; column-gap:normal;
    -webkit-column-rule:initial; column-rule:initial;
  }

  #tools-table th:nth-child(3), #tools-table td:nth-child(3){ text-align:right; }

  .controls{ display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:.6rem; margin:.6rem 0 .9rem; }
  .search{ display:flex; align-items:flex-start; gap:.6rem; flex-wrap:wrap; }
  .search label{ font-weight:700; font-size:.85rem; }
  .search input{ width:clamp(160px, 32vw, 520px); padding:.4rem .5rem; border:1px solid #aaa; border-radius:6px; font-size:.9rem; background-color:#f8f9fa; }
  .search input:focus{ outline:none; border-color:#0c5fce; box-shadow:0 0 0 2px rgba(26,115,232,.25); }
  .search button{ padding:.4rem .6rem; font-size:.85rem; border:1px solid #aaa; border-radius:6px; background:#f8f9fa; cursor:pointer; }
  .search button:hover{ background:#ececec; }
  .small{ color:#6b7280; font-size:.9em; }

  .dataTables_filter{ display:none !important; }

  /* Tag filter bar */
  #tagFilter{ margin:1rem 0 .75rem; display:flex; flex-wrap:wrap; gap:.5rem .75rem; max-width:100%; box-sizing:border-box; }
  .tag-chip{
    text-decoration:none; border-radius:999px; padding:.2rem .6rem; background:#f6f7f9; border:1px solid #e6e8ec;
    display:inline-flex; align-items:center; gap:.35rem;
    font-size:.78rem;
    line-height:1.05; cursor:pointer; user-select:none; color:inherit; font-weight:500;
  }
  .tag-chip .count{ font-size:.72rem; opacity:.8; font-variant-numeric:tabular-nums; }
  .tag-chip:hover{ background:#f0f3f7; }
  .tag-chip.active{ background:#eef3ff; border-color:#b7ccff; box-shadow:0 0 0 1px #dbe7ff inset; font-weight:600; }

  /* Smaller tags inside the table */
  .tags-display .tag-chip{
    font-size:.70rem;
    padding:.15rem .45rem;
    gap:.25rem;
    line-height:1.0;
  }
  @media (max-width: 640px){
    .tags-display .tag-chip{
      font-size:.66rem;
      padding:.12rem .40rem;
    }
  }

  table.dataTable th.dt-nowrap, table.dataTable td.dt-nowrap { white-space:nowrap; }

  @media (max-width: 1024px){ #tools-table td:nth-child(4){ -webkit-line-clamp:4; } }
  @media (max-width: 640px){
    .search input{ width:clamp(170px, 60vw, 85vw); }
    #tools-table td:nth-child(4){ -webkit-line-clamp:6; }
    #tools-table td:nth-child(1) a{ word-break:break-word; }
  }
</style>

<!-- Dependencies -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
<link rel="stylesheet" href="https://cdn.datatables.net/1.13.6/css/jquery.dataTables.min.css" />
<script src="https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js"></script>
<link rel="stylesheet" href="https://cdn.datatables.net/responsive/2.5.0/css/responsive.dataTables.min.css" />
<script src="https://cdn.datatables.net/responsive/2.5.0/js/dataTables.responsive.min.js"></script>
<script src="https://d3js.org/d3.v7.min.js"></script>

<script>
  var datatable;
  var searchInitialized = false;
  var ACTIVE_TAG = null;

  function normTag(t){ return (t || '').trim(); }

  function parseAllTags(s){
    if (!s) return [];
    return s.split(/[,;|]/).map(normTag).filter(Boolean);
  }

  function updateVisibleCount(){
    if (!datatable) return;
    const el = document.getElementById('toolsVisibleCount');
    if (el) el.textContent = datatable.rows({ filter: 'applied' }).count() + ' rows';
  }

  function applyHash() {
    if (!datatable || !searchInitialized) return;
    const raw = decodeURIComponent((window.location.hash || '').replace(/^#/, ''));
    const tagMatch = raw.match(/^tag=(.+)$/i);

    if (tagMatch && tagMatch[1]) {
      const want = tagMatch[1];
      const chip = Array.from(document.querySelectorAll('#tagFilter .tag-chip'))
        .find(el => (el.dataset.tag || '') === want);
      if (chip) chip.click();
      return;
    }
    datatable.columns().search('');
    datatable.search(raw).draw();
    updateVisibleCount();
  }

  function buildTagFilter(fromData) {
    const counts = {};
    let total = 0;

    fromData.forEach(d => {
      const tags = parseAllTags(d.all_tags || d.subcat || d.category || '');
      if (tags.length === 0) { total += 1; counts['Uncategorized'] = (counts['Uncategorized'] || 0) + 1; return; }
      total += 1;
      tags.forEach(t => { counts[t] = (counts[t] || 0) + 1; });
    });

    const entries = Object.entries(counts).sort((a,b) => b[1] - a[1]);
    const bar = document.getElementById('tagFilter');
    bar.innerHTML = '';

    const allChip = document.createElement('span');
    allChip.className = 'tag-chip active';
    allChip.dataset.tag = '';
    allChip.role = 'button';
    allChip.tabIndex = 0;
    allChip.setAttribute('aria-pressed', 'true');
    allChip.innerHTML = `All <span class="count">(${total})</span>`;
    bar.appendChild(allChip);

    entries.forEach(([tag, cnt]) => {
      const chip = document.createElement('span');
      chip.className = 'tag-chip';
      chip.dataset.tag = tag === 'Uncategorized' ? '' : tag;
      chip.role = 'button';
      chip.tabIndex = 0;
      chip.setAttribute('aria-pressed', 'false');
      chip.innerHTML = `${tag} <span class="count">(${cnt})</span>`;
      bar.appendChild(chip);
    });

    function activateChip(chip){
      const tag = chip.dataset.tag;
      ACTIVE_TAG = (tag === '') ? null : String(tag);

      bar.querySelectorAll('.tag-chip').forEach(el => {
        el.classList.remove('active'); el.setAttribute('aria-pressed','false');
      });
      chip.classList.add('active'); chip.setAttribute('aria-pressed','true');

      if (window.toolsSearchInput) window.toolsSearchInput.value = '';

      datatable.search('');
      datatable.columns().search('');

      if (ACTIVE_TAG === null) {
        datatable.draw();
        history.replaceState(null, '', location.pathname + location.search);
      } else {
        datatable.draw();
        location.hash = 'tag=' + encodeURIComponent(ACTIVE_TAG);
      }
      updateVisibleCount();
    }

    bar.addEventListener('click', e => {
      const chip = e.target.closest('.tag-chip');
      if (chip) activateChip(chip);
    });

    bar.style.display = '';
  }

  // External search bar wiring
  let toolsSearchInput, toolsResetBtn, toolsVisibleCount;
  function initToolsSearchBar(){
    toolsSearchInput = document.getElementById('toolsSearch');
    toolsResetBtn = document.getElementById('resetToolsSearch');
    toolsVisibleCount = document.getElementById('toolsVisibleCount');

    function doSearch(){
      if (!datatable) return;
      const q = (toolsSearchInput.value || '').trim();

      if (q) {
        const bar = document.getElementById('tagFilter');
        const all = bar && (bar.querySelector('.tag-chip[data-tag=""]') || bar.querySelector('.tag-chip'));
        if (all && !all.classList.contains('active')) all.click();
        history.replaceState(null, '', location.pathname + location.search);
      }

      datatable.search(q).draw();
      updateVisibleCount();
    }

    toolsSearchInput.addEventListener('input', doSearch);
    toolsResetBtn.addEventListener('click', () => {
      toolsSearchInput.value=''; datatable.search('').draw(); updateVisibleCount(); toolsSearchInput.focus();
    });

    document.addEventListener('keydown', (e) => {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') { e.preventDefault(); toolsSearchInput.focus(); }
      else if (e.key === 'Escape') { toolsSearchInput.value=''; datatable.search('').draw(); updateVisibleCount(); }
    });

    document.getElementById('toolsControls').style.display = '';
    updateVisibleCount();
  }

  // Tag filter hook
  $.fn.dataTable.ext.search.push(function(settings, data, dataIndex) {
    if (!datatable || !ACTIVE_TAG) return true;
    const node = datatable.row(dataIndex).node();
    const holder = node && node.querySelector('.tags-display');
    const raw = holder ? (holder.dataset.rawtags || '') : '';
    const tokens = raw.split('|').map(normTag).filter(Boolean);
    return tokens.map(t => t.toLowerCase()).includes(ACTIVE_TAG.toLowerCase());
  });

  $(document).ready(function () {
    $('#loading').show();

    d3.csv("github_topics.csv").then(function (data) {
      const rows = data.map(function (tool) {
        const github = (tool.repo || "").trim();
        const repo_url = "https://github.com/" + github;
        const desc_full = (tool.description || "").trim();
        const desc_short = desc_full.length > 400 ? (desc_full.substring(0, 400) + "…") : desc_full;
        const starsNum = tool.stars ? +tool.stars : 0;

        // Prefer all_tags; fallback to subcat/category
        const tags = parseAllTags(tool.all_tags || tool.subcat || tool.category || '');
        const tagsJoined = tags.join('|');

        // Single wrapper with data-rawtags
        const chips = `<span class="tags-display" data-rawtags="${tagsJoined.replace(/"/g,'&quot;')}">
          ${tags.length
            ? tags.slice(0, 12).map(t => `<span class="tag-chip" tabindex="-1" aria-hidden="true">${t}</span>`).join(' ')
            : `<span class="tag-chip" tabindex="-1" aria-hidden="true">Uncategorized</span>`}
        </span>`;

        const escapedTitle = desc_full.replace(/"/g,'&quot;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
        const descCell = `<span title="${escapedTitle}">${desc_short}</span>`;

        return [
          `<a href="${repo_url}" target="_blank" rel="noopener noreferrer">${github}</a>`, // Repo
          chips,                                                                            // Tags
          starsNum,                                                                         // Stars
          descCell                                                                          // Description
        ];
      });

      const dt = $('#tools-table').DataTable({
        data: rows,
        columns: [
          { title: "Repo", className: 'dt-nowrap' },
          { title: "Tags" },
          { title: "Stars", className: 'dt-nowrap' },
          { title: "Description" }
        ],
        responsive: { details: { type: 'inline' } },
        autoWidth: false,
        paging: false,
        searching: true,
        order: [[2, 'desc']],
        columnDefs: [
          { targets: 2, type: 'num' },
          { responsivePriority: 1, targets: 0 },
          { responsivePriority: 2, targets: 2 },
          { responsivePriority: 3, targets: 3 },
          { responsivePriority: 4, targets: 1 }
        ],
        initComplete: function () {
          datatable = this.api();

          $('#loading').hide();
          $('#tools-table').show();
          searchInitialized = true;

          buildTagFilter(data);
          initToolsSearchBar();
          applyHash();

          datatable.on('draw', updateVisibleCount);
          updateVisibleCount();
        }
      });

    }).catch(function (error) {
      console.error("Error loading github_topics.csv:", error);
      $('#tools-table').after(`<div style="color:red; margin-top:10px;">Failed to load data.</div>`);
      $('#loading').hide();
    });
  });

  $(window).on('hashchange', function () { applyHash(); });
</script>
