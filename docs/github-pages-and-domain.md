# GitHub Pages and Cloudflare domain

Repository: [meorajrul/meor-blog](https://github.com/meorajrul/meor-blog). Production domain: **meorajrul.com**. Canonical URLs use HTTPS at the apex. Cloudflare supplies DNS; GitHub Pages serves the static site.

## Deployment

Enable Pages with **GitHub Actions** as the build source. `pages.yml` runs tests, checks public article packets, builds the production Hugo site, validates links and output boundaries, and deploys only `site/public/`. A draft remains excluded. A failed gate stops publication.

Set **meorajrul.com** under repository Settings → Pages → Custom domain. With a custom Actions workflow, GitHub ignores CNAME as configuration; `site/static/CNAME` documents the domain but does not replace the repository setting. [GitHub's domain guide](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site) and [Hugo's deployment guide](https://gohugo.io/host-and-deploy/deploy-to-github-pages/) were inspected on 2026-10-18.

## Exact Cloudflare records

Inspect existing web records first. Add the following in the existing zone, with **DNS only** (gray cloud) and TTL Auto. Preserve unrelated mail, TXT and other records. If an existing apex/www web record conflicts, review it before replacement.

| Type | Name | Target | Proxy |
| --- | --- | --- | --- |
| A | @ | 185.199.108.153 | DNS only |
| A | @ | 185.199.109.153 | DNS only |
| A | @ | 185.199.110.153 | DNS only |
| A | @ | 185.199.111.153 | DNS only |
| CNAME | www | meorajrul.github.io | DNS only |

The www target is the account host, **without `/meor-blog`**. Correct apex and www configuration lets GitHub redirect www to the configured apex. The initial DNS-only choice simplifies direct GitHub verification and certificate handling; it is a project decision, not Cloudflare's universal web recommendation. [Cloudflare proxy behavior](https://developers.cloudflare.com/dns/proxy-status/) explains the difference.

Optional IPv6 is omitted to keep the initial setup small. If existing AAAA records point elsewhere, inspect them because some clients may still reach the wrong server. Do not add wildcard web records.

For account-level domain verification, request the exact TXT challenge from GitHub Settings → Pages and copy that value into Cloudflare. Never invent a verification token. This is useful protection against domain reuse; it is distinct from connecting the repository's custom domain.

## Verify completion

1. Observe the GitHub Actions deployment succeeding.
2. Query public DNS and confirm the apex A records and www CNAME.
3. Check the Pages DNS result and certificate state. Once the certificate is ready, enable **Enforce HTTPS**.
4. Open `https://meorajrul.com/`, About, Journal and Search. Check the www redirect and HTTPS certificate.
5. Record actual status in `docs/verification.md`; DNS propagation or certificate issuance may still be pending even after a successful deployment.

The public GitHub repository exposes tracked drafts and research; only the served artifact boundary keeps those files off the website. Keep sensitive personal notes in ignored `private/`.
