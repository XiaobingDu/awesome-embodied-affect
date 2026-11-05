# Awesome Embodied Affect 🤖

**具身情感计算综述：感知、理解、生成与表达、反馈、适应。**

A curated survey of embodied affective computing, with a focus on affect-conditioned motion generation and physical realization in humanoid robots.

**80 项相关工作 · 五阶段闭环 · 六个技术模块 · 人体基础与数字人参考**

[研究动机](#overview) · [分类体系](#taxonomy) · [研究总览](#figures) · [方法详解](#core-methods) · [横向对比](#comparison) · [完整文献](#catalog) · [核心洞察](#insights)

### 图1：人与具身智能体的情感交互闭环

![Interaction loop](./assets/overview-v3.2-en-public.png)

*图1．具身情感计算的交互闭环与研究框架。具身智能体感知人的情感，结合交互情境确定回应目标，生成带有目标情感的动作，并在身体与任务约束下执行；人的解读与反馈进一步影响后续行为的修正与适应。情感条件化动作生成与实体执行共同连接表达意图和实际行为，机器人表达、人体身体语言及数字人动作研究为这一过程提供理论、方法与数据支撑。*

<a id="overview"></a>
## 📌 为什么要研究具身情感（Embodied Affect）？

同样是递出一本书，动作的速度、幅度、身体展开、朝向和停顿，可能让人感受到不同的态度。人在与机器人交互时，会同时解读**机器人做了什么、以怎样的方式做、是否注意到自己的反应**。具身情感研究关注如何把这些表达因素纳入机器人的感知、决策与运动，使任务行为与社会互动相互配合。

本综述的核心问题是：**能否把情感或社会表达转化为可调节的条件，与动作内容共同驱动实体机器人，并在执行后保留人能够理解的表达？** 这需要连接情感表示、动作生成、身体约束和人的评价。LLM／VLM提供语境理解与行为编排接口。潜变量模型、扩散模型和基于流匹配的生成模型用于合成动作；控制策略负责将参考动作落实为满足身体与任务约束的实际运动。

| 研究动机 | 需要回答的问题 | 代表入口 |
|---|---|---|
| 让动作携带可理解的表达 | 同一个任务能否表现出平静、活跃或关切？ | [MoveAE](https://msgtn.io/assets/pdf/hri20-moveae.pdf)、[Laban Shape](#w039) |
| 把表达变成可控条件 | 情感条件与动作内容如何分别调节？ | [PAMoR](#w009)、[Honda 情绪条件生成](#w041) |
| 将语境和语义落到身体 | 语言意图怎样变为当前机器人可执行的行为？ | [GenEM](#w001)、[EMOTION](#w002)、[EmoPose](#w008) |
| 在实体执行中保持表达 | 平衡、接触和任务约束介入后，表达还剩下什么？ | [Beyond Kinematic Tracking](#w076)、[RoboMMT](#w034) |
| 让人的解读参与改进 | 人是否读懂、是否喜欢，系统又怎样根据反馈调整？ | [VITA](#w020)、[HAPI](#w013) |

### 代表作导读：从情感表示到实体表达

以下工作按时间串起本综述的主要问题。选取依据是对**情感表示、可控生成、实体实现或人类验证**的代表性贡献；完整目录仍保留全部 W001–W080。日期区分首公开与正式发表。

> **1980 · 英属哥伦比亚大学 · JPSP**
>
> **[H002 · A Circumplex Model of Affect](https://pdodds.w3.uvm.edu/research/papers/others/1980/russell1980a.pdf)**  
> **James A. Russell**
>
> 以效价和唤醒度组织情感空间，为连续条件提供理论参照。机器人运动学定义的 VA 代理仍需要人的感知校准。

> **1997 · MIT Media Lab · MIT Press**
>
> **[H014 · Affective Computing](https://mitpress.mit.edu/9780262161701/affective-computing/)**  
> **Rosalind W. Picard**
>
> 从计算系统如何处理情感出发，为情感感知、建模与表达提供领域背景；本综述进一步聚焦这些能力如何与实体身体和互动结合。

> **2000 · MIT · 博士论文**
>
> **[H005 · Sociable Machines / Kismet](https://groups.csail.mit.edu/lbr/hrg/2000/phd.pdf)**  
> **Cynthia L. Breazeal**
>
> 将感知、内部状态和社会表达放入人机互动，提供理解完整交互闭环的早期系统参照。

> **2020-03 · 康奈尔大学 × 本田日本研究所 · HRI 2020**
>
> **[H008 · MoveAE](https://msgtn.io/assets/pdf/hri20-moveae.pdf)**  
> **Michael Suguitan / Randy Gomez / Guy Hoffman**
>
> 用带分类约束的变分自编码器编辑机器人情感动作，展示从预设动作走向可编辑潜空间的一条方法路线。

> **2022-03 首公开 · 加州大学伯克利分校 · IROS 2022**
>
> **[H010 · Teaching Robots to Span the Space of Functional Expressive Motion](https://arxiv.org/abs/2203.02091)**  
> **Arjun Sripathy / Andreea Bobu / Anca D. Dragan 等**
>
> 学习人的表达感知并联合考虑任务与表达目标，为“动作正确且表达可控”提供优化视角；机器人与用户研究基于仿真。

> **2024-01 首公开 · Google DeepMind × Hoku Labs · HRI 2024**
>
> **[W001 · GenEM](#w001)**  
> **Karthik Mahadevan / Leila Takayama / Dorsa Sadigh 等**
>
> 将社会意图转为机器人技能 API 的参数化代码，并通过语言反馈修订，连接语境推理、行为组合和当次纠正。

> **2024-10 首公开 · Apple · IEEE RA-L 2025**
>
> **[W002 · EMOTION](#w002)**  
> **Peide Huang / Yuhan Hu 等**
>
> 通过上下文学习生成手部运动序列，再以逆运动学与插值执行；反馈版本进一步调整自然性和可理解性。

> **2025-03 首公开 · 理化学研究所 × 京都大学 × NII · IROS 2025**
>
> **[W013 · HAPI](#w013)**  
> **Dongsheng Yang / Wataru Sato 等**
>
> 用成对人类偏好学习表情评价，再优化机器人面部参数，为“由人来校准表达”提供参考；研究对象为面部。

> **2025-08 首公开 · 本田欧洲研究所 · RO-MAN 2025**
>
> **[W041 · Autonomous Generation of Real-time Robotic Emotional Expressions](#w041)**  
> **Chao Wang / Michael Gienger / Fan Zhang**
>
> 将混合现实示范、离散情绪条件和 flow matching 连接起来，学习头、手与脸的实时表达片段。

> **2026-08 · 伦敦大学学院 UCL · 预印本**
>
> **[W009 · PAMoR](#w009)**  
> **Yan Pan / Lingfan Bao / Tianhu Peng / Chengxu Zhou**
>
> 组合动作与连续运动学 VA 先验，滚动生成机器人原生全身运动，并报告 G1 实体执行和人感知研究。它是本综述研究“情感条件与动作共同驱动”的重点入口。

> **2026-09 · 上海交通大学 × 中兴通讯 · 预印本**
>
> **[W010 · SocialHumanoid](#w010)**  
> **Chengqun Yang / Xiaokang Yang / Yichao Yan 等**
>
> 用音频和情绪条件驱动单步共语动作生成，再连接在线重定向与全身跟踪，重点处理持续表达的生成时延。

> **2026-10 · 伦敦大学学院 UCL · 预印本**
>
> **[W076 · Beyond Kinematic Tracking](#w076)**  
> **Lingfan Bao / Chengxu Zhou 等**
>
> 在全身跟踪后补偿运动幅度、能量和姿态等表达特征，将关注点延伸到“实际执行保留了什么”；人的情感意义保持仍待验证。

> **2026-10 · 斯图加特大学 SIR · 预印本**
>
> **[W034 · RoboMMT](#w034)**  
> **Till Hielscher / Kai O. Arras**
>
> 将调制表达参考、稳定跟踪与互动目标连接，研究大幅调制下的身体实现。实体迁移证据为四足，人形评估主要在仿真中。

<a id="scope"></a>
<a id="taxonomy"></a>
## 🗂️ 分类体系：五阶段、六个技术模块

本综述以**实体人形机器人**为核心，比较面部、头部、机械臂、四足和桌面机器人；人体身体语言、心理与表演理论、数字人和动作数据作为理论、方法与资源支撑。

**① 感知 → ② 理解与决策 → ③A 情感条件化动作生成 → ③B 实体执行与任务约束 → ④ 人类解读与反馈 → ⑤ 修正与适应 → 下一轮交互。** 阶段③包含两个技术模块，其余四个阶段各包含一个模块。

| 技术模块 | 核心问题与输入／输出 | 代表工作 | 深入阅读 |
|---|---|---|---|
| ① 情感感知 | 从脸、语音、身体和触觉估计人的状态及不确定性 | UGotMe、EmArm、FER-to-motion | [模块解析与文献](#stage-1) |
| ② 情境理解与回应决策 | 结合任务、关系与环境，从人的状态确定机器人的回应目标 | Context-Aware、HIAER、MHE、SeM² | [模块解析与文献](#stage-2) |
| **③A 情感条件化动作生成** | 将动作内容、情感／社会意图和历史条件转为表达参考 | **PAMoR、EMOTION、SocialHumanoid、Honda flow** | [方法详解](#core-methods) · [完整条目](#stage-3a) |
| **③B 实体执行与任务约束** | 将参考运动变为满足身体、接触与任务条件的实际动作 | **Beyond Kinematic Tracking、RoboMMT、EmoLo** | [方法详解](#core-methods) · [完整条目](#stage-3b) |
| ④ 人类解读与反馈 | 测量人的感知、偏好、后续行为与多轮交互结果 | VITA、AffectLoop、Emotion Appropriateness | [模块解析与文献](#stage-4) |
| ⑤ 修正与适应 | 将纠正、偏好或后续反应转为当次调整与策略更新 | GenEM、HAPI、Proxy-based Optimization | [模块解析与文献](#stage-5) |

### 三类基础支撑

| 支撑方向 | 提供什么 | 与核心问题的连接 |
|---|---|---|
| [机器人身体与运动表达](#foundation-body)、[头部与面部表达](#foundation-face) | 可解释运动参数、形态设计、执行器映射、表达感知实验 | 为③A提供控制变量，为③B提供身体实现，为④提供评价依据 |
| [人体身体语言、心理与表演理论](#foundation-human) | 情感表示、动作线索、示范及知觉机制 | 支撑①识别、③A表达设计和④人的解读 |
| [数字人、动作表示与数据](#virtual-data) | 骨架／网格动画、情感标注、共语时序与生成模型 | 为③A提供方法和数据；迁移到实体时需处理身体、动力学与接触约束 |

### 交叉分类：读一篇论文时还要看什么？

| 分类维度 | 主要类别 | 阅读时关注 |
|---|---|---|
| 情感与表达的含义 | 狭义：离散情绪、连续 VA／VAD；广义：温暖、关切、生动、礼貌等社会表达 | 强度、唤醒度、人格和社会意图分别如何定义与测量？ |
| 身体与表达通道 | 面部／头部、机械臂、全身人形、其他机器人；身体、声音与脸的多模态组合 | 可用自由度、表达同步与跨形态迁移 |
| 生成与控制路线 | 规则／参数、库与插值、潜变量、扩散／flow、语言程序、控制／强化学习 | 情感进入了哪个环节，输出是意图、参考运动还是控制量？ |
| 证据类型 | 仿真／实体、录制／现场、单次／多次、离线优化／在线适应 | 实验对象、比较基线、人类验证和泛化范围 |

同一论文可以涉及多个模块。下文按主要研究问题安排主位置，保留交叉标签；机构与学者采用作品发表时的署名和合作信息。

<a id="figures"></a>
## 🧭 研究总览

### 图2：人体、机器人与具身情感表达的时间演进

![Evolution of embodied affect](./assets/embodied-affect-timeline-v2-all-works.png)

*图2．人体、机器人与具身情感表达的研究演进。沿时间轴与研究方向梳理情感表示、身体语言、机器人表达及具身交互的相关工作，并对照生成模型与大语言模型的发展背景，呈现从运动参数设计、学习式动作表示到情感条件生成、实体执行与反馈适应的研究脉络。各方向的论文与研究机构按时间并列呈现，展示基础研究与交互系统之间持续发展的联系。*

[SVG](assets/embodied-affect-timeline-v2-all-works.svg) · [PDF](assets/embodied-affect-timeline-v2-all-works.pdf) · [完整节点与来源](data/timeline-full-coverage-v2.json)

<a id="timeline"></a>
### 时间演进与 AI／LLM 的关系

| 时期 | 研究重心 | 对当前问题的支撑 |
|---|---|---|
| 1970s–2000s：人体与情感理论 | 生物运动知觉、情感维度、身体运动与情绪归因 | 运动线索、概念定义和人的评价 |
| 2000s–2010s：机器人表达与参数设计 | 互动调节、节奏／幅度／姿态、表演与任务约束 | 可解释表达参数和形态差异 |
| 2020–2022：学习表示与约束优化 | AE／CVAE、目标 VA、表达运动优化 | 可编辑生成、任务与表达联合优化 |
| 2023–2025：语言接口与多模态表达 | LLM程序／序列、VLM编排、情绪条件生成 | 将社会意图、场景和表达要求接入机器人行为 |
| 2026：连续条件与实体表达保持 | PAMoR、SocialHumanoid、RoboMMT与表达补偿 | 进一步连接可控生成、低延迟实现与执行后表达 |

[Transformer（2017）](https://arxiv.org/abs/1706.03762)、[DDPM（2020）](https://arxiv.org/abs/2006.11239)和[GPT-4（2023）](https://arxiv.org/abs/2303.08774)分别提供序列建模、生成建模和语言接口的方法背景。具体论文的依赖关系需逐项判断；机器人表达与人体情感研究有自身的长期积累。

