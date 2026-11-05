"""Render a standalone README HTML with local figures embedded byte-for-byte.

The portable GitHub README keeps repository-relative links. This offline copy
does not depend on a Markdown previewer's local-asset resolver.
Requires the already-installed pypandoc / pandoc for generation only.
"""
from pathlib import Path
import base64
import hashlib
import html
import json
import mimetypes
import re
import subprocess

STYLE = """
html{scroll-behavior:smooth;background:#0f1119;color:#dfe5ef;color-scheme:dark}
body{margin:0;font:17px/1.85 -apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC',sans-serif}
main{max-width:1440px;margin:auto;padding:32px 44px 80px}
nav{position:sticky;top:0;z-index:5;display:flex;gap:24px;flex-wrap:wrap;padding:14px 32px;background:#141724f5;border-bottom:1px solid #303650;font-size:15px}
nav a{color:#b7c0dc;text-decoration:none}nav a:hover{color:#36d8e9}
h1,h2,h3,h4{line-height:1.45;scroll-margin-top:90px}h1{font-size:44px;letter-spacing:-1px;color:#f5f7fc;margin-bottom:12px}
main a[id]{scroll-margin-top:90px}
h2{font-size:29px;margin-top:2.8em;border-bottom:1px solid #303650;padding-bottom:16px;color:#edf0f8}
h3{margin-top:2em;color:#33d1e2;font-size:23px}h4{color:#ece7ff;border-left:4px solid #7c6df1;padding:12px 18px;background:#1c2030;border-radius:0 8px 8px 0}
a{color:#35cfe5;overflow-wrap:anywhere;text-decoration:none}a:hover{text-decoration:underline}
p{margin:1em 0;color:#a9b5c9}strong{font-weight:650;color:#e2e8f4}
blockquote{position:relative;margin:0 0 0 16px;padding:8px 18px 25px 34px;border-left:2px solid #343955}
blockquote:before{content:'';position:absolute;top:22px;left:-8px;width:14px;height:14px;border-radius:50%;background:#7866f5;box-shadow:0 0 0 5px #0f1119}
blockquote:nth-of-type(2n):before{background:#2bcce0}blockquote p{margin:4px 0 10px}blockquote p:first-child strong{color:#ffb949}
blockquote p:nth-child(2) a{font-size:20px;color:#e2e8f4;font-weight:650}
img{display:block;max-width:100%;height:auto;margin:20px auto;background:white;border-radius:10px}
figure{margin:24px 0}figure img{cursor:zoom-in}
.table-scroll{overflow:auto;margin:22px 0;border:1px solid #343955;border-radius:10px}
table{border-collapse:collapse;min-width:100%;font-size:14px;line-height:1.8}
th,td{padding:13px 16px;border:1px solid #303650;vertical-align:top;min-width:100px}
th{background:#23283b;color:#e2e8f4;position:sticky;top:0}td:last-child{min-width:320px}tr:nth-child(even){background:#151925}td{color:#aebbd0}
pre{padding:16px;overflow:auto;background:#1c2030;border-radius:8px}code{background:#23283b;padding:2px 5px;border-radius:4px}
details{margin:28px 0;padding:16px 20px;border:1px solid #303650;border-radius:10px}summary{cursor:pointer;color:#c5baff;font-weight:650}
math{overflow:auto;max-width:100%}#lightbox{border:0;padding:0;max-width:96vw;max-height:96vh;overflow:auto;background:#fff}
#lightbox::backdrop{background:#000a}#lightbox img{max-width:none;margin:0}#lightbox button{position:sticky;top:10px;left:10px;z-index:1;padding:8px 16px}
@media(max-width:760px){main{padding:20px 18px}body{font-size:15px}h1{font-size:31px}h2{font-size:24px}nav{gap:10px 18px;padding:12px 18px;font-size:13px}blockquote{margin-left:6px;padding-left:22px}}
"""


def build_preview(directory):
    directory = Path(directory).resolve()
    source = directory / "README.md"
    markdown = source.read_text()
    embedded = []

    def embed(match):
        label, target = match.group(1), match.group(2).strip("<>")
        if target.startswith(("http://", "https://")):
            # Remote badges are decorative and should not cause offline requests.
            return ""
        image = (directory / target).resolve()
        assert image.is_file(), image
        binary = image.read_bytes()
        mime = mimetypes.guess_type(image.name)[0] or "application/octet-stream"
        encoded = base64.b64encode(binary).decode("ascii")
        embedded.append({"path": target, "sha256": hashlib.sha256(binary).hexdigest(), "bytes": len(binary)})
        return f'<figure><img alt="{html.escape(label, quote=True)}" src="data:{mime};base64,{encoded}" loading="eager"></figure>'

    markdown = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", embed, markdown)
    markdown = re.sub(r"^.*\[综述阅读版\]\(README\.preview\.html\).*$", "", markdown, flags=re.M)
    import pypandoc
    result = subprocess.run([pypandoc.get_pandoc_path(), "--from=gfm+tex_math_dollars+raw_html", "--to=html5", "--mathml", "--wrap=none"], input=markdown, text=True, capture_output=True, check=True)
    content = re.sub(r"(<table\b.*?</table>)", r'<div class="table-scroll">\1</div>', result.stdout, flags=re.S)
    page = '<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Awesome Embodied Affect — 具身情感计算综述</title><style>' + STYLE + '</style></head><body>'
    sections = [('overview', '研究动机'), ('taxonomy', '分类体系'), ('figures', '研究总览'), ('core-methods', '方法详解'), ('comparison', '横向对比'), ('catalog', '完整文献'), ('insights', '核心洞察')]
    page += '<nav aria-label="综述导航">' + ''.join(f'<a href="#{key}">{label}</a>' for key, label in sections) + '</nav><main>' + content + '</main>'
    page += '<dialog id="lightbox"><button type="button">关闭大图</button><img alt="放大图"></dialog><script>const box=document.getElementById("lightbox");document.querySelectorAll("main figure img").forEach(img=>img.addEventListener("click",()=>{box.querySelector("img").src=img.src;box.showModal()}));box.querySelector("button").onclick=()=>box.close();box.onclick=e=>{if(e.target===box)box.close()};</script></body></html>'
    assert len(embedded) == 2, len(embedded)
    assert len(re.findall(r'<img\b[^>]*src="data:image/png;base64,', page)) == 2
    assert not re.findall(r'<img\b[^>]*src="(?:https?://|\./?assets/)', page)
    (directory / "README.preview.html").write_text(page)
    return {"directory": directory.name, "images": embedded, "embedded_images": len(embedded), "html_bytes": len(page.encode())}


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    reports = [build_preview(root)]
    public = root.parent / "awesome-embodied-affect-public"
    if public.exists() and public != root:
        reports.append(build_preview(public))
    (root / "docs/readme-preview-audit-v1.json").write_text(json.dumps(reports, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(reports, ensure_ascii=False))
