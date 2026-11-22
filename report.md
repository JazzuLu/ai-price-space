# AI 聚合比价 · 数据报告

生成时间：2026-11-23T02:46:00+08:00 · 数据文件：`data.json`（同目录）
本报告所有数字均由 `data.json` 的 `items` 数组复算，复算方法见文末。
元数据校验：meta.total=62338 与 items 实际行数=62338 一致。

## 总览

- 报价总行数：**62338**
- 覆盖店铺数：**1680**（按 平台+店铺标识 去重）
- 分类数：**42**
- 厂商数：**26**
- 价格区间：¥0.01 ~ ¥99135
- 数据观察时间：AI价网 2026-11-19T18:27:39+08:00；BiWu 2026-11-19T18:28:10+08:00；水獭 2026-11-14T12:37:00+08:00（5 天前缓存，见口径说明）；PriceAI 2026-11-19T20:56:00+08:00；CardNav 2026-11-23T02:20:43+08:00

## 各源净增

| 来源 | 原始行数 | 并入行数 | 去重剔除 | 无效剔除 | 占位剔除 |
|---|---|---|---|---|---|
| 直抓 | 0 | 0 | 0 | 0 | 0 |
| AI价网 | 1843 | 1697 | 145 | 0 | 1 |
| BiWu | 5983 | 5937 | 44 | 2 | 0 |
| 水獭 | 20 | 20 | 0 | 0 | 0 |
| PriceAI | 325 | 302 | 14 | 9 | 0 |
| PriceAI | 325 | 44 | 272 | 9 | 0 |
| PriceAI | 325 | 9 | 307 | 9 | 0 |
| PriceAI | 325 | 48 | 268 | 9 | 0 |
| PriceAI | 325 | 9 | 307 | 9 | 0 |
| PriceAI | 325 | 46 | 274 | 5 | 0 |
| PriceAI | 325 | 59 | 261 | 5 | 0 |
| PriceAI | 325 | 52 | 269 | 4 | 0 |
| PriceAI | 325 | 20 | 300 | 5 | 0 |
| PriceAI | 325 | 47 | 273 | 5 | 0 |
| PriceAI | 324 | 36 | 283 | 5 | 0 |
| PriceAI | 324 | 28 | 291 | 5 | 0 |
| PriceAI | 324 | 16 | 304 | 4 | 0 |
| PriceAI | 324 | 27 | 293 | 4 | 0 |
| PriceAI | 324 | 40 | 280 | 4 | 0 |
| PriceAI | 324 | 45 | 275 | 4 | 0 |
| CardNav | 44497 | 29045 | 15322 | 87 | 0 |

- 去重键：平台 + 店铺标识 + 标题 + 价格（无商品标识时的 fallback）；冲突时保留观察时间最新的一行。
- PriceAI 14 条去重中，13 条以更新鲜的 PriceAI 行替换了同款旧行（BiWu 5、AI价网 8），1 条为快照内重复；PriceAI 行现存 315 行。9 条无效为 5 条 ¥0 价 + 4 条已过期报价。
- CardNav 1473 条去重为与现存行同款但观察时间更旧（未替换）；80 条无效为 76 条无价 + 4 条美元价（暂不换算）。
- 2026-11-19 21:39 另做一次 wzyp 店铺标识大小写归一（wurk0xwx 与 WURK0XWX 为同一家店），折叠重复行 300 条；各源并入行数之和 46896 与总行数 46596 之差即这 300 条。
- 直抓 0 行：wzyp / catfk 接口与店铺页均被阿里云 ESA 人机验证拦截，各只试一次，未硬试滑块。
- 无效剔除：BiWu 2 行价格为 ¥0（免费邀请码/免费接码号），无有效售价。
- 占位剔除：AI价网 Telegram 分类 1 行，价格 ¥9999、库存 9999，疑似商家占位价。
- AI价网原始 1843 行中有 145 行源内重复（同一店铺同一标题同一价格出现在多个分类）；BiWu 原始 5983 行中有 44 行与 AI价网重复或源内重复。

## 平台分布

| 平台 | 行数 | 占比 | 店铺数 |
|---|---|---|---|
| wzyp | 45320 | 72.7% | 967 |
| 16688 | 8094 | 13.0% | 312 |
| 自建站 | 6644 | 10.7% | 274 |
| 云猫 | 1723 | 2.8% | 95 |
| Kami | 434 | 0.7% | 11 |
| 独角数卡 | 103 | 0.2% | 6 |
| 未知 | 20 | 0.0% | 15 |

## 库存分布

| 状态 | 行数 | 占比 | 口径 |
|---|---|---|---|
| 有货 | 47899 | 76.8% | stock > 0（数字为件数；仅有有货标记的源记 1） |
| 缺货 | 14343 | 23.0% | stock = 0 |
| 库存未公开 | 96 | 0.2% | stock = -1 |

