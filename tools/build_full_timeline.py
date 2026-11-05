"""Create a new, exact-text scientific map from the entire reviewed catalog.

This draws a new vector visualization; it does not modify any generated raster.
"""
from pathlib import Path
from collections import Counter
import hashlib
import html
import json
import math
import os
import re
import textwrap
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT.parent / "awesome-embodied-affect-public"
if not PUBLIC.exists():
    PUBLIC = ROOT
os.environ.setdefault("MPLCONFIGDIR", "/private/tmp/embodied-affect-mpl-cache")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, PathPatch, Circle
from matplotlib.path import Path as MPath

plt.rcParams.update({"font.family": "DejaVu Sans", "svg.fonttype": "none", "pdf.fonttype": 42})
BASE = "embodied-affect-timeline-v2-all-works"

# Publication-network abbreviations, not current affiliations or rankings.
ORG = {
"W001":"DeepMind × Hoku Labs", "W002":"Apple", "W003":"Tokyo × Alternative Machine",
"W004":"Monash collaboration", "W005":"KITECH × UST", "W006":"Apple",
"W007":"Stuttgart SIR", "W008":"HKUST(GZ) × Shandong × RoboScience", "W009":"UCL",
"W010":"SJTU × ZTE", "W011":"Columbia collaboration", "W012":"Cornell / CMU / Plus One",
"W013":"RIKEN × Kyoto × NII", "W014":"USST × Droid × Hamburg", "W015":"RIKEN × Kyoto × NII",
"W016":"Ghent × imec", "W017":"Ghent × imec", "W018":"Southeast University × NUS",
"W019":"Geneva MIRALab", "W020":"Cambridge × Politecnico di Milano", "W021":"XJTLU × Liverpool",
"W022":"Kyoto × Boise State", "W023":"BLCU × Manchester × SHU × Penn State", "W024":"XJTLU",
"W025":"Nottingham CHART", "W026":"Author affiliations pending", "W027":"Macquarie × SYSU × SJTU",
"W028":"Cambridge", "W029":"VU Amsterdam", "W030":"Humboldt Berlin", "W031":"Uppsala",
"W032":"UCL", "W033":"Stuttgart SIR", "W034":"Stuttgart SIR", "W035":"Disney Research",
"W036":"Disney × UFRGS", "W037":"Disney Research", "W038":"Wuhan University",
"W039":"CU Boulder collaboration", "W040":"Honda Japan", "W041":"Honda Europe",
"W042":"Monash collaboration", "W043":"USST × Mech-Mind × CETC32 × Hamburg",
"W044":"Tsinghua × BAAI × MGI × Beihang", "W045":"Tsinghua MiLab × Neurobo", "W046":"ETH × Sony",
"W047":"RAD Lab · Amy LaViers", "W048":"Canberra × RAD × Penn State / Stelarc",
"W049":"Ghent × imec", "W050":"UBC SPIN", "W051":"USST",
"W052":"HKUST(GZ) / HKUST × CAS + partners", "W053":"SJTU RL²", "W054":"Nanjing Forestry University",
"W055":"XJTLU × UniSC", "W056":"HKUST × Shenzhen × Nankai", "W057":"Harbin Institute of Technology",
"W058":"BIT collaboration · affiliations provisional", "W059":"HUST collaboration",
"W060":"Hohai × Changzhou × Leicester × Manchester", "W061":"ZJUT · bibliography pending",
"W062":"Shanghai University", "W063":"Guangdong University of Technology", "W064":"CUHK collaboration",
"W065":"CAS-related Taicang computing institute", "W066":"UNIST", "W067":"UNIST", "W068":"UNIST",
"W069":"Osaka × Kobe", "W070":"NTU · affiliations provisional", "W071":"Oregon State SHARE",
"W072":"SeoulTech HCIR", "W073":"Liverpool · affiliations provisional", "W074":"BGU / TU Wien collaboration",
"W075":"BGU / TU Wien collaboration", "W076":"UCL", "W077":"CU Boulder × PLU", "W078":"Honda Europe",
"W079":"Sony + collaborators", "W080":"Intempus",
"H001":"Uppsala · Johansson", "H002":"UBC · Russell", "H003":"Tilburg · de Meijer",
"H004":"MGH / Harvard × Tilburg · de Gelder et al.", "H005":"MIT · Breazeal",
"H006":"Georgia Tech × IDC · Bretan / Hoffman / Weinberg", "H007":"UIUC × dance collaborators",
"H008":"Cornell × Honda Japan", "H009":"SFU ROSIE collaboration", "H010":"UC Berkeley",
"H011":"Google / Toronto author collaboration", "H012":"UC Berkeley", "H013":"OpenAI", "H014":"MIT · Picard",
"R001":"Tokyo × Keio × Huawei × JAIST", "R002":"Tokyo / Keio / MPI / JAIST / Tsinghua",
"R003":"East China Normal University",
}
H_NAMES={"H001":"Biological motion", "H002":"Affect circumplex", "H003":"Body motion & emotion",
"H004":"Whole-body affect perception", "H005":"Kismet", "H006":"Shimi", "H007":"Task-Constrained Laban",
"H008":"MoveAE", "H009":"Target VA-CVAE", "H010":"Functional Expressive Motion",
"H011":"Transformer", "H012":"DDPM", "H013":"GPT-4 Technical Report", "H014":"Affective Computing"}

