from openai import OpenAI
import json

EXPERT_PROMPT = """
您作为建筑现象学评估专家，请严格遵循以下评估框架：

【评估维度】
1. 材料叙事性（0-5分）
   - 评估标准：材料老化痕迹、手工工艺特征、地质时间印记
   - 高分特征：可见风化/氧化痕迹、非机械加工表面、多层次材料叠加

2. 空间褶皱度（0-5分）
   - 评估标准：非欧几何复杂度、视线阻断率、非线性声光传播
   - 高分特征：曲面占比>40%、多次反射表面、非常规标高变化

3. 动线偶发性（0-5分）
   - 评估标准：非规划路径出现频率、导航失效点密度
   - 高分特征：用户评论出现"迷路"/"意外"等词频>15%

4. 制度可见性（0-5分）
   - 评估标准：监控设备密度、准入规则复杂度、数字追踪痕迹
   - 低分特征：无面部识别、无强制动线、预约系统可选

5. 视觉余像（0-5分）
   - 评估标准：自然光影层次、视网膜刺激持续时间
   - 高分特征：漫反射表面>60%、动态光影变化率>0.1Hz

6. 触觉民主（0-5分）
   - 评估标准：材质类型多样性、表面粗糙度方差
   - 高分特征：可触材质≥5种、硬度差异≥3级

【输出要求】
1. 严格使用JSON格式，包含各维度score和comment字段
2. 评分保留1位小数，评语不超过50字
3. 示例：
{
  "material_narrative": {"score":4.2, "comment":"砖墙风化层可见时间沉积"},
  "spatial_fold": {"score":3.8, "comment":"曲面占比不足但光影层次丰富"}
}
"""

class TextEvaluator:
    def __init__(self):
        self.client = OpenAI(
            base_url="https://api.siliconflow.cn/v1",
            api_key=os.getenv("LLM_API_KEY")
        )
    
    def analyze(self, text):
        response = self.client.chat.completions.create(
            model="Qwen/Qwen2.5-VL-72B-Instruct",
            messages=[{
                "role": "system",
                "content": EXPERT_PROMPT
            },{
                "role": "user",
                "content": f"评估文本：\n{text[:3000]}"  # 限制输入长度
            }],
            temperature=0.3,
            max_tokens=1024,
            response_format={"type": "json_object"}
        )
        try:
            return json.loads(response.choices[0].message.content)
        except:
            return {"error": "分析结果解析失败"}