## 分类 Top 10

| 分类 | 行数 |
|---|---|
| ChatGPT Plus | 12197 |
| ChatGPT Team | 8680 |
| ChatGPT Pro | 6257 |
| 邮箱 | 5350 |
| 接码 | 5172 |
| 其他 | 3337 |
| Gemini Pro | 2887 |
| ChatGPT 账号 | 2060 |
| Muse AI | 1492 |
| Codex | 1143 |

## 厂商分布

category（产品线）保留，新增 vendor（厂商）字段：同品牌商品归到同一厂商下，非 AI 品类厂商即品类本身。

| 厂商 | 行数 | 占比 | 包含的产品线 |
|---|---|---|---|
| OpenAI | 30903 | 49.6% | ChatGPT Go / ChatGPT Plus / ChatGPT Pro / ChatGPT Team / ChatGPT 账号 / Codex |
| 邮箱 | 5350 | 8.6% | 邮箱 |
| 接码 | 5172 | 8.3% | 接码 |
| Google | 4900 | 7.9% | Gemini Plus / Gemini Pro / Gemini Ultra / Gemini 账号 |
| 其他 | 3337 | 5.4% | 其他 |
| Anthropic | 3182 | 5.1% | Claude Max 20x / Claude Max 5x / Claude Pro / Claude Team / Claude 账号 |
| xAI | 2835 | 4.5% | Grok Plus / Grok Premium / Grok Super / Grok Ultra / Grok 账号 |
| Muse AI | 1492 | 2.4% | Muse AI |
| 中转站 | 913 | 1.5% | 中转站 |
| Apple ID | 845 | 1.4% | Apple ID |
| KYC | 647 | 1.0% | KYC |
| Telegram | 523 | 0.8% | Telegram |
| Cursor | 462 | 0.7% | Cursor |
| 虚拟卡 | 397 | 0.6% | 虚拟卡 |
| TikTok | 332 | 0.5% | TikTok |
| 即梦 | 301 | 0.5% | 即梦 |
| Kiro | 294 | 0.5% | Kiro |
| X | 205 | 0.3% | X |
| Notion | 107 | 0.2% | Notion |
| Suno | 36 | 0.1% | Suno |
| Perplexity | 32 | 0.1% | Perplexity |
| 多邻国 | 30 | 0.0% | 多邻国 |
| 礼品卡 | 26 | 0.0% | 礼品卡 |
| Microsoft | 9 | 0.0% | Copilot |
| Windsurf | 5 | 0.0% | Windsurf |
| PayPal | 3 | 0.0% | PayPal |

## 标准商品分布

标准商品由 `product`（slug）+ `product_label` 标识，当前共 77 个标准商品（`vendor` 与 `category` 均按 `product_map.json` 口径同步对齐）。三路归类：CardNav 行按 `item_url` 回查原始 `autoCategory` 并按标题细化；PriceAI 行按 `(标题, 价格, 店名)` 回查快照 `top_offers`；其余按 `category` 基线 + 标题关键词。当前 `other-product` 共 2893 行（4.6%），主要为 CapCut、Runway、Kling、Figma 等非核心长尾商品与杂项标题。