ROWS=[
("SENSE","01", "Perceive human affect", "Situated face, voice, body and touch cues", "#1675b9", "#eef7fd"),
("UNDERSTAND & DECIDE","02", "Understand & decide", "Context, response target and timing", "#7957b8", "#f5f0fc"),
("AFFECT-CONDITIONED MOTION","3A", "Affect-conditioned generation", "Task content + affect / social expression", "#cc7a08", "#fff4d9"),
("PHYSICAL EXECUTION","3B", "Physical realization", "Tracking, task constraints, expression retention", "#c75f37", "#fff0e7"),
("HUMAN FEEDBACK","04", "Human interpretation & feedback", "Recognition, appropriateness and interaction outcomes", "#9961ab", "#f8effb"),
("REFINE & ADAPT","05", "Refine & adapt", "Correction, preferences and bounded adaptation", "#448a44", "#f0f8ec"),
("ROBOT MOVEMENT FOUNDATIONS","FB", "Robot body foundations", "Motion parameters, design, latent spaces and control", "#238d88", "#edf8f5"),
("FACE & HEAD FOUNDATIONS","FF", "Robot face & head foundations", "Actuation, expression mapping and timing", "#3a908c", "#eff8f7"),
("HUMAN BODY, THEORY & DATA","FH", "Human body & theory", "Perception, psychology and performing arts", "#b56286", "#fcf0f5"),
("VIRTUAL DATA","FD", "Virtual humans & motion data", "Transferable data / representations; physical gap remains", "#537ead", "#eff4fb"),
("ENGINEERING & CONCEPT CANDIDATES","EL", "Evidence-limited entries", "Abstract / engineering / white-paper evidence", "#77818c", "#f3f5f7"),
("AI-context","AI", "AI / LLM background", "Context, not a necessary dependency of every method", "#657488", "#f1f3f6"),
]

def dvalue(value):
    return (value or {}).get("value", "")


def safe_date(item):
    first=dvalue(item.get("first_public_date"))
    return first or dvalue(item.get("publication_date")), bool(first)


