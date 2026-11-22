# AI聚合比价空间

把散布在各个卡网（发卡平台）和 AI 代充聚合站的 AI 订阅 / 账号商品（ChatGPT、Claude、Gemini、Grok、Cursor 等的代充、成品号、卡密、车位）聚合到一处，按关键词、平台、店铺、价格、库存快速比价。

只做信息聚合，不卖货、不下单、不登录任何账号。

## 在线使用

有两个发布渠道，内容同源、部署形态不同：

- **GitHub Pages**：<https://jazzulu.github.io/ai-price-space/> —— 本仓库 main 分支 push 后自动构建，入口就是 `index.html`。
- **Muse 空间**：Muse 侧边栏「空间」区的 `aiju-he-bi-jia-kong-jian`。空间用相对路径加载随包发布的内置数据，不读 GitHub Pages，所以数据和前端都要单独合入并重建才更新（见「部署」）。

## 当前数据快照

- 更新时间：**2026-11-22 14:46 CST**（commit `211ca37`）
- 报价：**59,804 行**，覆盖 **1,670 家店铺**，**77 个标准商品**
- 数据每 6 小时自动重采一次（见「定时刷新」），数字以 `data.json` 的 meta 和 `report.md` 为准。

## 文件

本仓库是发布出来的站点本身，只含这些文件。采集与合并的脚本不在仓库里，在 VM 的 `~/workspace/ai-price-space/`（见「数据从哪来」）。

| 文件 | 说明 |
| --- | --- |
| `index.html` | 完整页面（静态页，无构建步骤；数据外置，加载时拉取，不内嵌） |
| `data.json` | 清单 manifest：meta（总数、店铺数、来源）+ 4 个分片的地址，约 241KB |
| `assets/data-1.json` … `assets/data-4.json` | 4 个数据分片，共约 8.6MB；页面顺序加载，第一片到了就能先看 |
| `report.md` | 统计报告：总数、各源净增、各平台分布、库存分布，每个数字都可从 `data.json` 复算 |
| `product_map.json` | 77 个标准商品的映射（商品名归一） |
| `README.md` | 本文件：交接文档 |

## 数据从哪来

工作副本在 VM 的 `~/workspace/ai-price-space/research/data.json`，合并链的脚本都在 `~/workspace/ai-price-space/`（`refresh_data.py`、`merge_priceai.py`、`merge_cardnav.py`、`add_product_field.py`、`dedup_listings.py`、`gen_report.py`、`gen_manifest.py`、`gen_chunks.py` 等）。只跑它们，不要改逻辑。

合并链（`refresh_data.py` 编排）：

1. **PriceAI 快照**：拉 `https://data.priceai.cc/latest.json` 看 `snapshot_id`，变了才下载完整快照并合并。
2. **CardNav 整包**：`GET https://cardnav.xyz/api/shop-products.json`（一次约 8.8MB，无鉴权），整包重拉后合并。
3. 清洗：`fix_shop_ids`（wzyp 店铺标识大小写归一）→ `drop_placeholder_prices` → `add_product_field`（重算标准商品字段，含 junk / 免费号纠正）→ `dedup_listings`（同一店铺同一商品链接只留最新一行）。
4. 生成：`gen_report` → `gen_manifest` → `gen_chunks`（含解码往返校验）。

来源：PriceAI 快照、CardNav 整包、AI价网（aiprice.club）、BiWu（biwu.ai）、水獭（shuita.xyz）。直抓（链动小铺 wzyp、云猫）为 0 行：直连被阿里云 ESA 人机验证拦截，需真实浏览器会话过验证保住 cookies 后再拉接口，未硬刷。

注意：

- 数据许可只记来源、不挡自用研究（PriceAI Source Available 1.0、CardNav AGPL 等）。
- **封号 / 死号不能宽匹配**——「封号质保 / 封号双保」是质保承诺，宽匹配会误删上千行好商品；只有「封号的 / 死号的」才是真死号。
- 单份 data.json 曾达 25,000,112 字节、超过网关 25,000,000 上限导致拉取失败，所以数据必须分片；不要再把全量塞进一个文件。SQLite 不需要。

## 定时刷新（每 6 小时）

cron `ai-price-space-refresh`，每 6 小时跑一轮（锚点 2026-11-20 02:45 CST，Asia/Shanghai），定义在 `~/workspace/goals/ai-price-comparison-space/crons/hourly/ai-price-space-refresh__interval@6h.md`。**只推数据，不动前端。**

每轮：

1. 跑 `python3 ~/workspace/ai-price-space/refresh_data.py`（跑之前自动备份 `data.json` 到 `/tmp/data.json.bak_refresh_<时间>`）。
2. 用 `md5sum` 对比备份与当前 `research/data.json`。**没变就静默结束**：不推 GitHub、不发消息、不动空间。
3. 变了才做：把 `research/manifest.json` 拷为 `github/data.json`（覆盖），更新 `github/assets/data-1..4.json` 和 `report.md`；**不要动 `github/index.html`**（前端由 Jazzu 维护）。`git add -A`、commit（信息写清新旧行数与店铺数）、`push origin main`；用 `gh api repos/JazzuLu/ai-price-space/pages/builds/latest` 核 Pages 构建 built，再 curl 线上 Pages 与 4 个分片核对 HTTP 200 与总行数。
4. 完成后在主聊天告诉 Jazzu 一句话：新旧行数、店铺数、推没推 GitHub（附 commit）。