| 标准商品 | 行数 | 占比 |
|---|---|---|
| ChatGPT Plus 试用订阅 (`chatgpt-plus`) | 10456 | 16.8% |
| ChatGPT Team 10x (`chatgpt-team-10x`) | 4432 | 7.1% |
| OpenAI / ChatGPT 接码 (`sms-openai`) | 3289 | 5.3% |
| ChatGPT Team 5x (`chatgpt-team-5x`) | 3064 | 4.9% |
| 其他商品 (`other-product`) | 2893 | 4.6% |
| ChatGPT Pro 100刀档 代充 (`chatgpt-pro-100`) | 2769 | 4.4% |
| Gmail / Google 邮箱 (`gmail-account`) | 2391 | 3.8% |
| ChatGPT Pro 200刀档 代充 (`chatgpt-pro-200`) | 2094 | 3.4% |
| ChatGPT 普号 (`chatgpt-free-account`) | 2060 | 3.3% |
| Outlook / Hotmail 邮箱 (`outlook-account`) | 1814 | 2.9% |
| ChatGPT Plus 正价代充 (`chatgpt-plus-recharge`) | 1741 | 2.8% |
| Gemini Pro 充值/开通 (`gemini-pro`) | 1643 | 2.6% |
| Muse AI 账号 (`muse-ai-account`) | 1492 | 2.4% |
| Gemini Pro 成品号 (`gemini-pro-account`) | 1244 | 2.0% |
| ChatGPT Team (`chatgpt-team`) | 1184 | 1.9% |
| Codex 额度充值 (`codex-credits`) | 1135 | 1.8% |
| Claude 普号 / 兑换号 (`claude-account`) | 1068 | 1.7% |
| 中转站 / API 网关 (`api-gateway`) | 913 | 1.5% |
| ChatGPT Pro 500刀档 代充 (`chatgpt-pro-500`) | 910 | 1.5% |
| Apple ID / 苹果账号 (`apple-id-account`) | 845 | 1.4% |
| Grok Super (`grok-super`) | 791 | 1.3% |
| Gemini 账号 (`gemini-account`) | 682 | 1.1% |
| 真人 / KYC 验证 (`kyc`) | 642 | 1.0% |
| Grok Ultra (`grok-ultra`) | 631 | 1.0% |
| 通用接码 (`sms-generic`) | 599 | 1.0% |
| Google AI Ultra 20x (`gemini-ultra-20x`) | 596 | 1.0% |
| iCloud 邮箱 (`icloud-email`) | 591 | 0.9% |
| Grok Premium (`grok-premium`) | 587 | 0.9% |
| ChatGPT Go (`chatgpt-go`) | 566 | 0.9% |
| Claude Pro 代充 (`claude-pro`) | 564 | 0.9% |
| Telegram 账号 (`telegram-account`) | 482 | 0.8% |
| 其他邮箱 (`email-account`) | 472 | 0.8% |
| Claude Max 5x 代充 (`claude-max-5x`) | 437 | 0.7% |
| Grok 普号 / 体验号 (`grok-account`) | 425 | 0.7% |
| Google / Gemini 接码 (`sms-google`) | 416 | 0.7% |
| Grok Plus (`grok-plus`) | 401 | 0.6% |
| Claude Max 20x 代充 (`claude-max-20x`) | 397 | 0.6% |
| 虚拟卡 (`virtual-card`) | 397 | 0.6% |
| Google AI Ultra 5x (`gemini-ultra-5x`) | 397 | 0.6% |
| Claude Pro 成品号 (`claude-pro-account`) | 392 | 0.6% |
| 社媒账号 (`social-media-account`) | 380 | 0.6% |
| Gemini Plus (`gemini-plus`) | 338 | 0.5% |
| TikTok 账号 (`tiktok-account`) | 332 | 0.5% |
| Claude / Anthropic 接码 (`sms-claude`) | 307 | 0.5% |
| Dreamina / 即梦 (`dreamina-account`) | 301 | 0.5% |
| ChatGPT Pro 100刀档 成品号 (`chatgpt-pro-100-account`) | 251 | 0.4% |
| Kiro Pro / 额度号 (`kiro-pro`) | 198 | 0.3% |
| Cursor 接码 (`sms-cursor`) | 196 | 0.3% |
| Cursor 账号 (`cursor-account`) | 190 | 0.3% |
| Meta / Muse 接码 (`sms-muse`) | 185 | 0.3% |
| X / 推特账号 (`x-account`) | 180 | 0.3% |
| Claude Max 20x 成品号 (`claude-max-20x-account`) | 163 | 0.3% |
| ChatGPT Pro 200刀档 成品号 (`chatgpt-pro-200-account`) | 158 | 0.3% |
| Claude Max 5x 成品号 (`claude-max-5x-account`) | 131 | 0.2% |
| Cursor Ultra (`cursor-ultra`) | 122 | 0.2% |
| Instagram / Threads 接码 (`sms-instagram`) | 108 | 0.2% |
| Notion 商业版 (`notion-business`) | 107 | 0.2% |
| Kiro 普号 / Free (`kiro-account`) | 96 | 0.2% |
| 教育邮箱 (`education-email`) | 82 | 0.1% |
| Cursor Free (`cursor-free`) | 80 | 0.1% |
| ChatGPT Pro 500刀档 成品号 (`chatgpt-pro-500-account`) | 75 | 0.1% |
| PayPal 接码 (`sms-paypal`) | 72 | 0.1% |
| Cursor Pro (`cursor-pro`) | 70 | 0.1% |
| 提链卡密 (`topup-card`) | 64 | 0.1% |
| Telegram Premium / Pro 会员 (`telegram-premium`) | 41 | 0.1% |
| Suno 账号 (`suno-account`) | 36 | 0.1% |
| Perplexity 账号 (`perplexity-account`) | 32 | 0.1% |
| 多邻国 Super 会员 (`duolingo-super`) | 30 | 0.0% |
| 礼品卡 (`gift-card`) | 26 | 0.0% |
| Claude Team Standard (`claude-team-standard`) | 25 | 0.0% |
| X Premium / 推特会员 (`x-premium`) | 25 | 0.0% |
| Copilot (`copilot`) | 9 | 0.0% |
| Codex / ChatGPT 周边与自助服务 (`codex-service`) | 8 | 0.0% |
| Claude Team Premium (`claude-team-premium`) | 5 | 0.0% |
| Claude KYC 认证 (`claude-kyc`) | 5 | 0.0% |
| Windsurf 账号 (`windsurf-account`) | 5 | 0.0% |
| PayPal (`paypal`) | 3 | 0.0% |

