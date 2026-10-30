// Apply contact details from js/config.js to every page
(function(){
  var C=window.SITE_CONFIG; if(!C) return;
  var q=function(s,f){document.querySelectorAll(s).forEach(f);};
  q('[data-c=tel]',function(a){a.href='tel:+'+C.phone;});
  q('[data-c=phone-text]',function(e){e.textContent=C.phoneDisplay;});
  q('[data-c=mail]',function(a){a.href='mailto:'+C.email;});
  q('[data-c=email-text]',function(e){e.textContent=C.email;});
  q('[data-c=fb]',function(a){a.href=C.facebook;});
  q('a[href*="wa.me/"]',function(a){a.href=a.href.replace(/wa\.me\/\d+/,'wa.me/'+C.phone);});
  // Logo / footer / copyright name (single place: brandName in config.js)
  if(C.brandName){
    var acc=C.brandAccent||'';
    q('[data-c=logo]',function(a){
      a.textContent='';
      var i=acc?C.brandName.indexOf(acc):-1;
      if(i<0){a.textContent=C.brandName;return;}
      a.appendChild(document.createTextNode(C.brandName.slice(0,i)));
      var sp=document.createElement('span');sp.textContent=acc;a.appendChild(sp);
      a.appendChild(document.createTextNode(C.brandName.slice(i+acc.length)));
    });
    q('[data-c=brand]',function(e){e.textContent=C.brandName;});
  }
  q('input[name=access_key]',function(i){i.value=C.web3formsKey;});
  // header height -> body offset (fixed header)
  var h=document.querySelector('.site-header');
  function setH(){if(h)document.documentElement.style.setProperty('--hdr-h',h.offsetHeight+'px');}
  setH();window.addEventListener('resize',setH);window.addEventListener('load',setH);
})();

// Mobile menu
var t=document.getElementById('menuToggle'),m=document.getElementById('navMenu');
if(t&&m){
  t.addEventListener('click',function(){var o=m.classList.toggle('show');t.setAttribute('aria-expanded',o);});
  m.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){m.classList.remove('show');t.setAttribute('aria-expanded','false');});});
}

// Web3Forms submit -> thank-you page
document.querySelectorAll('form.js-form').forEach(function(f){
  f.addEventListener('submit',function(e){
    e.preventDefault();
    var C=window.SITE_CONFIG||{};
    var useSheet=f.hasAttribute('data-testi-form')&&C.testimonialsApi;
    var s=f.querySelector('.form-status'),b=f.querySelector('button[type=submit]'),old=b.textContent;
    s.className='form-status';s.textContent='Sending...';b.disabled=true;b.textContent='Sending...';
    if(useSheet){
      // Student feedback -> Google Sheet (via Apps Script); shows on site after approval
      var body=new URLSearchParams(new FormData(f));
      fetch(C.testimonialsApi,{method:'POST',mode:'no-cors',body:body})
        .then(function(){window.location.href=f.dataset.redirect||'thank-you.html';})
        .catch(function(){
          s.className='form-status err';s.textContent='Could not send. Please try again in a moment.';
          b.disabled=false;b.textContent=old;
        });
      return;
    }
    fetch(f.action,{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify(Object.fromEntries(new FormData(f)))})
    .then(function(r){return r.json();})
    .then(function(d){
      if(d.success){window.location.href=f.dataset.redirect||'thank-you.html';}
      else{throw new Error(d.message||'Error');}
    })
    .catch(function(){
      s.className='form-status err';
      s.innerHTML='Could not send. Please try again or message us on <a href="https://wa.me/'+((window.SITE_CONFIG||{}).phone||'919625959146')+'" target="_blank" rel="noopener">WhatsApp</a>.';
      b.disabled=false;b.textContent=old;
    });
  });
});

// Thank-you page text for feedback form
if(location.search.indexOf('type=feedback')>-1){
  var h=document.getElementById('ty-title'),p=document.getElementById('ty-text');
  if(h&&p){h.textContent='Thank you for your feedback!';p.textContent='Your feedback has been received. After a quick review it will be added to the Testimonials page.';}
}

// Live testimonials from Google Sheet (approved rows only). Static cards stay as fallback.
(function(){
  var C=window.SITE_CONFIG||{};
  var grids=document.querySelectorAll('.testimonial-grid[data-testi]');
  if(!C.testimonialsApi||!grids.length||!window.fetch) return;
  function card(t){
    var fig=document.createElement('figure');fig.className='testimonial-card';
    var r=Math.max(1,Math.min(5,parseInt(t.rating,10)||5));
    var st=document.createElement('div');st.className='stars';
    st.setAttribute('aria-label',r+' out of 5 stars');
    st.textContent=new Array(r+1).join('\u2605')+new Array(6-r).join('\u2606');
    var bq=document.createElement('blockquote'),p=document.createElement('p');
    p.textContent='\u201C'+String(t.message||'')+'\u201D';bq.appendChild(p);
    var cap=document.createElement('figcaption');cap.className='testimonial-name';
    var meta=[t.role,t.grade].filter(Boolean).join(', ');
    cap.textContent='\u2014 '+(t.name||'Anonymous')+(meta?' ('+meta+')':'');
    fig.appendChild(st);fig.appendChild(bq);fig.appendChild(cap);return fig;
  }
  fetch(C.testimonialsApi).then(function(r){return r.json();}).then(function(d){
    var list=(d&&d.testimonials)||[];
    if(!list.length) return;
    grids.forEach(function(g){
      var limit=g.getAttribute('data-testi')==='all'?Infinity:parseInt(g.getAttribute('data-testi'),10)||3;
      var fallback=[].slice.call(g.children);
      var items=list.slice(0,limit).map(card);
      // pad with the original sample cards so the page never looks empty
      for(var i=0;items.length<Math.min(3,limit)&&i<fallback.length;i++) items.push(fallback[i]);
      g.textContent='';items.forEach(function(n){g.appendChild(n);});
    });
  }).catch(function(){});
})();
