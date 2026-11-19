# AI 聚合比价 · 数据报告

生成时间：2026-11-19T18:40:00+08:00，2026-11-19T21:00:00+08:00 增加 vendor（厂商）字段，2026-11-19T21:15:00+08:00 并入 PriceAI 快照 · 数据文件：`data.json`（同目录）
本报告所有数字均由 `data.json` 的 `items` 数组复算，复算方法见文末。

## 总览

- 报价总行数：**7956**
- 覆盖店铺数：**984**（按 平台+店铺标识 去重）
- 分类数：**43**
- 厂商数：**25**
- 价格区间：¥0.01 ~ ¥15500.0
- 数据观察时间：AI价网 2026-11-19T18:27:39+08:00；BiWu 2026-11-19T18:28:10+08:00；水獭 2026-11-14T12:37:00+08:00（5 天前缓存，见口径说明）；PriceAI 2026-11-19T20:56:00+08:00

## 各源净增

| 来源 | 原始行数 | 并入行数 | 去重剔除 | 无效剔除 | 占位剔除 |
|---|---|---|---|---|---|
| 直抓 | 0 | 0 | 0 | 0 | 0 |
| AI价网 | 1843 | 1697 | 145 | 0 | 1 |
| BiWu | 5983 | 5937 | 44 | 2 | 0 |
| 水獭 | 20 | 20 | 0 | 0 | 0 |
| PriceAI | 325 | 302 | 14 | 9 | 0 |

- PriceAI 14 条去重中，13 条以更新鲜的 PriceAI 行替换了同款旧行（BiWu 5、AI价网 8），1 条为快照内重复；PriceAI 行现存 315 行。9 条无效为 5 条 ¥0 价 + 4 条已过期报价。

- 去重键：平台 + 店铺标识 + 标题 + 价格（无商品标识时的 fallback）；优先级 直抓 > AI价网 > BiWu > 水獭。
- 直抓 0 行：wzyp / catfk 接口与店铺页均被阿里云 ESA 人机验证拦截，各只试一次，未硬试滑块。
- 无效剔除：BiWu 2 行价格为 ¥0（免费邀请码/免费接码号），无有效售价。
- 占位剔除：AI价网 Telegram 分类 1 行，价格 ¥9999、库存 9999，疑似商家占位价。
- AI价网原始 1843 行中有 145 行源内重复（同一店铺同一标题同一价格出现在多个分类）；BiWu 原始 5983 行中有 44 行与 AI价网重复或源内重复。

## 平台分布

| 平台 | 行数 | 占比 | 店铺数 |
|---|---|---|---|
| wzyp | 6005 | 75.5% | 626 |
| Kami | 872 | 11.0% | 18 |
| 自建站 | 412 | 5.2% | 113 |
| 16688 | 439 | 5.5% | 176 |
| 独角数卡 | 147 | 1.8% | 8 |
| 云猫 | 61 | 0.8% | 28 |
| 未知 | 20 | 0.3% | 15 |

## 库存分布

| 状态 | 行数 | 占比 | 口径 |
|---|---|---|---|
| 有货 | 7408 | 93.1% | stock > 0（数字为件数；仅有有货标记的源记 1） |
| 缺货 | 407 | 5.1% | stock = 0 |
| 库存未公开 | 141 | 1.8% | stock = -1 |

## 分类 Top 10

| 分类 | 行数 |
|---|---|
| 邮箱 | 1394 |
| ChatGPT Plus | 1325 |
| 接码 | 738 |
| ChatGPT Pro | 647 |
| ChatGPT Team | 603 |
| Gemini Pro | 418 |
| ChatGPT 账号 | 310 |
| Grok Super | 212 |
| Claude 账号 | 199 |
| Claude Pro | 194 |

## 厂商分布（vendor 字段，2026-11-19 21:00）

category（产品线）保留，新增 vendor（厂商）字段：同品牌商品归到同一厂商下，非 AI 品类厂商即品类本身。