## 口径与缺口

- **直抓缺口**：链动小铺（wzyp 909 家店）与云猫（100 家店）本次 0 行，需真实浏览器会话过一次 ESA 验证、保住 cookies 后再调 goodsList 分页拉取。9 月快照（Samge0/wzyp-view，250 家店 / 11042 件商品）未并入，因非当日数据。
- **水獭时效**：MCP 当日取数返回 403（Cloudflare 按 IP 信誉拦截，本机与新加坡 VPS 出口均被拦），20 行来自 2026-11-14 首页缓存副本，仅作兜底；待换出口重跑 MCP 全量（约 73 SKU）后整体替换。
- **AI价网覆盖**：63 种标准商品只有 44 种有 md 文件（其余 19 种如 GPT Pro、Kiro、DeepSeek、Sora 在 index 表里比价页为“—”）；每类只含在售最便宜 50 家。
- **AI价网链接口径**：md 层不给原站单品链接，`item_url` 为 AI价网分类页，`shop_url` 为 AI价网店铺页；原站店铺链接仅 wzyp 可推导（wzyp.cn/shop/\<token>）。
- **水獭链接口径**：`platform` 未知记为“未知”，`shop_id` 暂用店名，`item_url` 仅 3 行有值。
- **市场价**：各源均未提供有效市场价，`market_price` 全为空。
- **PriceAI**：2026-11-19 21:01 Jazzu 决定自用研究不考虑许可限制后，已并入其公开快照（data.priceai.cc/latest.json → 当日快照，66 商品、每品最多 5 条 top offers，共 325 条，抓取时间 2026-11-19T20:56+08:00）。并入 302 条新行，13 条以更新鲜的 PriceAI 行替换同款旧行，9 条无效剔除（5 条 ¥0、4 条过期）。全量报价 API（/api/products/[id]/offers，约 15855 条）已验证可用（真实浏览器与 Chrome UA curl 均 200），但 2026-11-19 21:28 起的全量拉取被 429 限流：本机 IP（2 秒/页，66 商品全灭 0 行）与新加坡 VPS（10 秒/页，首商品退避 30/60/120 秒后仍 429）均被拦，两边拉取已停；单次探测是通的，连续拉就拦，限流按请求速率触发。快照 315 行已在库里，全量等限流解除或换浏览器会话再说。
- **CardNav**：2026-11-19 21:32 找到批量口径并并入：公开 JSON `GET https://cardnav.xyz/api/shop-products.json`（仓库 `src/pages/api/shop-products.json.ts`，无鉴权），一次返回 8.8MB：1009 家店、2623 个分类、40493 件商品；行是位置数组，按仓库 `src/shop-products-data.ts` 的 pack 规则解码（店 10 位、商品 12 位，分类与价格单位另有对照表）。分类按 autoCategory 直映射 + 标题关键词兜底归类；平台按商品链接 host 派生（wzyp / 16688 / catfk→云猫 / 其余自建站）；去重仅当新行更新鲜才替换旧行。
- **AIPricedb、模真真**：均为闭源、无公开许可，无批量拉取口径，只能顺着线索去原站核对（新店发现、验真报告），不能批量拉取。模真真的验真报告可作中转站风险线索。
- **开源站调研结论（2026-11-19）**：唯一数据本身明确 CC BY 4.0 的卡网报价源仍是 AI价网（已在用）。顺带核实的两个可合法新增的候选只覆盖官方按量 API 价、不含卡网转售价，且与订阅价单位不同，需单独成组，尚未并入：API Price Index（apipriceindex.com，996 个 LLM API 报价，数据集 CC BY 4.0）和 AICostBudget 的 ai-api-pricing-data（196 个模型）；使用前须再对一次许可。
- **跨站口径差异**：PriceAI 与 AI价网对“标准商品”的切分不同（如 Cursor 成品号 ¥0.35 vs AI价网 Cursor ¥20），跨站比价须先对齐定义。

## 复算方法

```python
import json
from collections import Counter
d = json.load(open('data.json'))
items = d['items']
len(items)  # 总行数
Counter(r['source'] for r in items)  # 各源行数
Counter(r['platform'] for r in items)  # 平台分布
Counter(r['vendor'] for r in items)  # 厂商分布
len({(r['platform'], r['shop_id']) for r in items})  # 覆盖店铺数
Counter('有货' if r['stock'] > 0 else ('缺货' if r['stock'] == 0 else '库存未公开') for r in items)  # 库存分布
```
