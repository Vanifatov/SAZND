<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en"><head>

<meta charset="utf-8">
<meta name="generator" content="quarto-1.2.269">

<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">


<title>prak1</title>
<style>
code{white-space: pre-wrap;}
span.smallcaps{font-variant: small-caps;}
div.columns{display: flex; gap: min(4vw, 1.5em);}
div.column{flex: auto; overflow-x: auto;}
div.hanging-indent{margin-left: 1.5em; text-indent: -1.5em;}
ul.task-list{list-style: none;}
ul.task-list li input[type="checkbox"] {
  width: 0.8em;
  margin: 0 0.8em 0.2em -1.6em;
  vertical-align: middle;
}
pre > code.sourceCode { white-space: pre; position: relative; }
pre > code.sourceCode > span { display: inline-block; line-height: 1.25; }
pre > code.sourceCode > span:empty { height: 1.2em; }
.sourceCode { overflow: visible; }
code.sourceCode > span { color: inherit; text-decoration: inherit; }
div.sourceCode { margin: 1em 0; }
pre.sourceCode { margin: 0; }
@media screen {
div.sourceCode { overflow: auto; }
}
@media print {
pre > code.sourceCode { white-space: pre-wrap; }
pre > code.sourceCode > span { text-indent: -5em; padding-left: 5em; }
}
pre.numberSource code
  { counter-reset: source-line 0; }
pre.numberSource code > span
  { position: relative; left: -4em; counter-increment: source-line; }
pre.numberSource code > span > a:first-child::before
  { content: counter(source-line);
    position: relative; left: -1em; text-align: right; vertical-align: baseline;
    border: none; display: inline-block;
    -webkit-touch-callout: none; -webkit-user-select: none;
    -khtml-user-select: none; -moz-user-select: none;
    -ms-user-select: none; user-select: none;
    padding: 0 4px; width: 4em;
    color: #aaaaaa;
  }
