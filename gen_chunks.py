"""从正本 data.json 生成 compact-v1 分片（data-1..4.json），与空间里的编码一致。

编码（与页面 decodeCompact 互逆，见导出 HTML 内联脚本）：
  行 -> [title, price, market_price, stock, shop_idx, platform_idx, source_idx,
         category_idx, vendor_idx, item_url, observed_idx, product_idx]
  shop_idx 查 manifest.dicts.shops 的 [shop_name, shop_url, shop_id] 三元组；
  product_idx 查 dicts.products 的 [slug, label]。
分片：按正本顺序均分 4 份（每份 11640 行），与 manifest.chunks 的
  ["assets/data-1.json", ..., "assets/data-4.json"] 对应。
最后做解码往返校验：按 decodeCompact 的逻辑把分片解回对象行，与正本逐行逐字段比对。
"""
import json
import re
import base64
import sys

BASE = "/home/hatch/workspace/ai-price-space"
DATA = f"{BASE}/research/data.json"
EXPORT_HTML = "/home/hatch/workspace/your_files/aiju-he-bi-jia-kong-jian/aiju-he-bi-jia-kong-jian.html"
OUT_DIR = f"{BASE}/github/assets"
N_CHUNKS = 4


def load_manifest():
    html = open(EXPORT_HTML, encoding="utf-8").read()
    m = re.search(r"data:application/json;base64,([A-Za-z0-9+/=]+)", html)
    man = json.loads(base64.b64decode(m.group(1)))
    assert man["format"] == "compact-v1", man.get("format")
    return man


def main():
    man = load_manifest()
    d = json.load(open(DATA, encoding="utf-8"))
    items = d["items"]
    assert len(items) == man["total"] == 46560, (len(items), man["total"])

    dicts = man["dicts"]
    shop_idx = {tuple(s): i for i, s in enumerate(dicts["shops"])}
    plat_idx = {v: i for i, v in enumerate(dicts["platforms"])}
    src_idx = {v: i for i, v in enumerate(dicts["sources"])}
    cat_idx = {v: i for i, v in enumerate(dicts["categories"])}
    ven_idx = {v: i for i, v in enumerate(dicts["vendors"])}
    obs_idx = {v: i for i, v in enumerate(dicts["observed"])}
    prod_idx = {tuple(p): i for i, p in enumerate(dicts["products"])}

    misses = {"shop": 0, "platform": 0, "source": 0, "category": 0,
              "vendor": 0, "observed": 0, "product": 0}
    rows = []
    for r in items:
        si = shop_idx.get((r["shop_name"], r["shop_url"], r["shop_id"]))
        pi = plat_idx.get(r["platform"])
        soi = src_idx.get(r["source"])
        ci = cat_idx.get(r["category"])
        vi = ven_idx.get(r["vendor"])
        oi = obs_idx.get(r["observed_at"])
        pri = prod_idx.get((r["product"], r["product_label"]))
        for key, val in (("shop", si), ("platform", pi), ("source", soi),
                         ("category", ci), ("vendor", vi), ("observed", oi),
                         ("product", pri)):
            if val is None:
                misses[key] += 1
        if None in (si, pi, soi, ci, vi, oi, pri):
            raise SystemExit(f"字典缺失：{r['title'][:40]} shop={si} plat={pi} src={soi} cat={ci} ven={vi} obs={oi} prod={pri}")
        rows.append([r["title"], r["price"], r["market_price"], r["stock"], si,
                     pi, soi, ci, vi, r["item_url"], oi, pri])
    print("misses:", misses)

    import os
    os.makedirs(OUT_DIR, exist_ok=True)
    n = len(rows)
    per = (n + N_CHUNKS - 1) // N_CHUNKS
    for i in range(N_CHUNKS):
        part = rows[i * per:(i + 1) * per]
        path = f"{OUT_DIR}/data-{i + 1}.json"
        json.dump(part, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
        print(f"chunk {i + 1}: {len(part)} rows -> {path} ({os.path.getsize(path)} bytes)")

    # 解码往返校验（复刻 decodeCompact）
    shops, platforms, sources = dicts["shops"], dicts["platforms"], dicts["sources"]
    cats, vens, obss, prods = dicts["categories"], dicts["vendors"], dicts["observed"], dicts["products"]
    decoded = []
    for i in range(N_CHUNKS):
        part = json.load(open(f"{OUT_DIR}/data-{i + 1}.json", encoding="utf-8"))
        for row in part:
            shop = shops[row[4]]
            prod = prods[row[11]]
            decoded.append({
                "title": row[0], "price": row[1], "market_price": row[2], "stock": row[3],
                "shop_name": shop[0], "shop_url": shop[1], "shop_id": shop[2],
                "platform": platforms[row[5]], "source": sources[row[6]],
                "category": cats[row[7]], "vendor": vens[row[8]],
                "item_url": row[9], "observed_at": obss[row[10]],
                "product": prod[0], "product_label": prod[1],
            })
    assert len(decoded) == len(items), (len(decoded), len(items))
    bad = 0
    for a, b in zip(decoded, items):
        if a != b:
            bad += 1
            if bad <= 3:
                print("MISMATCH:", {k: (a[k], b[k]) for k in a if a[k] != b[k]})
    print(f"round-trip: {len(decoded)} rows, mismatches: {bad}")
    assert bad == 0


if __name__ == "__main__":
    main()
