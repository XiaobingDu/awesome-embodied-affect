# 具身情感研究时间叙事 v1

日期：2026-11-05。配套数据：[timeline-milestones-v1.json](../data/timeline-milestones-v1.json)。本次在既有80条目录之外，为时间叙事补充历史与AI背景节点H001—H014，原有W编号不变。本表精选25个节点，不是历史穷尽表，不推断“最早”“首次”或机构排名。

## 叙事主旨

这段历史不是“人体理论→传统机器人→大模型机器人”依次替代的阶梯。更准确的叙事是：**人体与心理研究持续提供表达和解读的依据；机器人表达研究持续发展参数、表示、物理实现与人的校准；AI方法为其中一部分提供新的生成和语义接口；近期系统把这些能力以不同方式组合到具身互动中。**

早期Kismet和Shimi已具有感知、状态/情境处理和表达回应的耦合。因此，完整概念闭环并不是2026年首次出现。PAMoR等近期工作的重要性在于其具体的条件定义、可组合生成、实时全身实现及验证范围，不能将“情感接动作”本身作为新颖性。

建议时间图采用四条平行研究带：

1. **人体／情感理论与知觉：** 点光运动知觉、情感维度、身体运动的情感归因、身体情感知觉机制。
2. **机器人表达能力：** 参数化表达、潜空间与目标VA、任务约束、人的感知与偏好校准；此带继续延伸到2025/2026。
3. **具身表达系统：** 语言到动作接口、情感条件化生成、全身物理执行与表达特征保持；此带与robot带交叠。
4. **AI方法背景：** 情感计算、Transformer、扩散、LLM等并行背景；用较弱颜色或更窄带展示，不混作机器人情感实证。

“robot／embodied”的泳道是编辑上的研究侧重，不是断言前者没有智能、前者不具身，或后者必然使用LLM。人体表示和机器人原生表示也都是可选择的建模路线；扩散/flow无需必然经过LLM。

## 时间标记规范

- `year` 为主图建议锚点；近期研究尽量按已核最早公开稿落点，`first_public.date`与`formal.date`分别保留。
- `first_public.date = null` 表示未核更早公开稿或最早网络上线时间，**不表示以前没有公开研究**。
- 实心圆可以表示正式论文/著作；空心圆表示预印本；学位论文另用小菱形。与同一作品的正式版本之间可加短连线，不能重计作独立算法。
- Kismet的2000是学位论文节点，不是机器人项目起始年；2002/2003的互动调节论文作为续作注明。
- Alter3为**2023首公开→2025正式**；EMOTION为**2024首公开→2025正式**，不能统称2025首次提出。
- PAMoR、SocialHumanoid、Beyond Kinematic Tracking、RoboMMT在所核原始记录中保留预印本标记；PAMoR仍注明RA-L在审。
- 1973—2004历史段可以压缩和断轴，2023—2026适当放大。图注明确：**“时间位置示意，历史段有压缩，非线性刻度。”** 不用等距点暗示真实等间隔。
- 不将顺序相邻画成因果依赖；若画支撑箭头，必须有具体表示/方法或引用关系依据。LLM不得画成所有扩散/flow生成的必经输入。

## 经核验的25个节点

