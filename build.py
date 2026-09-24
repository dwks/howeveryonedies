#!/usr/bin/env python3
"""Build How Everyone Dies from the sources in src/ into dist/.

Everything in dist/ is generated and everything served comes from there:

  * the site      -- dist/index.html, mechanisms.html, explanation.html and
                     scenarios.html, four real pages that work without JS,
                     alongside a copy of the stylesheet.
  * the artifact  -- dist/artifact.html, a single document holding all four
                     views behind a hash router, because a published Claude
                     Artifact is one page. Not part of the served site.

Partials link to each other with {{href <view>}} or {{href <view> <anchor>}};
each output resolves those to whatever its own navigation needs.
"""

import pathlib
import re
import shutil

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "src"
DIST = ROOT / "dist"

VIEWS = [
    ("home", "How Everyone Dies", None),
    ("mechanisms", "A few different ways everyone could die", "Mechanisms"),
    ("explanation", "Four steps to an explanation", "Explanation"),
    ("scenarios", "Other people's scenarios, summarised", "Scenarios"),
]
TITLES = {name: title for name, title, _ in VIEWS}
NAV = [(name, label) for name, _, label in VIEWS if label]

HEAD = """<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700&family=IBM+Plex+Mono:wght@400;500&family=Newsreader:opsz,wght@6..72,400;6..72,500&display=swap">
<link rel="stylesheet" href="styles.css">"""

HREF = re.compile(r"\{\{href ([a-z]+)(?: ([a-z0-9-]+))?\}\}")


def resolve(html, link):
    return HREF.sub(lambda m: link(m.group(1), m.group(2)), html)


def page_link(view, anchor):
    path = "index.html" if view == "home" else view + ".html"
    return path + ("#" + anchor if anchor else "")


def hash_link(view, anchor):
    if view == "home" and not anchor:
        return "#/"
    return "#/" + view + ("/" + anchor if anchor else "")


def topbar(link, current=None):
    rows = [
        '<header class="topbar">',
        '  <div class="topbar-inner">',
        '    <a class="wordmark" href="%s">How Everyone Dies</a>' % link("home", None),
        '    <nav aria-label="Parts">',
    ]
    for name, label in NAV:
        mark = ' aria-current="page"' if name == current else ""
        rows.append(
            '      <a href="%s" data-nav="%s"%s>%s</a>' % (link(name, None), name, mark, label)
        )
    rows += ["    </nav>", "  </div>", "</header>"]
    return "\n".join(rows)


def document(title, body):
    return (
        '<!doctype html>\n<html lang="en">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        + HEAD.format(title=title)
        + "\n</head>\n<body>\n"
        + body
        + "\n</body>\n</html>\n"
    )


def build_site(partials):
    for name, title, _ in VIEWS:
        body = "\n".join(
            [
                '<a class="skip" href="#main">Skip to content</a>',
                topbar(page_link, current=name),
                '<div class="shell">',
                '<main id="main">',
                resolve(partials[name], page_link),
                "</main>",
                "</div>",
            ]
        )
        full = title if name == "home" else "%s · How Everyone Dies" % title
        out = DIST / page_link(name, None)
        out.write_text(document(full, body))
        print("built dist/%s" % out.name)


ROUTER = """<script>
(function () {
  var TITLES = %s;
  var views = Array.prototype.slice.call(document.querySelectorAll('[data-view]'));
  var navs = Array.prototype.slice.call(document.querySelectorAll('[data-nav]'));
  function route() {
    var m = /^#\\/([a-z]+)(?:\\/([a-z0-9-]+))?/.exec(location.hash);
    var view = m && TITLES[m[1]] ? m[1] : 'home';
    views.forEach(function (v) { v.hidden = v.getAttribute('data-view') !== view; });
    navs.forEach(function (a) {
      if (a.getAttribute('data-nav') === view) a.setAttribute('aria-current', 'page');
      else a.removeAttribute('aria-current');
    });
    document.title = view === 'home' ? TITLES.home : TITLES[view] + ' \\u00b7 How Everyone Dies';
    var anchor = m && m[2] && document.getElementById(m[2]);
    if (anchor) anchor.scrollIntoView();
    else window.scrollTo(0, 0);
  }
  window.addEventListener('hashchange', route);
  route();
})();
</script>"""


def build_artifact(partials):
    sections = []
    for name, _, _ in VIEWS:
        sections.append(
            '<section class="view" data-view="%s"%s>\n%s\n</section>'
            % (name, "" if name == "home" else " hidden", resolve(partials[name], hash_link))
        )
    body = "\n".join(
        [
            HEAD.format(title="How Everyone Dies"),
            '<a class="skip" href="#/">Skip to content</a>',
            topbar(hash_link, current="home"),
            '<div class="shell">',
            '<main id="main">',
            "\n".join(sections),
            "</main>",
            "</div>",
            ROUTER % repr(TITLES).replace("'", '"'),
        ]
    )
    (DIST / "artifact.html").write_text(body + "\n")
    print("built dist/artifact.html")


def main():
    DIST.mkdir(exist_ok=True)
    shutil.copyfile(SRC / "styles.css", DIST / "styles.css")
    print("built dist/styles.css")
    partials = {name: (SRC / (name + ".html")).read_text().strip() for name, _, _ in VIEWS}
    build_site(partials)
    build_artifact(partials)
    left = {m.group(0) for p in partials.values() for m in HREF.finditer(p)}
    broken = [t for t in left if HREF.match(t).group(1) not in TITLES]
    if broken:
        raise SystemExit("unknown link target: " + ", ".join(sorted(broken)))


if __name__ == "__main__":
    main()
