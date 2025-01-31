快速了解AIGC🚀（营销号洗脑文）
---

## AIGC的历史和发展

提出：1956，由约翰·麦卡锡（John McCarthy）在达特茅斯会议上提出，是一种模拟人类智能的研究方法。

20世纪70年代：专家系统

1997：IBM的深蓝战胜国际象棋世界冠军卡斯帕罗夫

2010：快速发展，大数据、云计算、深度学习、GPU、TPU等技术的发展

2022：OpenAI的ChatGPT

### AIGC的布局
#### Microsoft
- 投资OpenAI
- Copilot（融合式）
- Azure

#### Google
- DeepMind
- Google Cloud AI
- 投资Anthropic
> ChatGPT对搜索引擎的威胁

#### Meta(原Facebook)
- Llama
- SAM（Segment anything model）

#### 其他国外AI大模型
| 公司 | AI模型名称 |
|------|------------|
| Amazon | AMS |
| X(原Twitter) | Grok |

#### 国内AI大模型
| 公司 | AI模型名称 |
|------|------------|
| 百度 | 文心一言 |
| 阿里巴巴 | 通义千问 |
| 腾讯 | 混元大模型 |
| 字节跳动 | 豆包 |

### OpenAI
- 加州，Samuel Altman, Elon Musk
- 融资

产品：
- ChatGPT
- DALL·E（图像生成）
- Whisper（语音识别）
- Codex（Github Copilot）
- OpenAI API

### DeepMind
- 英国，Demis Hassabis，被Google收购

产品：
- AlphaGo
- Gemini
- AlphaFold（蛋白质结构预测）
- Google AI API

### Anthropic
- 前OpenAI高管Dario Amodei
- 获得Google和Amazon的投资

产品：Claude

### Nvidia
- CUDA生态
- H100 GPU

> 为什么要关注AIGC？因为全世界最聪明的人和最有钱的人都在这么干。🥺

## AIGC相关技术介绍
### Transformer路线
规则系统 → 变分自编码器 → GAN及其变种 → Transformer → BERT及其它基于编码器的模型 → GPT及其它基于解码器的模型 → ChatGPT → UL2？

> *注释*
>
> **规则系统**：人工指定规则，约束随机的内容生成，已被淘汰
>
> **变分自编码器**：相比于仅仅是压缩图像的自编码器，变分自编码器可以学习数据的分布，从而生成新的图像
>
> **CGAN**:(Conditional GAN)：可以输入条件信息，让生成更加可控
>
> **WGAN**:(Wasserstein GAN)：解决了训练不稳定的问题
>
> **CycleGAN**: 图像→图像，风格迁移
>
> **BERT**：双向编码器表示转换，对于文本的理解比GPT更好
>
> **GPT**：单向解码器，适合生成文本，可以few-shot或zero-shot学习，微调成本低，通用性强
>
> **ChatGPT**：加入了RLHF（Reward Learning from Human Feedback）的GPT，可以更好地与人类对话
> 
> **UL2**：未来的模型？混合训练（BERT+T5+GPT）同时适用于理解+生成任务

### 扩散模型路线
规则系统 → 变分自编码器 → GAN及其变种 → U-Net → Diffusion → Reverse Diffusion

> **扩散模型**：先让数据逐步变成噪声（前向扩散），再学会如何去噪（反向扩散）

- 前向扩散（Forward Diffusion）
给一张原始图片 $X_0$ 不断加入噪声，直到它变成纯高斯噪声 $X_T$

- 反向扩散（Reverse Diffusion）
训练一个 神经网络（U-Net） 来预测原始数据 X₀，并逐步去掉噪声。

应用：U-Net用于图像分割，Diffusion用于图像生成，Reverse Diffusion用于去噪，Whisper用于语音识别

### AIGC的界限？
- 模型能力（算例/性能优化）
- 数据质量（不能胡言乱语）
- 可控性（例如GAN不能精确引导生成的内容）
- 用户交互&生态（人机交互的优化）

## NLP领域的AIGC

### 发展路线
ai元年 → 机器翻译 → 发展停滞（1970-1980）→ 统计学习（1990）→语料库（2000）→ 深度学习（2010）→ Word2Vec → Seq2Seq → Attention → Transformer→BERT → GPT → ChatGPT

### NLP的应用
- 机器翻译
- 社交媒体文案
- 新闻和文学创作
- 剧本改写
- 出题和做题
- 代码生成：Github Copilot（Codex）
- 搜索引擎优化：Perplexity
- 聊天机器人：ChatGPT