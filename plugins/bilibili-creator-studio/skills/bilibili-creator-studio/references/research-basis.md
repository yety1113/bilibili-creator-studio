# 设计依据与来源记录

访问日期：2026-09-19。

本文件记录 Skill 设计时采用的公开依据。它不是永久不变的平台规则；使用 Skill 执行当前趋势或合规任务时仍需重新核验。

## B站官方及官方账号

- [创作灵感功能介绍](https://www.bilibili.com/opus/609910734998525262)：说明站内创作灵感会汇集近期热门选题、优质作品、未来事件和创作模板。由此采用“站内信号 + 竞品样本 + 创作计划”的选题调研路径，但不把热度等同于适合某位创作者。
- [优质UP主分享：小鹿道长](https://www.bilibili.com/opus/740129401971146840)：官方扶持计划案例强调从创作者擅长领域切入、先定时长与字数、筛选素材顺序、安排情绪变化。案例经验只作为启发，不升级为全平台定律。
- [手机端创作学院介绍](https://www.bilibili.com/opus/178758119409743235)：官方课程体系覆盖取材创意、拍摄、制作和个人运营，支持将 Skill 做成从创意到运营的闭环，而不是单一大纲生成器。
- [花火稿件审核规范总则](https://www.bilibili.com/blackboard/activity-hp6i7WQHrx.html)：商业内容需避免夸大、虚假、侵权及不当诱导，并在特定品类提供相应材料。Skill 因此对商业及高风险内容设置实时规则核验和披露门禁。
- [包月充电专属视频创作公约](https://www.bilibili.com/blackboard/activity-Zwl3skTcLf.html)：强调题文相符、真实性、科学性与内容专业性。Skill 将包装承诺一致和事实核验设为 P0/P1 门禁。

## 平台官方创作者资料（可迁移原则）

- [YouTube：理解推荐系统中的内容表现](https://support.google.com/youtube/answer/16559650)：官方建议识别核心与潜在受众，让标题/封面清楚传达价值，开头兑现包装承诺，并通过实际留存反复实验结构与表达。这里采用的是可迁移的观众体验原则，不声称 B站算法相同。
- [YouTube：关键留存时刻](https://support.google.com/youtube/answer/9314415)：解释平段、渐降、峰值、低谷和前 30 秒留存的含义，也提醒峰值可能来自重看或不理解。Skill 因此要求基于实际曲线复盘，不把单一指标神化。

## 开源 Skill 与工作流样本

- [HeyGen 官方视频 Skill](https://github.com/heygen-com/skills/blob/master/heygen-video/SKILL.md)：将用途、受众、时长、语气、素材、关键信息、视觉风格和语言分开采集，并在生成前展示全文、字数和预计时长供用户确认。采用了“先确认脚本，再进入昂贵阶段”的门禁。
- [creator-futures：scripting-and-storyboarding](https://github.com/creator-futures/social-media-skills/blob/main/skills/scripting-and-storyboarding/SKILL.md)：强调双栏音画脚本、按场景组织拍摄、纸面剪辑、时长验证和不把摆拍伪装成抓拍。采用了可拍性与真实性检查。
- [skind-skills：educational-video-creator](https://github.com/skindhu/skind-skills/blob/main/skills/educational-video-creator/SKILL.md)：把完整逐字稿与分镜设计拆成不同阶段，并要求脚本获批后再做视觉设计。采用了“内容决策先于视觉规格”的工作顺序。
- [45ck/content-machine](https://github.com/45ck/content-machine)：强调脚本、音频、时间戳、视觉、字幕、来源权利和审核等中间产物可检查。采用了文件化交付与可追溯设计。

## 从来源得出的边界

- 未找到可信依据支持原 Skill 中“每 3 分钟必须高潮”“每条至少 3 个弹幕点”“某分区固定最佳时长”等普遍法则，故全部降级为按题材、受众、素材与历史数据决定的可测试假设。
- 开源项目的字速、画面切换频率等经验值依语言、表演者和内容而变，只用于粗估；最终以用户桌读和实际剪辑为准。
- 传播效率定义为“用有限制作成本持续提高合适受众的点击、理解、观看与关系”，不等于追逐最大播放量，也不保证爆款。