| ID | 主锚点 | 公开／正式时间 | 泳道 | 作品与机构 | 供图中使用的短说明 | 一手来源 |
|---|---:|---|---|---|---|---|
| H001 | 1973 | 正式/文献日期 1973-06 | 人体 | Johansson 点光运动；Uppsala University — Gunnar Johansson | 点光运动：从稀疏关节点读出身体运动 | [原始记录](https://link.springer.com/article/10.3758/BF03212378) |
| H002 | 1980 | 正式/文献日期 1980 | 人体 | Russell 情感环形模型；University of British Columbia — James A. Russell | 情感环形模型：愉悦度与唤醒度的理论基础 | [原始记录](https://pdodds.w3.uvm.edu/research/papers/others/1980/russell1980a.pdf) |
| H003 | 1989 | 正式/文献日期 1989-12 | 人体 | de Meijer 身体情感归因；Tilburg University — Marco de Meijer | 身体运动特征与人的情感归因 | [原始记录](https://link.springer.com/article/10.1007/BF00990296) |
| H014 | 1997 | 正式/文献日期 1997-09-24 | AI-context | Picard《情感计算》；MIT Media Lab — Rosalind W. Picard | 情感计算：感知、理解与回应情感的研究背景 | [原始记录](https://mitpress.mit.edu/9780262161701/affective-computing/) |
| H005 | 2000 | 正式/文献日期 2000-05 | robot | Kismet；MIT — Cynthia L. Breazeal | Kismet：感知、内部状态与社会表达调节互动 | [原始记录](https://groups.csail.mit.edu/lbr/hrg/2000/phd.pdf) |
| H004 | 2004 | 公开 2004-11-16；正式/文献日期 2004-11-23 | 人体 | de Gelder 身体情感知觉；MGH / Harvard Medical School × Tilburg University — Beatrice de Gelder 等 | 身体情感知觉的神经机制支撑 | [原始记录](https://pmc.ncbi.nlm.nih.gov/articles/PMC528902/) |
| H006 | 2015 | 公开 2015-02-04；正式/文献日期 2015 | robot | Shimi；Georgia Institute of Technology × IDC Herzliya — Mason Bretan / Guy Hoffman / Gil Weinberg | Shimi：参数化身体表达接入语言情感分析 | [原始记录](https://hrc2.io/assets/pdfs/papers/BretanetalIJHCS15.pdf) |
| H011 | 2017 | 公开 2017-06-12；正式/文献日期 2017 | AI-context | Transformer；Google Brain / Google Research / University of Toronto 作者合作 | Transformer：序列建模的方法背景 | [原始记录](https://arxiv.org/abs/1706.03762) |
| H007 | 2019 | 正式/文献日期 2019-03-27 | robot | Task-Constrained Laban；University of Illinois at Urbana-Champaign × independent dance / Laban/Bartenieff Institute / McGuffey Art Center — Hang Cui / Catherine Maguire / Amy LaViers | 任务约束下的Laban运动变化 | [原始记录](https://archive.the-rad-lab.org/laban-inspired-task-constrained-expressive-variable-motion-generation-on-aerial-robots) |
| H008 | 2020 | 正式/文献日期 2020-03 | robot | MoveAE；Cornell University × Honda Research Institute Japan — Michael Suguitan / Randy Gomez / Guy Hoffman | VAE潜空间编辑机器人的情感动作 | [原始记录](https://msgtn.io/assets/pdf/hri20-moveae.pdf) |
| H009 | 2020 | 正式/文献日期 2020 | robot | Target VA-CVAE；SFU ROSIE Lab 合作研究线 — Mina Marmpena / Fernando Garcia / Angelica Lim | 目标VA参与CVAE身体语言生成 | [原始记录](https://www.rosielab.ca/projects) |
| H012 | 2020 | 公开 2020-06-19；正式/文献日期 2020 | AI-context | DDPM；University of California, Berkeley — Jonathan Ho / Ajay Jain / Pieter Abbeel | 扩散生成模型：一条独立的方法研究线 | [原始记录](https://arxiv.org/abs/2006.11239) |
| H010 | 2022 | 公开 2022-03-04；正式/文献日期 2022 | robot | Functional Expressive Motion；University of California, Berkeley — Arjun Sripathy / Andreea Bobu / Zhongyu Li / Koushil Sreenath / Daniel S. Brown / Anca D. Dragan | 学习人的VAD感知，并联合优化任务与表达 | [原始记录](https://arxiv.org/abs/2203.02091) |
| H013 | 2023 | 公开 2023-03-15；正式版本本轮未核 | AI-context | GPT-4 技术报告；OpenAI | 大语言模型：语义理解、编排与代码生成背景 | [原始记录](https://arxiv.org/abs/2303.08774) |
| W003 | 2023 | 公开 2023-12-11；正式/文献日期 2025-05-27 | embodied | Alter3；University of Tokyo × Alternative Machine — Takahide Yoshida / Atsushi Masumori / Takashi Ikegami | 自然语言经程序接口驱动实体Alter3 | [原始记录](https://arxiv.org/abs/2312.06571) |
| W001 | 2024 | 公开 2024-01-26；正式/文献日期 2024-03 | embodied | GenEM；Google DeepMind × Hoku Labs — Karthik Mahadevan / Leila Takayama 等 | 语言社会意图→参数化控制代码与纠正 | [原始记录](https://arxiv.org/abs/2401.14673) |
| W002 | 2024 | 公开 2024-10-30；正式/文献日期 2025 | embodied | EMOTION；Apple论文作者群 — Peide Huang / Yuhan Hu 等 | LLM上下文学习生成手势序列；反馈修订 | [原始记录](https://arxiv.org/abs/2410.23234) |
| W012 | 2024 | 正式/文献日期 2024-08 | robot | Face2Gesture；Cornell / CMU / Plus One Robotics / Independent Researcher；部分作者实施时属Facebook AI Research | 共享潜空间：人脸表达映射为机器人动作 | [原始记录](https://msgtn.io/assets/pdf/thri-fg.pdf) |
| W013 | 2025 | 公开 2025-03-21；正式/文献日期 2025-10 | robot | HAPI；RIKEN × Kyoto University × NII 合作 — Dongsheng Yang / Wataru Sato 等 | 成对人类偏好与优化校准实体面部表达 | [原始记录](https://arxiv.org/abs/2503.17046) |
| W039 | 2025 | 公开 2025-05-16；正式/文献日期 2025-08 | robot | Laban Shape；University of Colorado Boulder — Srikrishna Bangalore Raghu / Bradley Hayes / Alessandro Roncone 等 | Laban Effort＋Shape：机械臂情感与功能表达 | [原始记录](https://arxiv.org/abs/2505.11716) |
| W041 | 2025 | 公开 2025-08-12；正式/文献日期 2025 | robot | Honda 情绪条件flow；Honda Research Institute Europe — Chao Wang / Michael Gienger / Fan Zhang | 专家MR示范→情绪条件flow生成 | [原始记录](https://www.honda-ri.de/publications/publications/?pubid=6361) |
| W009 | 2026 | 公开 2026-08-28；正式版本本轮未核 | embodied | PAMoR；University College London — Yan Pan / Lingfan Bao / Tianhu Peng / Chengxu Zhou | 机器人原生运动学VA＋动作条件：实时全身生成 | [原始记录](https://arxiv.org/abs/2608.28213) |
| W010 | 2026 | 公开 2026-09-27；正式版本本轮未核 | embodied | SocialHumanoid；Shanghai Jiao Tong University × ZTE — Chengqun Yang / Xiaokang Yang / Yichao Yan 等 | 情感条件共语生成→在线重定向→全身控制 | [原始记录](https://arxiv.org/abs/2609.33311) |
| W034 | 2026 | 公开 2026-10-19；正式版本本轮未核 | embodied | RoboMMT；University of Stuttgart SIR — Till Hielscher / Kai O. Arras | 表达调制、稳定跟踪与空间互动耦合 | [原始记录](https://arxiv.org/abs/2610.26414) |
| W076 | 2026 | 公开 2026-10-14；正式版本本轮未核 | embodied | Beyond Kinematic Tracking；University College London 合作 — Lingfan Bao / Chengxu Zhou 等 | 物理执行中补偿动态与姿态表达特征 | [原始记录](https://arxiv.org/abs/2610.19393) |

## 图面精选与细节安排

25条数据是可检索底稿，图面可以精简到12—18个节点，保证作品、机构和年份可读。若最多展示15个，可先用数据中的 `recommended_visual_ids`，并将DDPM、Laban任务约束、Face2Gesture、HAPI、Honda flow、Beyond/RoboMMT作为第二层或旁注。

若图希望强调“情感参数共同驱动动作”的技术演进，优先保留 **Shimi→MoveAE／Target VA-CVAE→Functional Expressive Motion→PAMoR** 这组对比，但连线标题应为“参数化、表示与控制的不同研究方向”，不称一条证明过的直接师承链。SocialHumanoid与PAMoR并列：前者是情感条件共语与在线重定向，后者是机器人原生运动学VA和动作条件组合，不将二者条件接口等同。

## 与既有闭环图的连接

时间图回答“不同能力和思路何时出现”，闭环图回答“这些工作研究交互的哪个部分”。两者互补。可以给时间节点加小型①②③A③B④⑤符号，但不强行让每篇包含所有环节：

- Kismet、Shimi支持早期感知—回应耦合，而不是证明持续学习已普遍解决。
- MoveAE、Target VA-CVAE、PAMoR主要连接③A；前两者足以否定“第一次把量化情感条件加入动作”的宽泛主张。
- Functional Expressive Motion同时提醒③A、任务约束和④人类感知模型已有方法先行，但实证是仿真，不能写实体Cassie验证。
- Beyond Kinematic Tracking、RoboMMT连接③B。运动跟踪和运动学表达特征保持，不自动意味着人的情绪解读保持。
- HAPI连接④/⑤，展示人类偏好校准；其平台为面部，不能写全身策略学习。
- GenEM、EMOTION连接生成与反馈修订，但语言纠正/离线修订并非人的实时情绪估计到策略优化闭环。

## 本轮纠正与未确定项

1. **GenEM机构更正：** 原稿首页仅署Google DeepMind和Hoku Labs。Mahadevan使用toronto.edu邮箱不能据此将多伦多大学列为该篇论文署名合作机构；旧总图或旧表中的Toronto应在新版本校正。[原论文首页](https://arxiv.org/pdf/2401.14673)。
2. **2019 Laban作者与机构：** 第一作者为Hang Cui；Catherine Maguire署独立舞者、Laban/Bartenieff Institute和McGuffey，不能将全体作者挂在UIUC。[原论文](https://pdfs.semanticscholar.org/c041/5780cd983df77654f2a2abf09944752f3b35.pdf)、[Illinois机构记录](https://experts.illinois.edu/en/publications/laban-inspired-task-constrained-variable-motion-generation-on-exp)。
3. **Functional Expressive Motion：** 原始arXiv为2022-03-04；Berkeley技术报告为2022-05-09，后者不能替代前者当最早公开日期。[arXiv记录](https://arxiv.org/abs/2203.02091)。
4. **Face2Gesture：** 原稿首页为2024年8月，部分实施时机构与发表时机构不同；timeline保留该区别，不能概括成Cornell独立研究。[作者原稿](https://msgtn.io/assets/pdf/thri-fg.pdf)。
5. **HAPI正式会议：** 理研托管原作者报告确认IROS2025（10月19—25日），本轮不补写冲突的页码记录。[原作者报告](https://grp.riken.jp/events/20251120-report/Prof.Nishida.pdf)。
6. **Honda flow：** 2025预印题名与机构正式论文题名有差异，2026修订也不是新研究起始点。正式摘要含人评；具体平台证据和旧版不能混写。[机构论文记录](https://www.honda-ri.de/publications/publications/?pubid=6361)、[原预印本记录](https://arxiv.org/abs/2508.08999)。
7. **Target VA-CVAE：** 2020 HRI LBR由作者实验室发表清单确认，原稿Google Drive链接本轮正文解析受限；完整当年机构脚注仍待补核。2022扩展稿已确认2022-05-02，不与2020工作重复计独立突破。[作者实验室](https://www.rosielab.ca/projects)、[2022扩展稿](https://arxiv.org/abs/2205.00763)。
8. **EMOTION正式月份：** Apple网页标2025年1月，期刊记录年份为2025，二者页面时间不能直接推作IEEE精确在线出版日。本图以“2024首公开→2025正式”足够。[Apple机构页](https://machinelearning.apple.com/research/emotion-expressive-motion)。
9. **Picard著作版本：** 精装首版为1997-09-24，平装2000不是首次出版年；1997书节点也不否认1995同名技术报告。[MIT Press](https://mitpress.mit.edu/9780262161701/affective-computing/)。

本轮进行了原始页面、论文首页、作者/机构记录的定向年份核验；没有复现方法，也没有将一张选择性时间图作为全领域研究数量、成熟度或机构排名证据。

## 时间图首版图面核验补记

已查看生成的英文时间图初稿。年代与W/H编号未发现新的硬错；GenEM机构已经写为DeepMind×Hoku。颜色分类需定向纠正三处：Kismet（2000）归机器人表达带、Face2Gesture（2024）归机器人表达带、Picard《Affective Computing》（1997）归AI/学科背景带。若增加机构，2019任务约束Laban可写UIUC × dance collaborators；Target VA-CVAE可写SFU ROSIE collaboration。

背景条额外标出的 **2022 ChatGPT** 已核为2022-11-30的研究预览发布，属于OpenAI方法/产品背景，不是机器人情感论文，来源：[OpenAI原始发布页](https://openai.com/index/chatgpt/)。该补充放入JSON的 `supplementary_background`，不改变25条文献节点的编号和计数。