def venue_short(item):
    venue=item.get("venue", "")
    overrides={"W009":"preprint · RA-L under review", "W012":"THRI", "W020":"THRI", "W078":"ICRA workshop", "W077":"HRI workshop", "W026":"AIM abstract", "W065":"patent CN121661700A", "W080":"white paper"}
    if item["id"] in overrides:return overrides[item["id"]]
    replacements=[("IEEE Robotics and Automation Letters", "RA-L"), ("IEEE Transactions on Affective Computing", "TAFFC"),
        ("ACM Transactions on Human-Robot Interaction", "THRI"), ("ACM Transactions on Human–Robot Interaction", "THRI"),
        ("IEEE Transactions on Robotics", "T-RO"), ("Frontiers in Robotics and AI", "Frontiers RAI"),
        ("Applied Sciences", "Applied Sciences"), ("Computers in Human Behavior: Artificial Humans", "CHB: AH")]
    for old,new in replacements:venue=venue.replace(old,new)
    for key in ["HRI Companion", "HRI", "IROS", "ICRA", "RO-MAN", "CHI", "IUI", "ECCV", "CVPR", "SIGGRAPH", "ICSR", "ICIRA", "ICCRE", "APSIPA", "RSS", "Nature Sensors", "Nature Communications", "Science Robotics", "RA-L", "THRI", "TAFFC", "T-RO", "Frontiers RAI", "Sensors", "Biomimetics", "Applied Sciences", "CHB: AH"]:
        if key in venue:return key
    return {"W043":"Concurrency Comput.","W047":"Annual Review", "W051":"Applied Computer Research", "W061":"ICRAIC · report", "W062":"Computer Science", "W064":"JADD", "W065":"Patent CN121661700A", "W066":"JCROS", "W072":"Korean Robotics Society", "W079":"RSJ", "W080":"White paper", "R003":"CGF / PG"}.get(item["id"],"preprint" if "arxiv" in venue.lower() else "source record")


def lines(value, width):
    return textwrap.wrap(str(value), width=width, break_long_words=False, break_on_hyphens=False) or [""]


