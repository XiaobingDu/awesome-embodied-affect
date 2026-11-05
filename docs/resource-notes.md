# 人体与数字人邻近资源

核验日期：2026-11-05。这三项为综述提供数据、表征与生成方法支撑，使用独立R编号；不并入或复用W001–W080，也不把数字人实验作为机器人实体能力证明。

| 编号／资源 | 正式发表与首发 | 论文／项目／实现 | 在本综述中的作用 |
|---|---|---|---|
| R001 · **BEAT** | ECCV 2022；发表2022；首发2022-03-10 | [论文](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136670605.pdf) · [作者项目](https://pantomatrix.github.io/BEAT/) · [代码](https://github.com/beat2022dataset/beat) | 人体情感共语数据集与CaMN基线 |
| R002 · **EMAGE / BEAT2** | IEEE/CVF CVPR 2024；发表2024；首发2023-12-31 | [论文](https://openaccess.thecvf.com/content/CVPR2024/papers/Liu_EMAGE_Towards_Unified_Holistic_Co-Speech_Gesture_Generation_via_Expressive_Masked_CVPR_2024_paper.pdf) · [作者项目](https://pantomatrix.github.io/EMAGE/) · [代码](https://github.com/haiyangliu0/character-policy) | 数字人全身共语生成方法与BEAT2身体／面部数据 |
| R003 · **EmoDiffGes** | Computer Graphics Forum 44(7):e70261 / Pacific Graphics 2025；发表2025-10-11；首发更早首发未确认 | [论文](https://doi.org/10.1111/cgf.70261) · [作者论文展示页](https://ripemangobox.github.io/)（独立项目站未确认） · [代码](https://github.com/HellAngel18/EmoDiffGes) | 数字人情感条件共语全身生成方法 |

**BEAT的会议信息应写ECCV 2022，不能写CVPR 2022。** 作者项目与正式ECCV论文一致；arXiv首发为2022-03-10。[作者项目](https://pantomatrix.github.io/BEAT/)、[ECCV原论文](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136670605.pdf)、[首发记录](https://arxiv.org/abs/2203.05297)

## R001 · BEAT

机构：The University of Tokyo；Keio University；Huawei Digital Human Lab／Huawei Turkey R&D；Japan Advanced Institute of Science and Technology。作者：Haiyang Liu、Zihao Zhu、Naoya Iwamoto、Yichen Peng、Zhengqing Li、You Zhou、Elif Bozkurt、Bo Zheng。

- **问题：**缺少同步语音、身体、表情与情绪／语义标注的共语数据。
- **方法：**动作捕捉配合面部blendshape、音频、文本及情绪／语义标注，并提供级联运动网络CaMN。
- **贡献：**将多模态数据与情感和语义关联用于人体手势研究。
- **成果：**正式论文报告76小时、30位说话者、八类情绪及四种语言；提供数据与基线入口。
- **边界：**人体数据与生成基线，不代表机器人实体执行；版本与子集须注明，不能把各版时长和语言分布混用。

**代码状态：**已核官方PantoMatrix/BEAT README链接的原匿名提交代码，包含CaMN训练／推理和预处理；历史入口顶层现主要为README与docs；新整合库另列，未运行复现。

[PantoMatrix/BEAT](https://github.com/PantoMatrix/BEAT)为官方历史入口，当前顶层主要为README/docs；其README明确链接的[原提交实现](https://github.com/beat2022dataset/beat)仍包含CaMN训练／推理及预处理。维护后的[整合代码库](https://github.com/haiyangliu0/character-policy)提供另一个入口，应注明版本。

## R002 · EMAGE / BEAT2

机构：The University of Tokyo；Keio University；Max Planck Institute for Intelligent Systems；Japan Advanced Institute of Science and Technology；Tsinghua University；其他作者归属以论文对应版本为准。作者：Haiyang Liu、Zihao Zhu、Giorgio Becherini、Yichen Peng、Mingyang Su、You Zhou、Xuefei Zhe、Naoya Iwamoto、Bo Zheng、Michael J. Black。

- **问题：**如何统一生成面部、身体、手与全局运动并接受部分运动提示？
- **方法：**Masked Audio Gesture Transformer联合音频生成与遮罩重建，组合VQ-VAE分别建模身体区域；BEAT2结合SMPL-X与FLAME参数。
- **贡献：**全身多区域生成与可见运动提示统一，附标准化身体／脸网格数据。
- **成果：**论文报告共语生成与可控补全实验，作者公开模型、数据及工具入口。
- **边界：**输出数字人动作参数，不是实体机器人控制；BEAT2不是独立机器人数据集，不能把原版模型与维护后audio-only等变体混为同一设置。

**代码状态：**旧官方仓库地址本轮重定向到character-policy，作者EMAGE项目Code按钮也指向该库的EMAGE训练入口；新整合库不默认等于CVPR原始实验的全部配置，未运行复现。

[旧PantoMatrix/PantoMatrix地址](https://github.com/PantoMatrix/PantoMatrix)当前重定向到[character-policy](https://github.com/haiyangliu0/character-policy)；作者项目的Code按钮指向其中[EMAGE训练入口](https://github.com/haiyangliu0/character-policy/blob/main/train_emage_audio.py)。BEAT2随EMAGE提供，不重复计成另一篇方法论文。[CVPR论文](https://openaccess.thecvf.com/content/CVPR2024/papers/Liu_EMAGE_Towards_Unified_Holistic_Co-Speech_Gesture_Generation_via_Expressive_Masked_CVPR_2024_paper.pdf)、[arXiv首发](https://arxiv.org/abs/2401.00374)

## R003 · EmoDiffGes

机构：华东师范大学计算机科学与技术学院。作者：Xinru Li、Jingzhong Lin、Bohao Zhang、Yuanyuan Qi、Changbo Wang、Gaoqi He。

- **问题：**共语运动忽略情绪时间变化，身体分区建模又易失去协同。
- **方法：**动态情绪对齐模块DEAM提供情绪引导；渐进协同手势生成器在身体区域先验下迭代细化区域潜码并交换上下文。
- **贡献：**结合动态情绪条件和分区协同的扩散生成。
- **成果：**正式论文报告表达性、协调性与情绪相关实验；公开RVQ-VAE和扩散模型的训练／评估入口。
- **边界：**属于人体／数字人运动生成，不能据标题中的embodied emotion theory认定已解决实体机器人驱动、平衡与接触；Inter-Region Synergistic Flow名称不代表它是flow-matching模型。

**代码状态：**已核合作者主页明确链接的公开仓库，包含训练、测试、demo与模型下载说明；未运行或核验全部外部权重可下载。

Wiley页面明确First published为**2025-10-11**；[合作者主页](https://ripemangobox.github.io/)将它列为PG2025并直接链接[公开仓库](https://github.com/HellAngel18/EmoDiffGes)。机构按Wiley署名为华东师范大学，不泛化为未核的多机构合作。[出版社记录](https://onlinelibrary.wiley.com/doi/10.1111/cgf.70261)、[Eurographics记录](https://diglib.eg.org/items/880901e6-3e61-428f-93cd-34354b9a450d)

代码存在不等于本轮复现成功；数据和人体模型的许可、原论文版本与维护后实现需要分别记录。对机器人综述而言，应继续研究这些人体先验经过重定向、实体控制和任务约束后，表达是否仍能被人准确理解。