失败处理：任何一步失败（拉取 429 / 超时、合并报错、分片校验不通过、Pages 构建失败），**不要反复重试、不要推一半的数据**；把失败原因和当前数据状态告诉 Jazzu，等他决定。运行记录只记到当日的 `~/memory/YYYY-MM-DD.md`，不要改 `MEMORY.md`。

注意：刷新汇报里的「线上核对通过」核的是 GitHub Pages，不是 Muse 空间地址；空间内容要另核。

## 部署

### GitHub Pages

push main 即自动构建，无额外步骤。核对：Pages 构建状态 + 线上 `index.html` 与本地 md5 一致。

### Muse 空间

空间 slug `aiju-he-bi-jia-kong-jian`，源文件在助手侧（`ts-spaces/aiju-he-bi-jia-kong-jian/index.html`），通过 artifact 构建流程发布。空间页面用相对路径加载随包发布的内置数据（`assets/data.json` + 分片），不读 GitHub Pages。

**唯一事实来源是 `github/index.html`。** 前端由 Jazzu 在本仓库改，改完后由助手把改动合入空间源文件并重建。**绝不能把空间旧版导出覆盖 `github/index.html`**——2026-11-22 查实两份曾分叉：空间停在 11-20 旧版（49,915 条 / 1,642 店），Pages 已是新版（59,804 条 / 1,670 店），合入重建后才一致。旧流程「空间为准、export 覆盖 github/」已废弃，不要恢复。

同步规矩：

- 每次同步先**双向 diff**，不要单向盲覆盖——空间构建时可能带自己的修复（2026-11-22 就有 3 处手机端修复和 1 处加载修复先落在空间那份，后来才写回本仓库）。
- 两份文件现仅剩**一行有意差异：清单加载顺序**。Pages 版先试根目录 `data.json`、再回退 `assets/data.json`；空间版反过来。**别统一这一行**，各自对应部署形态。
- 加载健壮性（2026-11-22 修过）：清单走实际存在的路径、请求失败自动重试 3 次、分片顺序加载；数据本身不动。
- 同步后要在**空间地址**上实测加载通过，只核 Pages 不算数。

### 自动同步（已上线，每小时）

cron `ai-price-space-auto-sync`（2026-11-22 Jazzu 选每小时）：定时 hash `github/index.html` + 数据文件，有变化就合入空间并重建、失败通知；构建进行中时跳过；水位只在同步成功后记录，水位文件在 `~/workspace/goals/ai-price-comparison-space/hidden_files/last-sync.txt`。首次同步 2026-11-22 22:48 完成，空间数据 59,804 → 61,167 行。

## 前端开发

- `index.html` 由 Jazzu 维护，内联编译后的 Tailwind v3.4.17，**无 CDN 引用、无构建步骤**（2026-11-20 审计发现 CDN Tailwind 与 Google Fonts 失败时整页退化为无样式 HTML，已消除）。
- 界面：三级聚类浏览（大类 Tab → 标准商品 → 店铺聚合），移动端交互已精简。
- 卡片：最低价 + 绿色质保最低价、有货 / 缺货数、渠道数，点卡片进渠道报价表。
- 功能：关键词搜索；按平台 / 来源 / 分类 / 店铺筛选；只看有货开关；价格排序与价格区间；页内刷新按钮 no-store 重拉数据，自动刷新开关默认关、30 分钟。
- 改完前端后告诉助手合入空间并重建，不要自己动空间源文件。

## 库存口径

数字 = 库存件数；0 = 缺货；只有「有货 / 缺货」标记的源，有货记 1、缺货记 0；未知记 -1（库存未公开）。

## 数据来源与署名

- **AI价网（aiprice.club）** — 数据 CC BY 4.0，使用须注明来源并附链接。
- **水獭（shuita.xyz）** — 派生报价行，署名水獭。
- **BiWu.Ai（biwu.ai）** — 全渠道报价表。
- **PriceAI（priceai.cc）** — 快照数据，Source Available 1.0。
- **CardNav（cardnav.xyz）** — 整包数据，AGPL。

## 教训

- MCP GitHub App 建库报 403，**建库走本机 gh CLI**（已登录 JazzuLu）。
- `merge_cardnav.py` 的 wzyp token 去重前未小写，重采曾多出 18,848 行，现已统一小写。
- `merge.py` 曾无 `__main__` 守卫，import 会重跑合并覆盖 `data.json`（已加守卫并验证无副作用）。
- PriceAI 全量并入不要硬来：全量在 `GET /api/products/[id]/offers`（约 120 页），本机与新加坡 VPS 拉取均被 429 限流、已停；脚本 `pull_priceai_full.py`，原始文件存 `raw/priceai_full/`。
- wzyp 直接抓取在出口 / IP 层被挡（ESA 挑战），要走真实浏览器 cookie 路线。