| 厂商 | 行数 | 占比 | 包含的产品线 |
|---|---|---|---|
| OpenAI | 2992 | 37.6% | ChatGPT Plus / Pro / Team / 账号 / Go、Codex |
| 邮箱 | 1394 | 17.5% | 邮箱 |
| 接码 | 738 | 9.3% | 接码 |
| Google | 677 | 8.5% | Gemini Pro / Ultra / Plus / 账号 |
| Anthropic | 654 | 8.2% | Claude 账号 / Pro / Max 20x / Max 5x / Team |
| xAI | 569 | 7.2% | Grok Super / 账号 / Plus / Premium / Ultra、SuperGrok Heavy / Lite |
| 其他 | 190 | 2.4% | 其他 |
| Cursor | 130 | 1.6% | Cursor |
| 虚拟卡 | 113 | 1.4% | 虚拟卡 |
| KYC | 99 | 1.2% | KYC |
| Telegram | 94 | 1.2% | Telegram |
| X | 73 | 0.9% | X |
| Apple ID | 57 | 0.7% | Apple ID |
| TikTok | 49 | 0.6% | TikTok |
| 中转站 | 50 | 0.6% | 中转站 |
| Kiro | 39 | 0.5% | Kiro |
| 礼品卡 | 5 | 0.1% | 礼品卡 |
| Perplexity | 5 | 0.1% | Perplexity |
| Muse AI | 5 | 0.1% | Muse AI |
| 即梦 | 5 | 0.1% | 即梦 |
| Notion | 5 | 0.1% | Notion |
| Microsoft | 4 | 0.1% | Copilot |
| Suno | 4 | 0.1% | Suno |
| PayPal | 3 | 0.0% | PayPal |
| 多邻国 | 2 | 0.0% | 多邻国 |

## 口径与缺口

- **直抓缺口**：链动小铺（wzyp 909 家店）与云猫（100 家店）本次 0 行，需真实浏览器会话过一次 ESA 验证、保住 cookies 后再调 goodsList 分页拉取。9 月快照（Samge0/wzyp-view，250 家店 / 11042 件商品）未并入，因非当日数据。
- **水獭时效**：MCP 当日取数返回 403（Cloudflare 按 IP 信誉拦截，本机与新加坡 VPS 出口均被拦），20 行来自 2026-11-14 首页缓存副本，仅作兜底；待换出口重跑 MCP 全量（约 73 SKU）后整体替换。
- **AI价网覆盖**：63 种标准商品只有 44 种有 md 文件（其余 19 种如 GPT Pro、Kiro、DeepSeek、Sora 在 index 表里比价页为“—”）；每类只含在售最便宜 50 家。
- **AI价网链接口径**：md 层不给原站单品链接，`item_url` 为 AI价网分类页，`shop_url` 为 AI价网店铺页；原站店铺链接仅 wzyp 可推导（wzyp.cn/shop/\<token>）。
- **水獭链接口径**：`platform` 未知记为“未知”，`shop_id` 暂用店名，`item_url` 仅 3 行有值。
- **市场价**：三源均未提供有效市场价，`market_price` 全为空。
- **PriceAI**：2026-11-19 21:01 Jazzu 决定自用研究不考虑许可限制后，已并入其公开快照（data.priceai.cc/latest.json → 当日快照，66 商品、每品最多 5 条 top offers，共 325 条，抓取时间 2026-11-19T20:56+08:00）。并入 302 条新行，13 条以更新鲜的 PriceAI 行替换同款旧行，9 条无效剔除（5 条 ¥0、4 条过期）。此前仅作店铺发现与交叉核对（106 家店，其中 52 家不在 AI价网清单里）。
- **CardNav**：代码 AGPL-3.0，DATA_LICENSE 同款禁止批量复制与用作替代数据源；仓库内无采集器（人工整理 + 商家/用户提交审核），只能发现核对。
- **AIPricedb、模真真**：均为闭源、无公开许可，默认保留所有权利，只能顺着线索去原站核对（新店发现、验真报告），不能批量拉取。模真真的验真报告可作中转站风险线索。
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
