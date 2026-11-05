# 图稿来源与使用说明

当前README展示两张图：图1为交互闭环，图2为全量时间演进。研究树已从正文移除，原文件保留归档。

## 全量时间地图 v2

此前时间图是精选里程碑，本版改为97项全量目录图：80个W条目、14个H历史／方法背景、3个R人体数字人资源。ChatGPT背景另列，不计入97。每项含编号、简称、日期、机构及发表／证据标记。优先已核首公开日期，否则使用已核文献／正式日期；早期跨度压缩，年内只有年份的条目不假定准确先后顺序。

使用Matplotlib直接生成文字与图形，SVG保留真实文本与原文超链接。提供[SVG](../assets/embodied-affect-timeline-v2-all-works.svg)、[PNG](../assets/embodied-affect-timeline-v2-all-works.png)、[PDF](../assets/embodied-affect-timeline-v2-all-works.pdf)、[带搜索缩放的HTML](../assets/embodied-affect-timeline-v2-all-works.html)。旧的精选位图仍保留。

逐项核对结果：W001–W080、H001–H014、R001–R003恰各出现一次，遗漏0、重复0。97项混合不同文献／资源／背景身份，不宣称是97项独立的实体情感实验。机构缩写对应公开元数据中的发表时合作网络；头脸与身体基础为编辑主位置，不是互斥能力分区。

更新：2026-11-05。交互图和研究树使用内置 image_gen 工具生成或编辑；全量时间图以经过核验的数据重新排版为原生SVG／PDF和PNG，不编辑旧位图。它们不是从参考综述复制的原图。尺寸与校验值见清单。

| 图稿 | 内容 | 提示词／绘图源码 |
|---|---|---|
| [交互闭环](../assets/overview-v3.2-en-public.png) | 五阶段、六模块；新版本核正 GenEM 机构 | [提示词](../assets/prompts/overview-v3.2-en-public.txt) |
| [研究树](../assets/research-landscape-v4.1-zh-affiliations.png) | 理论根基、身体表达基础、核心技术与反馈；新版本核正 GenEM 机构 | [提示词](../assets/prompts/research-landscape-v4.1-zh-affiliations.txt) |
| [全量时间地图](../assets/embodied-affect-timeline-v2-all-works.png) | 全部80W＋14H＋3R，每个编号独立入图；按时间与研究环节定位 | [绘图源码](../tools/build_full_timeline.py) · [逐项位置](../data/timeline-full-coverage-v2.json) |

时间图借鉴用户提供的 Vid-LLMs 图的白底、曲线、标签与年代分组形式；内容与来源按本项目重新组织。交互故事图与研究树为已有项目插画的版本修订。图中机构采用文字与通用图标，不将图标解释为机构背书或排名。

时间曲线只组织阅读，不表示准确数量、成熟度、性能或必然因果。历史跨度采用非线性排布；同一工作的首公开与正式年份在元数据中分开。人体研究、机器人表达和具身系统相互支持，不能理解为前者被后者替代。

图面是精选导航，完整作者、版本、发表状态与证据边界以 README 和结构化索引为准。已有插画中的联合作者网络不用于推定每篇基础文献共享相同机构；例如 W047 为 Amy LaViers 单作者作品。

## 推荐图稿尺寸与校验

| 图稿 | 原生尺寸 | SHA256 |
|---|---|---|
| overview-v3.2-en-public.png | 1536 × 1024 | `e354a3bfb49423cd2c99ec64bfce43180273b9f8bf6c657bbbcc1af965dca64c` |
| research-landscape-v4.1-zh-affiliations.png | 1536 × 1024 | `3f2af4c1ff3880a86212796eb1c463a79e8b87d817fb01071cde8175c18cecaf` |
| embodied-affect-timeline-v1.1-en.png | 1536 × 1024 | `bbf6021e9025fe8a0947f6b6e76ae10a6f1994aa7dc4ebd8ff72b5ef88c9883c` |
