/* ===== SINGLE PLACE TO UPDATE CONTACT DETAILS + WEBSITE / LOGO NAME =====
   brandName   = logo, footer aur copyright mein dikhne wala naam (saare pages par ek saath badlega)
   brandAccent = brandName ka woh shabd jo logo mein alag rang mein dikhe (khaali chhodo to koi nahi)
   testimonialsApi = Google Apps Script "Web app URL" (steps: _source/TESTIMONIALS-SETUP.md)
   Yahin badlo, saari website par apne aap update ho jaayega.
   (Optional: badalne ke baad `python3 _source/build.py` chalao taaki Google ko dikhne wale
   static HTML/SEO data mein bhi same update ho jaaye.)
   phone = country code ke saath, bina + ya space ke. */
window.SITE_CONFIG = {
  "brandName": "Shaifali Jain Math Tutoring",
  "brandAccent": "Jain",
  "phone": "919625959146",
  "phoneDisplay": "+91 96259 59146",
  "email": "jshaifali91@gmail.com",
  "facebook": "https://www.facebook.com/shaifalimathstutor",
  "web3formsKey": "YOUR_WEB3FORMS_ACCESS_KEY",
  "testimonialsApi": "https://script.google.com/macros/s/AKfycby0e6nqtk1pH_op7El2TEP3z9tyQ0_8tvBQ1ZrpdkTy1HpZMY0TRHqrUftjil4-09w/exec"
};