def main():
    w=json.loads((PUBLIC/"data/literature-public-v1.json").read_text())["records"]
    corrections=json.loads((ROOT/"data/timeline-date-corrections-v2.json").read_text())["records"]
    by={r["id"]:r for r in w}
    for correction in corrections:
        by[correction["id"]]["first_public_date"]=correction["first_public_date"]
    history=json.loads((ROOT/"data/timeline-milestones-v1.json").read_text())["milestones"]
    resources=json.loads((PUBLIC/"data/adjacent-resources-v1.json").read_text())["records"]
    records=[]
    for item in w:
        date,first=safe_date(item)
        pub=dvalue(item.get("publication_date"))
        venue=venue_short(item)
        kind="preprint" if "arxiv" in item.get("venue", "").lower() else ""
        kind={"W065":"patent", "W077":"dataset / workshop", "W080":"white paper", "W061":"report · pending", "W026":"abstract · pending", "W047":"review", "W048":"review", "W062":"survey"}.get(item["id"],kind)
        meta=(f"pub {pub[:4]} · {venue}" if pub[:4]!=date[:4] else venue)
        if kind and kind.lower() not in meta.lower():meta+=" · "+kind
        records.append({"id":item["id"],"alias":item["alias"],"row":item["primary_group"],"date":date,"date_basis":"first public" if first else "publication / dated source", "publication_date":pub,"org":ORG[item["id"]],"meta":meta,"url":item.get("paper_url"),"title":item["title"]})
    for item in history:
        if not item["id"].startswith("H"):continue
        first=(item.get("first_public") or {}).get("date")
        formal=item.get("formal") or {}
        date=first or formal.get("date")
        row={"人体":"HUMAN BODY, THEORY & DATA", "robot":"ROBOT MOVEMENT FOUNDATIONS", "AI-context":"AI-context"}[item["lane"]]
        records.append({"id":item["id"],"alias":H_NAMES[item["id"]],"row":row,"date":date,"date_basis":"first public" if first else "publication / dated source", "publication_date":formal.get("date"), "org":ORG[item["id"]],"meta":"historical source" if row!="AI-context" else "method / discipline background", "url":item["source_url"],"title":item["title"]})
    for item in resources:
        date,first=safe_date(item)
        pub=dvalue(item.get("publication_date"))
        records.append({"id":item["id"],"alias":item["alias"],"row":"VIRTUAL DATA","date":date,"date_basis":"first public" if first else "publication / dated source", "publication_date":pub,"org":ORG[item["id"]],"meta":f"pub {pub[:4]} · {venue_short(item)}" if pub[:4]!=date[:4] else venue_short(item),"url":item["paper_url"],"title":item["title"]})
    expected={f"W{i:03}" for i in range(1,81)}|{f"H{i:03}" for i in range(1,15)}|{f"R{i:03}" for i in range(1,4)}
    assert len(records)==97 and {r['id'] for r in records}==expected
    for r in records:
        assert re.match(r"^\d{4}(-\d{2})?(-\d{2})?$", r["date"]),r
        r["year"]=int(r["date"][:4]);r["column"]="≤2022" if r["year"]<=2022 else str(r["year"])
    columns=[("≤2022",2),("2023",1),("2024",2),("2025",3),("2026",3)]
    CARD_W=406;CARD_H=160;GX=14;GY=14;LEFT=410;MARGIN=64
    colinfo={};x=LEFT
    for label,ncols in columns:
        width=ncols*CARD_W+(ncols-1)*GX+40
        colinfo[label]={"x":x,"width":width,"ncols":ncols};x+=width+24
    W=x+MARGIN;HEADER=422; y=HEADER;rowinfo={}
    for key,tag,title,note,color,fill in ROWS:
        needed=max([math.ceil(sum(r["row"]==key and r["column"]==col for r in records)/n) for col,n in columns])
        side_height=85+len(lines(title,20))*31+18+len(lines(note,28))*24+24
        h=max(needed*(CARD_H+GY)+36,side_height)
        rowinfo[key]={"y":y,"height":h,"tag":tag,"title":title,"note":note,"color":color,"fill":fill}
        y+=h+14
    H=y+215
    fig=plt.figure(figsize=(W/100,H/100),dpi=100,facecolor="white")
    ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,W);ax.set_ylim(H,0);ax.axis("off")
    def label(x,y,value,px=22,color="#182638",weight="normal",**kwargs):
        return ax.text(x,y,value,fontsize=px*.72,color=color,weight=weight,va="top",fontfamily="DejaVu Sans",**kwargs)
    label(MARGIN,42,"EVOLUTION OF EMBODIED AFFECT",60,weight="bold")
    label(MARGIN,120,"Complete catalog map · Human foundations, robot expression and embodied interaction",29,color="#526174")
    label(MARGIN,174,"80 W entries  +  14 H foundations / method-background entries  +  3 R resources  =  97 unique placements",27,weight="bold")
    label(MARGIN,220,"Five-stage loop / six technical modules   •   Orange rows: first-stage research focus   •   Each ID appears exactly once",23,color="#526174")
    label(MARGIN,264,"Time = verified first public date when available; otherwise dated publication/source. Earlier decades are compressed. No performance or maturity axis.",21,color="#526174")
    # A gentle temporal spine retains the reference timeline's curve-and-chip language.
    centers=[c["x"]+c["width"]/2 for c in colinfo.values()]
    pts=[(centers[0],377),(centers[1],360),(centers[2],344),(centers[3],327),(centers[4],312)]
    vertices=[pts[0]];codes=[MPath.MOVETO]
    for (xa,ya),(xb,yb) in zip(pts,pts[1:]):
        vertices.extend([(xa+(xb-xa)*.38,ya),(xb-(xb-xa)*.38,yb),(xb,yb)])
        codes.extend([MPath.CURVE4]*3)
    ax.add_patch(PathPatch(MPath(vertices,codes),facecolor="none",edgecolor="#247cc8",lw=3))
    for (col,n), (cx,cy) in zip(columns,pts):
        ax.add_patch(Circle((cx,cy),7,facecolor="white",edgecolor="#247cc8",lw=2))
        count=sum(r["column"]==col for r in records)
        label(cx,cy-54,f"{col}  ·  {count} entries",27,color="#1d5d94",weight="bold",ha="center")
    placements=[]
    for key,tag,title,note,color,fill in ROWS:
        info=rowinfo[key];yy=info["y"];rh=info["height"]
        ax.add_patch(FancyBboxPatch((MARGIN,yy),W-MARGIN*2,rh,boxstyle="round,pad=0,rounding_size=20",facecolor=fill,edgecolor="none"))
        ax.add_patch(FancyBboxPatch((MARGIN+18,yy+22),64,44,boxstyle="round,pad=0,rounding_size=12",facecolor=color,edgecolor="none"))
        label(MARGIN+50,yy+29,tag,25,color="white",weight="bold",ha="center")
        for j,line in enumerate(lines(title,20)):label(MARGIN+20,yy+85+j*31,line,25,color=color,weight="bold")
        for j,line in enumerate(lines(note,28)):label(MARGIN+20,yy+85+len(lines(title,20))*31+18+j*24,line,18,color="#526174")
        for col,ncols in columns:
            selected=sorted([r for r in records if r["row"]==key and r["column"]==col],key=lambda r:(r["date"],r["id"]))
            ci=colinfo[col]
            for j,r in enumerate(selected):
                xx=ci["x"]+20+(j%ncols)*(CARD_W+GX);ty=yy+18+(j//ncols)*(CARD_H+GY)
                core=key in {"AFFECT-CONDITIONED MOTION","PHYSICAL EXECUTION"}
                bg=FancyBboxPatch((xx,ty),CARD_W,CARD_H,boxstyle="round,pad=0,rounding_size=14",facecolor="white",edgecolor=color if r["id"]=="W009" else "#dce3e9",linewidth=2.3 if r["id"]=="W009" else .8)
                bg.set_gid("node-"+r["id"]);bg.set_url(r["url"]);ax.add_patch(bg)
                ax.add_patch(FancyBboxPatch((xx,ty+15),5,CARD_H-30,boxstyle="round,pad=0,rounding_size=2",facecolor=color,edgecolor="none"))
                label(xx+17,ty+12,r["id"],22,color=color,weight="bold",url=r["url"])
                label(xx+CARD_W-14,ty+13,r["date"],18,color="#637187",ha="right",url=r["url"])
                name_lines=lines(r["alias"],28)
                assert len(name_lines)<=2,(r["id"],name_lines)
                for z,t in enumerate(name_lines):label(xx+17,ty+43+z*26,t,23,weight="bold",url=r["url"])
                org_lines=lines(r["org"],43)
                assert len(org_lines)<=2,(r["id"],org_lines)
                for z,t in enumerate(org_lines):label(xx+17,ty+101+z*20,t,16,color="#425367",url=r["url"])
                label(xx+17,ty+141,r["meta"],14,color="#758194",url=r["url"])
                placements.append({**r,"x":xx,"y":ty,"width":CARD_W,"height":CARD_H})
    label(MARGIN,y+18,"READING THE MAP",23,weight="bold")
    label(MARGIN,y+59,"Rows are editorial primary placements, not mutually exclusive capabilities. W041 / W078 are related works, not two automatically independent breakthroughs.",20,color="#526174")
    label(MARGIN,y+94,"AI context: ChatGPT research preview, 2022-11-30 (shown here separately; not counted among the 97 indexed entries).",20,color="#526174")
    label(MARGIN,y+129,"Record types remain distinct: research / review / dataset / workshop / patent / white paper / limited evidence. Full metadata and scholars: README.",20,color="#526174")
    label(MARGIN,y+165,"Coverage audited: W001–W080 + H001–H014 + R001–R003. Click a card in the SVG / HTML to open its original source.",20,color="#247cc8",weight="bold")
    for ext in ["svg","png","pdf"]:
        fig.savefig(ROOT/"assets"/(BASE+"."+ext),dpi=100,facecolor="white")
    plt.close(fig)
    # Preserve actual SVG text, IDs and live source links for zoom/search.
    svgpath=ROOT/"assets"/(BASE+".svg")
    svg=svgpath.read_text();svg=re.sub(r'width="[\d.]+pt"',f'width="{W}px"',svg,count=1);svg=re.sub(r'height="[\d.]+pt"',f'height="{H}px"',svg,count=1)
    svgpath.write_text(svg)
    manifest={"date":"2026-11-05","scope":"97 indexed literature/resource/background entries; not 97 independent robot affect experiments","width":W,"height":H,"counts":{"W":80,"H":14,"R":3},"column_counts":dict(Counter(r["column"] for r in placements)),"date_policy":"verified first public when available, otherwise publication/dated source; early span compressed","placements":placements}
    (ROOT/"data/timeline-full-coverage-v2.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
    actual=set(re.findall(r'id="node-([WHR]\d{3})"',svg))
    assert actual==expected and len(placements)==97
    body=svg[svg.index("<svg"):]
    page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Embodied Affect — Complete Timeline</title><style>body{margin:0;background:#f2f5f8;color:#182638;font:15px system-ui}header{position:sticky;top:0;z-index:3;background:#fff;border-bottom:1px solid #dce3e9;padding:14px 20px;display:flex;gap:16px;align-items:center;flex-wrap:wrap}h1{font-size:19px;margin:0}input[type=search]{padding:8px 12px;border:1px solid #bccbda;border-radius:7px;width:230px}button{padding:7px 13px;border:1px solid #bccbda;border-radius:7px;background:#fff;cursor:pointer}#viewport{height:calc(100vh - 86px);overflow:auto}#sizer{position:relative}#stage{transform-origin:top left;position:absolute;background:white}#status{color:#5b6c80}svg{display:block}</style><header><h1>Complete Embodied Affect Map</h1><input id="find" type="search" placeholder="Find W009, PAMoR, H001…"><button id="search">Find</button><button id="fit">Fit width</button><label>Zoom <input id="zoom" type="range" min="12" max="160" value="30"> <span id="pct"></span></label><span id="status">97 indexed entries · drag scrollbars to explore</span></header><div id="viewport"><div id="sizer"><div id="stage">__SVG__</div></div></div><script>const data=__DATA__,W=__W__,H=__H__;const stage=document.getElementById('stage'),sizer=document.getElementById('sizer'),view=document.getElementById('viewport'),slider=document.getElementById('zoom');let scale=.3;function zoom(v){scale=v;stage.style.transform=`scale(${v})`;sizer.style.width=W*v+'px';sizer.style.height=H*v+'px';slider.value=Math.round(v*100);document.getElementById('pct').textContent=Math.round(v*100)+'%'}function fit(){zoom(Math.max(.12,(view.clientWidth-24)/W))}document.getElementById('fit').onclick=fit;slider.oninput=()=>zoom(slider.value/100);function find(){const q=document.getElementById('find').value.trim().toLowerCase();for(const r of data){const g=document.getElementById('node-'+r.id);if(g)g.style.filter='';}if(!q)return;const r=data.find(r=>r.id.toLowerCase()===q)||data.find(r=>(r.alias+' '+r.title+' '+r.org).toLowerCase().includes(q));if(!r){document.getElementById('status').textContent='No match';return;}zoom(Math.max(.7,scale));const g=document.getElementById('node-'+r.id);if(g)g.style.filter='drop-shadow(0 0 8px #ec7900)';view.scrollTo({left:Math.max(0,r.x*scale-80),top:Math.max(0,r.y*scale-60),behavior:'smooth'});document.getElementById('status').textContent=r.id+' · '+r.alias+' · '+r.date;}document.getElementById('search').onclick=find;document.getElementById('find').onkeydown=e=>{if(e.key==='Enter')find()};fit();</script></html>'''
    page=page.replace("__SVG__",body).replace("__DATA__",json.dumps(placements,ensure_ascii=True).replace("</","<\\/")).replace("__W__",str(W)).replace("__H__",str(H))
    (ROOT/"assets"/(BASE+".html")).write_text(page)
    audit={"date":"2026-11-05","expected_ids":sorted(expected),"svg_ids":sorted(actual),"missing_ids":sorted(expected-actual),"duplicate_placements":len(placements)-len(actual),"total":len(actual),"rendered_pixels":[W,H],"method":"New data-driven scientific visualization, Matplotlib SVG/PNG/PDF; existing raster artwork untouched","hashes":{e:hashlib.sha256((ROOT/"assets"/(BASE+"."+e)).read_bytes()).hexdigest() for e in ["svg","png","pdf","html"]}}
    (ROOT/"docs/timeline-full-audit-v2.json").write_text(json.dumps(audit,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"total":len(actual),"missing":audit["missing_ids"],"duplicates":audit["duplicate_placements"],"size":[W,H],"columns":manifest["column_counts"]}))


if __name__=="__main__":main()
