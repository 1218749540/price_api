# 价格查询 API

这是一个基于 Flask 的 API，可以查询淘宝和京东商品的价格历史。

## 部署

```sh
docker-compose up --build -d
```

## 使用方法

```sh
curl "http://your-vps-ip:5001/price?url=https://item.jd.com/123456.html"
```
