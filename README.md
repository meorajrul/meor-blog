# Meor Ajrul — personal journal

A broad personal journal at **https://meorajrul.com**, hosted by GitHub Pages from [meorajrul/meor-blog](https://github.com/meorajrul/meor-blog).

Start with [START-HERE.md](START-HERE.md). [Project plan](docs/project-plan.md) explains the choices and remaining work. [Research findings](research/findings.md) distinguish sourced guidance, our adaptations, and untested assumptions.

| Folder | What belongs here |
| --- | --- |
| `site/` | Hugo website: publishable Markdown in `content/`, design in `assets/` and `layouts/`, images in `static/` |
| `editorial/` | Topic inbox, publishing policy, and editorial workflow |
| `research/` | Reference library, research state, tests, and article evidence packets |
| `plugins/meor-journal/` | Reusable AI skills, templates, and validation tools; the maintained source |
| `plugins/packages/` | Versioned installable source archive |
| `scripts/` | Convenient entry points for everyday work |
| `docs/` | Folder map, frameworks, deployment, and maintenance |
| `.github/workflows/` | Validation, production build, and GitHub Pages deployment |
| `.agents/plugins/` | Repo plugin marketplace |
| `private/` | Local-only personal material; ignored by Git |
| `output/`, `.tools/` | Local reports, previews, and build tools; ignored by Git |

The previous `blog-staging/` and `plugins/meor-blog-plugins/` are preserved locally and ignored. The new source of truth is `site/` and `plugins/meor-journal/`.

Only `site/public/` is deployed to Pages. **Every tracked file, including drafts and research notes, is public in this repository.** Keep sensitive journal notes in `private/` until you prepare a public version.

## Build and check

Python 3.11+ and Hugo 0.167.0 are sufficient; Node, a database, and Docker are not required.

```powershell
python scripts/blog.py new my-topic --genre reflection
python scripts/blog.py check
.tools/hugo/hugo.exe --source site --environment production --minify
python scripts/blog.py check-output --directory site/public
```

On macOS/Linux use the matching Hugo executable. GitHub Actions installs the pinned Linux version automatically. The deploy workflow uses `main`, runs the editorial gate, builds only the site, and uploads only the static output.

## Skills and installation

See [plugins/meor-journal/README.md](plugins/meor-journal/README.md). The source and marketplace are versioned together. Installation and verification status is recorded in [docs/verification.md](docs/verification.md).
