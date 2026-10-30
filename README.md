# Shaifali Jain Math Tutoring - website

Static website (HTML/CSS/JS). Hosted on GitHub Pages.

## Phone / email / Facebook / Web3Forms key
Edit ONLY `js/config.js`. Change appears on every page automatically.
Optional: run `python3 _source/build.py` afterwards so the static HTML (SEO) also matches.

## Logo / website name
Edit `brandName` (and `brandAccent`, the highlighted word) in `js/config.js`. Logo, footer and copyright change on every page.
Run `python3 _source/build.py` to also update page titles / SEO text.

## Testimonials (students submit, shown automatically)
See `_source/TESTIMONIALS-SETUP.md` (Google Sheet + Apps Script, one-time setup).

## Other settings (`_source/build.py`, top of file)
- `GITHUB_USER`, `REPO` - GitHub username and repository name
- `CUSTOM_DOMAIN` - fill only if you use your own domain

After changing anything in `build.py`, run `python3 _source/build.py` and commit all files.

## Deploy
Repo -> Settings -> Pages -> Source: "Deploy from a branch" -> Branch: `main`, folder `/ (root)`.
