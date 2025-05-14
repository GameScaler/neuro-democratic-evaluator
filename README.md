# 神经民主评估体系

基于媒介递归性理论的商业空间评估系统，实现多维度的空间价值量化分析。

## 核心功能

- **多源数据融合**  
  整合社交媒体UGC内容与空间影像资料
- **六维向量评估**  
  物质/行为/感知三维度裂变的评估体系
- **可解释性架构**  
  模块化设计保障理论模型的可追溯性

## 技术特性

- 多模态数据处理架构
- 基于控制论的必要多样性原则
- 神经民主指数的非线性集成

## 快速开始

### 环境配置

```bash
git clone --recurse-submodules https://github.com/yourusername/neuro-democratic-evaluator.git
cd neuro-democratic-evaluator
pip install -r requirements.txt
playwright install
```

### 配置文件设置

1. 创建 `.env` 文件：

```ini
LLM_API_KEY=your_siliconflow_api_key
```

2. 小红书Cookie配置：

```bash
python -m MediaCrawler login xhs
# 扫码登录后自动保存cookies
```

### 使用流程

1. 将待分析图片放入 `static/uploads/` 目录（支持JPG/PNG格式）
2. 运行主程序：

```bash
python main.py
```

3. 输入项目名称（如"阿那亚"）
4. 查看生成的评估报告（JSON格式）

## 输出示例

```json
{
  "project": "阿那亚",
  "text_sources": 15,
  "image_sources": 3,
  "scores": {
    "material_narrative": {"score":4.5, "comment":"混凝土风化层记录十年海风侵蚀"},
    "spatial_fold": 3.9,
    "movement_contingency": {"score":4.8, "comment":"32%评论提及路径迷失体验"},
    "visual_afterimage": 4.2,
    "tactile_democracy": 4.1
  }
}
```

## 系统特性

该版本实现了：
- 完整的媒体数据采集流程
- 增强的图像特征工程
- 符合学术规范的评估逻辑
- 可审计的结果输出格式

## 理论依据

本系统基于以下学术框架：
- 德勒兹差异哲学
- 麦克卢汉媒介理论
- 斯蒂格勒技术药学

## 许可协议

本项目采用[知识共享署名-非商业性使用 4.0 国际许可协议](https://creativecommons.org/licenses/by-nc/4.0/deed.zh)