pre.numberSource { margin-left: 3em; border-left: 1px solid #aaaaaa;  padding-left: 4px; }
div.sourceCode
  {   }
@media screen {
pre > code.sourceCode > span > a:first-child::before { text-decoration: underline; }
}
code span.al { color: #ff0000; font-weight: bold; } /* Alert */
code span.an { color: #60a0b0; font-weight: bold; font-style: italic; } /* Annotation */
code span.at { color: #7d9029; } /* Attribute */
code span.bn { color: #40a070; } /* BaseN */
code span.bu { color: #008000; } /* BuiltIn */
code span.cf { color: #007020; font-weight: bold; } /* ControlFlow */
code span.ch { color: #4070a0; } /* Char */
code span.cn { color: #880000; } /* Constant */
code span.co { color: #60a0b0; font-style: italic; } /* Comment */
code span.cv { color: #60a0b0; font-weight: bold; font-style: italic; } /* CommentVar */
code span.do { color: #ba2121; font-style: italic; } /* Documentation */
code span.dt { color: #902000; } /* DataType */
code span.dv { color: #40a070; } /* DecVal */
code span.er { color: #ff0000; font-weight: bold; } /* Error */
code span.ex { } /* Extension */
code span.fl { color: #40a070; } /* Float */
code span.fu { color: #06287e; } /* Function */
code span.im { color: #008000; font-weight: bold; } /* Import */
code span.in { color: #60a0b0; font-weight: bold; font-style: italic; } /* Information */
code span.kw { color: #007020; font-weight: bold; } /* Keyword */
code span.op { color: #666666; } /* Operator */
code span.ot { color: #007020; } /* Other */
code span.pp { color: #bc7a00; } /* Preprocessor */
code span.sc { color: #4070a0; } /* SpecialChar */
code span.ss { color: #bb6688; } /* SpecialString */
code span.st { color: #4070a0; } /* String */
code span.va { color: #19177c; } /* Variable */
code span.vs { color: #4070a0; } /* VerbatimString */
code span.wa { color: #60a0b0; font-weight: bold; font-style: italic; } /* Warning */
</style>


<script src="prak1_files/libs/clipboard/clipboard.min.js"></script>
<script src="prak1_files/libs/quarto-html/quarto.js"></script>
<script src="prak1_files/libs/quarto-html/popper.min.js"></script>
<script src="prak1_files/libs/quarto-html/tippy.umd.min.js"></script>
<script src="prak1_files/libs/quarto-html/anchor.min.js"></script>
<link href="prak1_files/libs/quarto-html/tippy.css" rel="stylesheet">
<link href="prak1_files/libs/quarto-html/quarto-syntax-highlighting.css" rel="stylesheet" id="quarto-text-highlighting-styles">
<script src="prak1_files/libs/bootstrap/bootstrap.min.js"></script>
<link href="prak1_files/libs/bootstrap/bootstrap-icons.css" rel="stylesheet">
<link href="prak1_files/libs/bootstrap/bootstrap.min.css" rel="stylesheet" id="quarto-bootstrap" data-mode="light">


</head>

<body class="fullcontent">

<div id="quarto-content" class="page-columns page-rows-contents page-layout-article">

<main class="content" id="quarto-document-content">



<section id="системы-аутентификациии-и-защиты-от-несанкционированного-доступа" class="level1">
<h1>Системы аутентификациии и защиты от несанкционированного доступа</h1>
<p>Лабораторная работа №1</p>
<section id="цель-работы" class="level2">
<h2 class="anchored" data-anchor-id="цель-работы">Цель работы</h2>
<p>Вывести информацию о процессоре, операционной системе и о последних логах</p>
</section>
<section id="исходные-данные" class="level2">
<h2 class="anchored" data-anchor-id="исходные-данные">Исходные данные</h2>
<ol type="1">
<li>ОС Windows 11</li>
<li>IDE RStudio</li>
<li>Интерпретатор языка R 4.2.2</li>
</ol>
</section>
<section id="план" class="level2">
<h2 class="anchored" data-anchor-id="план">План</h2>
<ol type="1">
<li>Выполнить команду “systeminfo”</li>
<li>Выполнить команду “wmic cpu get name”</li>
<li>Выполнить команду “Get-EventLog -LogName System -Newest 30”</li>
</ol>
</section>
<section id="шаги" class="level2">
<h2 class="anchored" data-anchor-id="шаги">Шаги</h2>
<section id="шаг-1" class="level3">
<h3 class="anchored" data-anchor-id="шаг-1">Шаг 1</h3>
<p>Выполнение команды “systeminfo” для вывода информации об операционной системе</p>
<div class="cell">
<div class="sourceCode cell-code" id="cb1"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">system2</span>(<span class="st">"systeminfo"</span>, <span class="at">stdout =</span> <span class="cn">TRUE</span>)</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
<div class="cell-output cell-output-stdout">
<pre><code> [1] ""                                                                                                               
 [2] "Host Name:                 НОУТБУК"                                                                             
 [3] "OS Name:                   Майкрософт Windows 11 Домашняя для одного языка"                                     
 [4] "OS Version:                10.0.22621 N/A Build 22621"                                                          
 [5] "OS Manufacturer:           Microsoft Corporation"                                                               
 [6] "OS Configuration:          Standalone Workstation"                                                              
 [7] "OS Build Type:             Multiprocessor Free"                                                                 
 [8] "Registered Owner:          Artem_v21"                                                                           
 [9] "Registered Organization:   N/A"                                                                                 
[10] "Product ID:                00327-30780-35272-AAOEM"                                                             
[11] "Original Install Date:     28.01.2023, 0:25:32"                                                                 
[12] "System Boot Time:          14.03.2023, 18:31:29"                                                                
[13] "System Manufacturer:       Dell Inc."                                                                           
[14] "System Model:              G3 3590"                                                                             
[15] "System Type:               x64-based PC"                                                                        
[16] "Processor(s):              1 Processor(s) Installed."                                                           
[17] "                           [01]: Intel64 Family 6 Model 158 Stepping 10 GenuineIntel ~2592 Mhz"                 
[18] "BIOS Version:              Dell Inc. 1.11.1, 19.08.2020"                                                        
[19] "Windows Directory:         C:\\WINDOWS"                                                                         
[20] "System Directory:          C:\\WINDOWS\\system32"                                                               
[21] "Boot Device:               \\Device\\HarddiskVolume3"                                                           
[22] "System Locale:             ru;Russian"                                                                          
[23] "Input Locale:              ru;Russian"                                                                          
[24] "Time Zone:                 (UTC+03:00) Moscow, St. Petersburg"                                                  
[25] "Total Physical Memory:     32&nbsp;578 MB"                                                                           
[26] "Available Physical Memory: 23&nbsp;594 MB"                                                                           
[27] "Virtual Memory: Max Size:  34&nbsp;626 MB"                                                                           
[28] "Virtual Memory: Available: 23&nbsp;730 MB"                                                                           
[29] "Virtual Memory: In Use:    10&nbsp;896 MB"                                                                           
[30] "Page File Location(s):     C:\\pagefile.sys"                                                                    
[31] "Domain:                    WORKGROUP"                                                                           
[32] "Logon Server:              \\\\НОУТБУК"                                                                         
[33] "Hotfix(s):                 4 Hotfix(s) Installed."                                                              
[34] "                           [01]: KB5022497"                                                                     
[35] "                           [02]: KB5012170"                                                                     
[36] "                           [03]: KB5022845"                                                                     
[37] "                           [04]: KB5022610"                                                                     
[38] "Network Card(s):           4 NIC(s) Installed."                                                                 
[39] "                           [01]: LogMeIn Hamachi Virtual Ethernet Adapter"                                      
[40] "                                 Connection Name: Hamachi"                                                      
[41] "                                 Status:          Hardware not present"                                         
[42] "                           [02]: Qualcomm QCA9377 802.11ac Wireless Adapter"                                    
[43] "                                 Connection Name: Беспроводная сеть"                                            
[44] "                                 Status:          Media disconnected"                                           
[45] "                           [03]: Realtek PCIe GbE Family Controller"                                            
[46] "                                 Connection Name: Ethernet"                                                     
[47] "                                 DHCP Enabled:    Yes"                                                          
[48] "                                 DHCP Server:     10.0.30.5"                                                    
[49] "                                 IP address(es)"                                                                
[50] "                                 [01]: 10.11.30.53"                                                             
[51] "                                 [02]: fe80::a01d:1efe:2848:5e56"                                               
[52] "                                 [03]: 2001:b08:14:30:fcb9:dcc5:45d4:c580"                                      
[53] "                                 [04]: 2001:b08:14:30:2a5:f59e:47aa:8817"                                       
[54] "                           [04]: Bluetooth Device (Personal Area Network)"                                      
[55] "                                 Connection Name: Сетевое подключение Bluetooth"                                
[56] "                                 Status:          Media disconnected"                                           
[57] "Hyper-V Requirements:      A hypervisor has been detected. Features required for Hyper-V will not be displayed."</code></pre>
</div>
</div>
</section>
<section id="шаг-2" class="level3">
<h3 class="anchored" data-anchor-id="шаг-2">Шаг 2</h3>
<p>Выполнение команды “wmic cpu get name” для вывода информации о процессоре</p>
<div class="cell">
<div class="sourceCode cell-code" id="cb3"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a><span class="fu">system</span>(<span class="st">"wmic cpu get name"</span>, <span class="at">intern =</span> <span class="cn">TRUE</span>)</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
<div class="cell-output cell-output-stdout">
<pre><code>[1] "Name                                      \r"
[2] "Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz  \r"
[3] "\r"                                          </code></pre>
</div>
</div>
</section>
<section id="шаг-3" class="level3">
<h3 class="anchored" data-anchor-id="шаг-3">Шаг 3</h3>
<p>Выполнение команды “Get-EventLog -LogName System -Newest 30” для получения информации о последних 30 логах системы</p>
<div class="cell">
<div class="sourceCode cell-code" id="cb5"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb5-1"><a href="#cb5-1" aria-hidden="true" tabindex="-1"></a><span class="fu">system2</span>(<span class="st">"powershell"</span>, <span class="at">args  =</span> <span class="st">"Get-EventLog -LogName System -Newest 30"</span>, <span class="at">stdout =</span> <span class="cn">TRUE</span>)</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
<div class="cell-output cell-output-stdout">
<pre><code> [1] ""                                                                                                                       
 [2] "   Index Time          EntryType   Source                 InstanceID Message                                           "
 [3] "   ----- ----          ---------   ------                 ---------- -------                                           "
 [4] "    9731 мар 14 18:44  Information Service Control M...   1073748864 The start type of the Фоновая интеллектуальная ..."
 [5] "    9730 мар 14 18:36  Warning     Microsoft-Windows...         1014 Name resolution for the name cloud.dell.com tim..."
 [6] "    9729 мар 14 18:36  Warning     DCOM                        10016 The description for Event ID '10016' in Source ..."
 [7] "    9728 мар 14 18:35  Warning     DCOM                        10016 The description for Event ID '10016' in Source ..."
 [8] "    9727 мар 14 18:34  Information Microsoft-Windows...          113 Attempted to add URL (http://127.0.0.1:8884:127..."
 [9] "    9726 мар 14 18:34  Information Microsoft-Windows...          111 Create URL group 18158513715274579969. Status 0..."
[10] "    9725 мар 14 18:34  Information HTTP                   1073756831 The description for Event ID '1073756831' in So..."
[11] "    9724 мар 14 18:34  Information Microsoft-Windows...          112 Attempted to reserve URL http://127.0.0.1:8884:..."
[12] "    9723 мар 14 18:34  Information HTTP                   1073756832 The description for Event ID '1073756832' in So..."
[13] "    9722 мар 14 18:34  Information Microsoft-Windows...          112 Attempted to reserve URL http://127.0.0.1:8884:..."
[14] "    9721 мар 14 18:34  Information Microsoft-Windows...          113 Attempted to add URL (http://+:5700/) to URL gr..."
[15] "    9720 мар 14 18:34  Information Microsoft-Windows...          111 Create URL group 18302628903350435841. Status 0..."
[16] "    9719 мар 14 18:34  Information Microsoft-Windows...          119 SSL Certificate Settings deleted for endpoint :..."
[17] "    9718 мар 14 18:34  Warning     DCOM                        10016 The description for Event ID '10016' in Source ..."
[18] "    9717 мар 14 18:34  Warning     DCOM                        10016 The description for Event ID '10016' in Source ..."
[19] "    9716 мар 14 18:33  Information Microsoft-Windows...            5 Secure Trustlet NULL Id 0 and Pid 0 started wit..."
[20] "    9715 мар 14 18:33  Information Service Control M...   1073748869 A service was installed in the system....         "
[21] "    9714 мар 14 18:33  Information Microsoft-Windows...           16 The description for Event ID '16' in Source 'Mi..."
[22] "    9713 мар 14 18:33  Warning     DCOM                        10016 The description for Event ID '10016' in Source ..."
[23] "    9712 мар 14 18:33  Warning     DCOM                        10016 The description for Event ID '10016' in Source ..."
[24] "    9711 мар 14 18:33  Error       Service Control M...   3221232503 The Windows Search service terminated unexpecte..."
[25] "    9710 мар 14 18:33  Error       Service Control M...   3221232495 The Windows Search service terminated with the ..."
[26] "    9709 мар 14 18:33  Error       Service Control M...   3221232503 The Windows Search service terminated unexpecte..."
[27] "    9708 мар 14 18:33  Error       Service Control M...   3221232495 The Windows Search service terminated with the ..."
[28] "    9707 мар 14 18:32  Information Microsoft-Windows...           16 The description for Event ID '16' in Source 'Mi..."
[29] "    9706 мар 14 18:32  Information Microsoft-Windows...           15 The description for Event ID '15' in Source 'Mi..."
[30] "    9705 мар 14 18:32  Information Microsoft-Windows...         7001 User Logon Notification for Customer Experience..."
[31] "    9704 мар 14 18:31  Information Microsoft-Windows...         1025 The TPM was successfully provisioned and is now..."
[32] "    9703 мар 14 18:31  Information Microsoft-Windows...         1282 The TBS device identifier has been generated.     "
[33] "    9702 мар 14 18:31  Information TPM                            18 This event triggers the Trusted Platform Module..."
[34] ""                                                                                                                       
[35] ""                                                                                                                       </code></pre>
</div>
</div>
</section>
</section>
<section id="оценка-результата" class="level2">
<h2 class="anchored" data-anchor-id="оценка-результата">Оценка результата</h2>
<p>В результате лабораторной работы была получена информация о процессоре, об операционной системе и о последних логах</p>
</section>
<section id="вывод" class="level2">
<h2 class="anchored" data-anchor-id="вывод">Вывод</h2>
<p>В результате выполнения работы были получены навыки работы с командами Windows через среду разработки RStudio</p>
</section>
</section>

</main>
<!-- /main column -->
<script id="quarto-html-after-body" type="application/javascript">
window.document.addEventListener("DOMContentLoaded", function (event) {
  const toggleBodyColorMode = (bsSheetEl) => {
    const mode = bsSheetEl.getAttribute("data-mode");
    const bodyEl = window.document.querySelector("body");
    if (mode === "dark") {
      bodyEl.classList.add("quarto-dark");
      bodyEl.classList.remove("quarto-light");
    } else {
      bodyEl.classList.add("quarto-light");
      bodyEl.classList.remove("quarto-dark");
    }
  }
  const toggleBodyColorPrimary = () => {
    const bsSheetEl = window.document.querySelector("link#quarto-bootstrap");
    if (bsSheetEl) {
      toggleBodyColorMode(bsSheetEl);
    }
  }
  toggleBodyColorPrimary();  
  const icon = "";
  const anchorJS = new window.AnchorJS();
  anchorJS.options = {
    placement: 'right',
    icon: icon
  };
  anchorJS.add('.anchored');
  const clipboard = new window.ClipboardJS('.code-copy-button', {
    target: function(trigger) {
      return trigger.previousElementSibling;
    }
  });
  clipboard.on('success', function(e) {
    // button target
    const button = e.trigger;
    // don't keep focus
    button.blur();
    // flash "checked"
    button.classList.add('code-copy-button-checked');
    var currentTitle = button.getAttribute("title");
    button.setAttribute("title", "Copied!");
    let tooltip;
    if (window.bootstrap) {
      button.setAttribute("data-bs-toggle", "tooltip");
      button.setAttribute("data-bs-placement", "left");
      button.setAttribute("data-bs-title", "Copied!");
      tooltip = new bootstrap.Tooltip(button, 
        { trigger: "manual", 
          customClass: "code-copy-button-tooltip",
          offset: [0, -8]});
      tooltip.show();    
    }
    setTimeout(function() {
      if (tooltip) {
        tooltip.hide();
        button.removeAttribute("data-bs-title");
        button.removeAttribute("data-bs-toggle");
        button.removeAttribute("data-bs-placement");
      }
      button.setAttribute("title", currentTitle);
      button.classList.remove('code-copy-button-checked');
    }, 1000);
    // clear code selection
    e.clearSelection();
  });
  function tippyHover(el, contentFn) {
    const config = {
      allowHTML: true,
      content: contentFn,
      maxWidth: 500,
      delay: 100,
      arrow: false,
      appendTo: function(el) {
          return el.parentElement;
      },
      interactive: true,
      interactiveBorder: 10,
      theme: 'quarto',
      placement: 'bottom-start'
    };
    window.tippy(el, config); 
  }
  const noterefs = window.document.querySelectorAll('a[role="doc-noteref"]');
  for (var i=0; i<noterefs.length; i++) {
    const ref = noterefs[i];
    tippyHover(ref, function() {
      // use id or data attribute instead here
      let href = ref.getAttribute('data-footnote-href') || ref.getAttribute('href');
      try { href = new URL(href).hash; } catch {}
      const id = href.replace(/^#\/?/, "");
      const note = window.document.getElementById(id);
      return note.innerHTML;
    });
  }
  const findCites = (el) => {
    const parentEl = el.parentElement;
    if (parentEl) {
      const cites = parentEl.dataset.cites;
      if (cites) {
        return {
          el,
          cites: cites.split(' ')
        };
      } else {
        return findCites(el.parentElement)
      }
    } else {
      return undefined;
    }
  };
  var bibliorefs = window.document.querySelectorAll('a[role="doc-biblioref"]');
  for (var i=0; i<bibliorefs.length; i++) {
    const ref = bibliorefs[i];
    const citeInfo = findCites(ref);
    if (citeInfo) {
      tippyHover(citeInfo.el, function() {
        var popup = window.document.createElement('div');
        citeInfo.cites.forEach(function(cite) {
          var citeDiv = window.document.createElement('div');
          citeDiv.classList.add('hanging-indent');
          citeDiv.classList.add('csl-entry');
          var biblioDiv = window.document.getElementById('ref-' + cite);
          if (biblioDiv) {
            citeDiv.innerHTML = biblioDiv.innerHTML;
          }
          popup.appendChild(citeDiv);
        });
        return popup.innerHTML;
      });
    }
  }
});
</script>
</div> <!-- /content -->



</body></html>