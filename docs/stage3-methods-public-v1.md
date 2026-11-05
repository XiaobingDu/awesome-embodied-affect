# 第 3 环节：情感生成、表达与实体执行

更新：2026-11-05。本节围绕现有文献索引中的 3A 九项和 3B 八项主归类工作展开，并补充 GenEM、HAPI、Proxy-based Optimization 三项反馈／参数方法。主归类用于组织阅读，不是互斥能力分区。新近预印本、正式论文、工作坊和控制支撑方法保留各自证据身份；本节不据数量宣布领域主流或全球排名。

## 研究范式：做什么、以什么方式做、如何执行

目标是固定动作／任务内容，调节其表达方式，并使实际运动仍让人理解预期表达。统一接口可写为

\[
X^{\mathrm{ref}}_{t:t+H}=G_\theta(c_{\mathrm{action}},e_{\mathrm{target}},s_t,X_{<t}),\qquad
u_t=\pi_\phi(s_t,X^{\mathrm{ref}}_{t:t+H},c_{\mathrm{task}}).
\]

这是综述抽象，非任何一篇论文的原始公式。参考运动和实际控制量应分开；人的情绪估计、机器人的表达目标及观察者对结果的理解也是三个变量。

| 分析维度 | 可选内容 | 区分原则 |
|---|---|---|
| 条件表示 | 离散情绪、连续 VA、运动风格／Laban、强度、社会意图 | 强度不等于唤醒度；友好和犹豫不必硬映射为离散情绪 |
| 条件注入 | 库选择、参数调制、条件 token、FiLM、cross-attention、组合先验 | 情感可进入语义选择器、生成器或控制目标，位置不同 |
| 生成模型 | 规则／优化、库／插值、潜变量、扩散、flow／MeanFlow、LLM序列 | 潜空间可以同时用于扩散或flow；各类不是互斥路线 |
| 实体执行 | 重定向、IK、轨迹规划、全身跟踪、残差补偿、任务与接触约束 | 人体生成和机器人原生生成都可用，需同基准比较 |
| 人的验证 | 可识别性、强度可控、自然性、时机、适切性、任务效果 | 运动特征保持和人的情感意义保持须分别证明 |

数字人也以骨架／关节参数生成动作；实体机器人额外需要真实动力学、执行器、接触和任务约束。LLM生成数值关键帧、VLM选择动作库、扩散生成潜动作和RL产生控制量不能写成同一种“情感参数驱动”。

## 3A：生成与表达的九项主要工作

