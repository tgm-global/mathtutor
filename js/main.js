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
    var s=f.querySelector('.form-status'),b=f.querySelector('button[type=submit]'),old=b.textContent;
    s.className='form-status';s.textContent='Sending...';b.disabled=true;b.textContent='Sending...';
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
