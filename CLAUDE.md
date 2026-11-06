# adsncodes.com working notes

- This repo is the master copy of the live site. Every change that goes live on adsncodes.com must also be committed and pushed here in the same session, with a short message saying what changed.
- Build: `cd site2 && python3 build.py`, then `python3 mkprod.py` from the repo root (writes `prod/`, which is ignored by git).
- Deploy: upload changed files from `prod/` to Hostinger `public_html` with `tools/up.sh` (needs a fresh upload key from the Hostinger connector, kept in an untracked `hkeys.sh`). Then clear the Hostinger cache and ping IndexNow for changed URLs.
- Never enable Hostinger Git auto-deploy: demo subdomains live inside `public_html` and would be deleted.
- `server/.htaccess` and `server/audit.php` are the live server copies; keep them in sync with what is uploaded.
- Never commit keys, tokens or passwords.
- Content rules: brand is always "Ads n' Codes"; no prices; case study clients stay anonymised; India/Calicut only on About/Contact; never "Bur Dubai" (use BurJuman); no hyphens in sentences of site copy; Arabic pages stay hidden (`AR_LIVE = False`) until a native speaker reviews them.