| ID／代表作 | 方法链 | 主要证据身份 |
|---|---|---|
| [W009 · PAMoR](https://arxiv.org/abs/2608.28213) | 连续运动学VA＋动作文本 → 可组合潜扩散 → 机器人原生运动 | 预印本；作者注明RA-L在审 |
| [W010 · SocialHumanoid](https://arxiv.org/abs/2609.33311) | 音频＋离散情绪 → RVQ潜空间MeanFlow → 重定向与全身控制 | 预印本 |
| [W041 · Honda emotion flow](https://www.honda-ri.de/publications/publications/?pubid=6361) | 离散情绪＋状态 → FiLM U-Net flow matching → 动作片段 | RO-MAN |
| [W008 · EmoPose](https://arxiv.org/abs/2609.23414) | VLM语义计划 → 库变体与强度 → 确定性轨迹 | 预印本 |
| [W002 · EMOTION](https://arxiv.org/abs/2410.23234) | 上下文学习／LLM数值序列 → IK与插值 | IEEE RA-L 2025；首次预印2024；DOI10.1109/LRA.2025.3575983 |
| [W003 · Alter3](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1581110/full) | 动作语义描述 → GPT-4控制程序 → 43轴执行 | Frontiers in Robotics and AI 2025；DOI10.3389/frobt.2025.1581110 |
| [W005 · PEPE](https://www.mdpi.com/2076-3417/15/23/12759) | 分层结构与情绪提示 → 离线运动代码 | Applied Sciences 15(23):12759 |
| [W031 · SLM text + gesture](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1581024/full) | 语言隐藏状态 → 机器人专属gesture head → 高层手势 | Frontiers in Robotics and AI |
| [W078 · Emotion Retargeting](https://www.honda-ri.de/publications/publications/?pubid=6782) | MR示范／跨部位映射 → 条件flow → 实时表达 | ICRA工作坊 |

### W009 · PAMoR

- **问题：**怎样独立控制动作内容和连续表达条件？
- **方法：**机器人运动学定义VA代理，动作、V、A先验在共享潜空间逐去噪步组合，滚动生成机器人原生运动。
- **贡献：**可组合条件扩散使动作与表达分别调节。
- **成果：**论文采用29自由度G1，报告实时全身执行与独立人感知研究；运动学VA可控性与人的识别是分别评价的结果。[正文方法与实验](https://arxiv.org/html/2608.28213v2)
- **边界：**代理VA不等于心理VA；不是人的实时反馈学习，也不能把跨论文人类数字当同条件对照。

[论文／机构入口](https://arxiv.org/abs/2608.28213)。

阅读重点是动作与表达先验如何解耦、如何注入连续条件、滚动片段如何衔接。其有人的感知研究；缺口不是“无人评”，而是运动学代理与心理意义的进一步校准以及人的实时反馈学习。

### W010 · SocialHumanoid

- **问题：**如何低延迟持续生成带情绪的共语全身动作？
- **方法：**音频、情绪与说话者条件驱动分组RVQ潜空间的改进MeanFlow单步生成，历史衔接后在线重定向并全身跟踪。
- **贡献：**结合AffectMoCap情感监督、一次前向生成和实体部署链。
- **成果：**论文报告在BEAT2同一协议下较GestureLSM约6倍推理加速；另有生成表达识别及G1持续执行实验。这是生成器推理对照，不是端到端交互或全领域统一加速比。[原文摘要与实验](https://arxiv.org/html/2609.33311v1)
- **边界：**情绪标签不是连续VA；语音轮次循环不等于人的情感反馈优化。

[论文／机构入口](https://arxiv.org/abs/2609.33311)。

### W041 · Honda emotion flow

- **问题：**怎样从MR专家示范学习实时情绪表达？
- **方法：**七类情绪one-hot与机器人和目标物体状态，经FiLM条件U-Net flow matching预测头、手及脸的动作片段。
- **贡献：**示范映射与情绪条件生成相连接。
- **成果：**正式机构记录报告识别表现接近专家遥操作；早期预印本仅初步定性评估。
- **边界：**旧稿与正式记录有版本差异；非连续VA，也不据此声称实体双足全身验证。

[论文／机构入口](https://www.honda-ri.de/publications/publications/?pubid=6361)。

方法细节依据[早期预印本](https://arxiv.org/html/2508.08999v1)，正式人评结论依据机构记录；两者不可混写成同一版本的完整实验。

### W008 · EmoPose

- **问题：**开放语义如何可靠落到特定身体的表达手势？
- **方法：**VLM输出类别、库变体、五级强度、语音锚点；本地确定性模块生成14自由度上肢轨迹。
- **贡献：**显式划分语义选择与数值关节控制权。
- **成果：**实体G1实现29种库变体；160次完成指MuJoCo仿真试验，不是160次实体／真人交互。[项目结果](https://daojiepeng.github.io/EmoPose/)
- **边界：**不是自由连续全身生成；英语基准与固定导览场景限制外推，官方代码链接当前404。

[论文／机构入口](https://arxiv.org/abs/2609.23414)。

### W002 · EMOTION

- **问题：**怎样用少量示范生成自然且可理解的人形手势？
- **方法：**VLM选择手势意图，LLM上下文学习生成双手位置、朝向与手指序列，IK和插值执行；EMOTION++接受自然语言修订。
- **贡献：**从少量示范生成数值运动序列并引入反馈。
- **成果：**GR-1上部署十类手势；在线视频研究支持反馈版本的自然性和可理解性改善。
- **边界：**十手势不是十情绪；研究者先仿真修订再录制，不是长期在线个体学习。

[论文／机构入口](https://arxiv.org/abs/2410.23234)。

### W003 · Alter3

- **问题：**语言描述怎样落到新的机器人身体上？
- **方法：**分两阶段把动作描述转为43轴Alter3的Python控制程序，允许语言调整。
- **贡献：**无需每项动作手工编码的具身语言接口。
- **成果：**展示自拍、幽灵等多种实体动作及口头修改。
- **边界：**首发2023、正式2025；不是双足全身行走策略，也不是连续VA生成。

[论文／机构入口](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1581110/full)。

### W005 · PEPE

- **问题：**仿动物机器人怎样低数据成本生成情感动作？
- **方法：**逐步提示提供猫形PEPE结构、关节角边界、代码格式及情绪原则，离线生成八类动作。
- **贡献：**将本体知识和情绪要求结构化输入代码生成过程。
- **成果：**15人现场以五点量表评分；原文总体印象均值3.0为中性，各动作评价不均，不能表述为整体高度认可。[正文第5节与结论](https://www.mdpi.com/2076-3417/15/23/12759)
- **边界：**未评在线情绪感知或长期交互；传感硬件存在不代表已纳入研究闭环。

[论文／机构入口](https://www.mdpi.com/2076-3417/15/23/12759)。

### W031 · SLM text + gesture

- **问题：**小语言模型如何同时生成文本和合法高层手势？
- **方法：**从语言隐藏状态训练机器人专属gesture head，与语言头并行输出受平台词汇约束的行为。
- **贡献：**较低开销修补小模型不合法手势与参数。
- **成果：**论文报告低额外计算开销并在Furhat、Pepper上演示。
- **边界：**未做人评；输出行为意图而非精确关节轨迹，较大模型输出只是代理真值。

[论文／机构入口](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1581024/full)。

### W078 · Emotion Retargeting

- **问题：**如何采集并实时复现跨部位机器人情绪行为？
- **方法：**通过MR头显采集专家第一人称遥操作，把脸、头、上身映射到眼、耳、颈和臂；flow matching按情绪与环境刺激生成。
- **贡献：**将沉浸式示范采集、身体映射和情绪条件模型连接。
- **成果：**ICRA2026 Learning-HRI工作坊机构摘要描述虚拟及实体遥操作与实时生成链。
- **边界：**与W041同线续作，不自动算独立突破；机构摘要未给足细粒度人评或双足全身任务证据。

[论文／机构入口](https://www.honda-ri.de/publications/publications/?pubid=6782)。

## 3B：实体执行与任务约束的八项主要工作

| ID／代表作 | 方法链 | 主要证据身份 |
|---|---|---|
| [W076 · Beyond Kinematic Tracking](https://arxiv.org/abs/2610.19393) | 冻结全身跟踪器 → 运动感知门控残差 → 表达特征补偿 | 预印本Under Review |
| [W034 · RoboMMT](https://arxiv.org/abs/2610.26414) | 参数化表达参考 → RL稳定跟踪 → 互动目标调制 | 预印本，2026-10 |
| [W024 · ReSIn-HR](https://arxiv.org/abs/2601.17287) | 结构化运动库＋LLM描述 → 时长感知DTW → 关节校验 | 2026预印本 |
| [W035 · Operator Imitation](https://la.disneyresearch.com/publication/autonomous-human-robot-interaction-via-operator-imitation/) | 操作者数据 → 连续命令扩散＋离散分类 → 操作接口 | IROS |
| [W036 · AMOR](https://la.disneyresearch.com/publication/amor-adaptive-character-control-through-multi-objective-reinforcement-learning/) | 奖励权重条件 → 多目标RL → 动态角色控制 | SIGGRAPH 2025；控制邻近 |
| [W037 · Olaf](https://la.disneyresearch.com/publication/olaf-bringing-an-animated-character-to-life-in-the-physical-world/) | 动画参考 → RL＋机械／噪声／温度约束 → 实体角色 | IEEE RA-L 2026，机构记录 |
| [W046 · DFM](https://sony.github.io/DFM/) | 周期潜空间／Fourier运动表示 → RL跟踪与辅助任务 | ICRA 2025 |
| [W069 · EmoLo](https://mertcookimg.github.io/emolo/) | 三类风格one-hot → 姿态／活动奖励 → 单个RL行走策略 | RO-MAN |

### W076 · Beyond Kinematic Tracking

- **问题：**低平均跟踪误差为何仍可能丢失表达特征？
- **方法：**冻结跟踪器上叠加门控残差，按幅度、运动能量、展开、倾斜、骨盆高度补偿；动作教师策略蒸馏为统一策略。
- **贡献：**显式优化表达特征的执行后保持，而非只优化位置误差。
- **成果：**论文在八类动作上报告仿真与G1实体实验，支持动态和姿态描述子保持改善；不表示每个描述子在每个动作上都显著改善。[原文实验](https://arxiv.org/html/2610.19393v1)
- **边界：**运动学特征不是人的情感真值；尚不能把特征恢复称为人类情感意义恢复。

[论文／机构入口](https://arxiv.org/abs/2610.19393)。

### W034 · RoboMMT

- **问题：**表达参考在高调制幅度下如何保持动态稳定？
- **方法：**在广泛表达参数域训练参考跟踪策略，再以轻量互动策略调制目标吸引点。
- **贡献：**将表达合成、稳定跟踪与空间互动目标耦合。
- **成果：**论文在四足和两个人形模型上评价；实体sim-to-real及重扰动展示为四足。不能把三种平台都写成实体人形验证。[原文摘要与实验](https://arxiv.org/html/2610.26414v1)
- **边界：**两个人形主要仿真；不能写成全部实体人形验证或连续心理VA控制。

[论文／机构入口](https://arxiv.org/abs/2610.26414)。

### W024 · ReSIn-HR

- **问题：**情绪语音与身体动作如何同步并可执行？
- **方法：**结构化动作库约束LLM运动描述，以时长感知DTW对齐语音与关键帧，再进行可行性校验。
- **贡献：**将多通道时序与关节约束显式连接。
- **成果：**NAO框架报告优于规则基线的情绪对齐。
- **边界：**物理可行性反馈不是人的情绪反馈；性能受任务和评价协议限制。

[论文／机构入口](https://arxiv.org/abs/2601.17287)。

### W035 · Operator Imitation

- **问题：**如何从操作者社会经验学习自主角色互动？
- **方法：**统一Transformer用扩散预测连续操作命令、分类器预测离散命令，模仿不同mood交互。
- **贡献：**保留操作接口，把专家互动经验迁移到自主行为。
- **成果：**实体用户研究支持可辨mood与接近专家的简单互动，同操作接口实现另一平台迁移。
- **边界：**不是任意形态零样本迁移，也未建立人的情绪估计与连续VA闭环。

[论文／机构入口](https://la.disneyresearch.com/publication/autonomous-human-robot-interaction-via-operator-imitation/)。

### W036 · AMOR

- **问题：**角色控制中多个冲突目标如何避免反复重训？
- **方法：**多目标RL训练由奖励权重条件化的单策略，训练后调节权衡，高层策略可再选择权重。
- **贡献：**学习一组Pareto权衡而不是固定奖励组合。
- **成果：**机构记录展示动态角色运动及新任务适应。
- **边界：**奖励权重不是情绪坐标；是物理表达控制底座，不是情绪感知或反馈论文。

[论文／机构入口](https://la.disneyresearch.com/publication/amor-adaptive-character-control-through-multi-objective-reinforcement-learning/)。

### W037 · Olaf

- **问题：**夸张动画角色怎样在真实机械身体上保留风格？
- **方法：**动画参考引导RL，结合连杆机构、落地噪声及执行器温度约束。
- **贡献：**把角色造型、风格化控制与实体工程问题联合设计。
- **成果：**机构页报告仿真和实体Olaf实验。
- **边界：**动画风格不等于情绪参数生成；不能外推人类情绪理解或交互学习。

[论文／机构入口](https://la.disneyresearch.com/publication/olaf-bringing-an-animated-character-to-life-in-the-physical-world/)。

### W046 · DFM

- **问题：**舞蹈跟踪如何同时允许行走和注视任务？
- **方法：**艺术参考经周期自编码器形成运动潜表示，放松过强局部周期假设，RL同时跟踪舞蹈与辅助任务。
- **贡献：**连接可插值运动表示、平滑切换和多任务实体控制。
- **成果：**作者项目展示实体执行、较FLD更细致的跟踪及频率插值。
- **边界：**expressive dance不等于离散情绪或连续VA条件；项目模板仓库不是算法代码。

[论文／机构入口](https://sony.github.io/DFM/)。

### W069 · EmoLo

- **问题：**低成本双足行走如何同时带有可调表达风格？
- **方法：**单个RL策略接收Happy／Neutral／Sad的one-hot，头部俯仰和活动度奖励带门控，结合sim-to-real随机化。
- **贡献：**在共享行走策略中加入少量可解释风格控制。
- **成果：**Open Duck Mini V2固定向前行走试验中展示风格区分和实体部署。
- **边界：**主要评价行走完成和头部轨迹，尚不足以证明人的情绪识别或一般交互收益；不是连续VA。

[论文／机构入口](https://mertcookimg.github.io/emolo/)。

## 连接生成、评价与修正的三项补充

| 工作 | 可借鉴的方法 | 边界 |
|---|---|---|
| [GenEM W001](https://generative-expressive-motion.github.io/) | 语言意图到技能API代码，组合与语言纠正 | 广义社会表达；不含显式连续VA |
| [HAPI W013](https://arxiv.org/html/2503.17046v2) | 成对人类偏好→RankNet→贝叶斯优化 | 35自由度面部；不能直接外推全身；代码公开部分是标注器 |
| [Proxy-based Optimization W042](https://github.com/liamreneroy/LLM_vocab_optimization) | LLM准确度代理与参数／词汇集合优化 | 功能状态表达为主；代理分数需独立人评验证 |

## 第一阶段建议如何落地

1. 建立固定动作内容的动作库／显式参数基线，验证幅度、速度、节奏和展开的独立作用。
2. 以PAMoR式连续条件与内容／表达分离为核心，对比联合条件模型和组合先验；若是共语任务，再比较音频与情绪条件的单步生成。
3. 接现有可靠实体控制栈，单独研究任务约束、表达特征损失和补偿。机器人原生表示与人体生成＋重定向需同任务、平台和延迟协议比较。
4. 校准目标表达和人的实际理解：情绪／VA识别、强度单调性、适切性、自然性、时机、任务成功。控制语音、脸部、任务完成与新奇效应的混杂。
5. 在上述关系建立后，再增加人的反馈归因、单会话修正及跨会话偏好更新。不要先假定已能从一个微笑推断应如何改变全部关节。

语音、脸、头与全身的时间协调贯穿2的回应时机、3A的表达时间线、3B的执行延迟和中断、4的人感知以及5的策略修改。关节跟踪闭环、对话轮次循环、人的情感反馈优化应分别标明。

## 代码与资料状态（2026-11-05）

| 工作 | 核验结果 |
|---|---|
| PAMoR | 本轮打开官方论文及UCL主页，未确认公开算法代码；不猜测仓库 |
| SocialHumanoid | 原文确认[项目页](https://rex0191.github.io/SocialHumanoid/)，本轮页面不可访问；官方算法代码未确认 |
| EmoPose | [官方项目页](https://daojiepeng.github.io/EmoPose/)的Code按钮指向`https://github.com/DaojiePENG/EmoPose`，本轮404；记录候选链接，不当作已可下载实现 |
| EMOTION／GenEM／Honda flow | 本轮访问的一手页未确认官方算法代码；项目、附录、演示不自动视为代码 |
| HAPI | [PairwiseExpressionAnnotator](https://github.com/KUCognitiveInformaticsLab/PairwiseExpressionAnnotator)已确认，为成对标注实验代码，非全栈 |
| Proxy-based Optimization | [作者代码与资料](https://github.com/liamreneroy/LLM_vocab_optimization)已确认，包含优化、代理验证和用户研究／统计资料；未执行复现 |
| DFM／EmoLo／Disney三项 | 一手机构／作者页已核；未确认官方可下载算法实现，不能把网站模板或引用的控制基线称为本论文代码 |

“未确认”表示截至本轮核验的证据状态，不能写成确定未开源。正式发表日期、预印本首发日期和机构页日期分别记录于结构化数据；不把预印首发或会议日期偷偷当作出版社online日期。


## 数字与证据对象复查

本轮逐项复查了正文出现的自由度、动作数、样本数和加速比。数值直接保留作者原协议的对象，不跨研究拼排名；没有取得完整统计表时不补写效应量。最容易混淆的项目已明确如下：

| 量化陈述 | 对象和来源 | 可推出的范围 |
|---|---|---|
| PAMoR 29自由度 | [PAMoR III-A](https://arxiv.org/html/2608.28213v2)中的G1运动表示 | 平台与生成对象；不是29个独立表达通道 |
| SocialHumanoid约6倍 | [SocialHumanoid摘要及实验](https://arxiv.org/html/2609.33311v1)，BEAT2同协议相对GestureLSM推理 | 指定生成器对照；不是整个机器人闭环或任意硬件加速 |
| EmoPose 29种、160次 | [作者项目](https://daojiepeng.github.io/EmoPose/)中29种实体库变体、160次MuJoCo试验 | 实体与仿真两种证据分别报告，不合并为160次实体试验 |
| EMOTION十种 | [正文III–IV](https://arxiv.org/html/2410.23234v1)的社会手势集合与GR-1录制 | 十种手势，非十种情绪，也非十项成功率 |
| Alter3 43轴 | [正式正文2.1](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1581110/full)的气动身体 | 机械轴数，不是动态行走控制维度 |
| PEPE 15人、3.0 | [正文第5节](https://www.mdpi.com/2076-3417/15/23/12759)，五点现场适切性评分与总体印象 | 小样本主观评价；总体中性，非普遍高识别率 |
| Beyond Tracking八类动作 | [原文实验](https://arxiv.org/html/2610.19393v1) | 运动学描述子保持，非人的情感意义保持 |
| RoboMMT两个人形 | [原文](https://arxiv.org/html/2610.26414v1)的平台评估；实体零样本迁移为四足 | 人形评估不能笼统写成实体人形部署 |
| HAPI 35自由度 | [原文](https://arxiv.org/html/2503.17046v2)的Nikola面部平台 | 面部表达，不是全身；部分情绪改善不等于全情绪普遍领先 |
