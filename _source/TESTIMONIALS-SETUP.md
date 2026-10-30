# Testimonials: students khud likhein, website par apne aap dikhe

Ek baar ka setup (10 minute, free). Google account chahiye.

1. https://sheets.google.com par naya blank Sheet banao (naam kuch bhi, e.g. "Website Testimonials").
2. Menu: **Extensions -> Apps Script**.
3. Jo code pehle se likha hai use delete karo, aur `_source/testimonials-apps-script.gs` ki puri file paste karo. **Save** (Ctrl+S).
4. Upar **Run** dabao (function: `doGet`) -> Google permission maangega -> *Review permissions -> apna account -> Advanced -> Go to project (unsafe) -> Allow*. (Yeh sirf aapka apna script hai.)
5. **Deploy -> New deployment** -> gear icon -> **Web app**:
   - Execute as: **Me**
   - Who has access: **Anyone**
   - **Deploy** -> jo **Web app URL** mile (`https://script.google.com/macros/s/.../exec`) use copy karo.
6. `js/config.js` kholo, `"testimonialsApi": ""` ke andar woh URL paste karo. Phir `python3 _source/build.py` chalao (optional) aur GitHub par commit/push karo.

## Roz ka use
- Student form bharta hai -> row Sheet mein aati hai (aur aapko email aata hai).
- Row ke **Approved** checkbox ko tick karo -> website par aa jaata hai. Untick karo -> hat jaata hai.
- Bina approval ke seedha dikhana ho: script mein `AUTO_APPROVE = true` karo, phir **Deploy -> Manage deployments -> Edit -> New version -> Deploy**.

## Dhyan rakhein
- Script code badalne par hamesha "New version" deploy karna padta hai, URL wahi rehta hai.
- `testimonialsApi` khaali ho to form purane tareeke (Web3Forms email) se hi chalega.
