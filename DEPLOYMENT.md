# Deployment

Static site. No build command, no environment variables, no secrets.

---

## Before the first push — security check

Run these from inside the site folder and confirm each returns nothing:

```bash
grep -rniE "password|passwd|api[_-]?key|secret|token|BEGIN (RSA|OPENSSH|PRIVATE)" \
  --include="*.html" --include="*.css" --include="*.js" --include="*.json" --include="*.md" .
find . -name "*.env*" -o -name "*.pem" -o -name "*.key" -o -name "wrangler.toml"
```

Never commit credentials, control-panel logins, email passwords, FTP details, social
account passwords or API keys — not to files, not to commit messages, not to the README.
**Any credential that has previously been shared in a chat, email or screenshot must be
treated as compromised and rotated**, whether or not it ever reached this repository.

---

## GitHub

Do not create an account for the client. Once they have one and are signed in:

```bash
cd africa-rising-investments
git init
git add .
git status          # READ THIS LIST before committing
git commit -m "Africa Rising Investments website prototype"
git branch -M main
git remote add origin https://github.com/<account>/africa-rising-investments.git
git push -u origin main
```

Repository name: `africa-rising-investments`. Keep it **private** until the client
approves publication — the site is flagged `noindex` but a public repository is public.

---

## Cloudflare Pages

1. Cloudflare dashboard → **Workers & Pages** → **Create** → **Pages** → **Connect to Git**.
2. Authorise GitHub and select `africa-rising-investments`.
3. Build settings:
   - Framework preset: **None**
   - Production branch: **main**
   - Build command: **leave empty**
   - Build output directory: **/** (repository root)
4. Deploy. The site appears at the Pages URL assigned by Cloudflare.
5. Test the live deployment: every page, both nav states, all three PDF downloads, the
   404 (visit a URL that does not exist), and the site on a phone.
6. Share the deployed preview link with the client for review.

Every push to `main` redeploys. Every other branch gets its own preview URL, which is a
convenient way to show the client a change before it goes live.

---

## Connecting `africa.or.ke` — do not rush this

**The domain may also carry business email.** Changing nameservers without checking MX
records will silently stop email delivery, and the failure is not obvious for hours.

Do not proceed until all five of these are true:

1. A backup of the current `africa.or.ke` website exists and has been verified.
2. The client has approved the new site in writing.
3. Every existing DNS record has been exported and saved — **A, AAAA, CNAME, MX, TXT
   (SPF/DKIM/DMARC), SRV, NS**. Screenshot the current zone as well.
4. The new deployment has been tested on the `.pages.dev` URL.
5. A written rollback plan exists: exactly which records to restore, to what values, and
   who does it.

Then:

1. Confirm with the client, immediately before acting, that you may change DNS.
2. In Cloudflare Pages → **Custom domains**, add `africa.or.ke` and `www.africa.or.ke`.
3. If moving nameservers to Cloudflare, **recreate every record from step 3 in the
   Cloudflare zone before changing the nameservers at the registrar** — especially MX and
   the SPF/DKIM/DMARC TXT records.
4. After propagation, send and receive a test email on the domain before you consider it done.
5. Keep the old hosting live and paid for at least 30 days.

If any of this is uncertain, deploy on a subdomain (`new.africa.or.ke`) first. It carries
none of the email risk and gives the client a real preview.
