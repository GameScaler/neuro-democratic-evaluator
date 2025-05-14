import json
import os
from datetime import datetime
from crawlers.xhs_crawler import search_project
from evaluator.text_analyzer import TextEvaluator
from evaluator.image_analyzer import ImageEvaluator

def collect_images():
    image_dir = "static/uploads/"
    if not os.path.exists(image_dir):
        return []
    return [os.path.join(image_dir, f) 
            for f in os.listdir(image_dir) 
            if f.lower().endswith(('png', 'jpg', 'jpeg'))]

def generate_report(results):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"report_{timestamp}.json"
    with open(filename, 'w') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    return filename

def main():
    project = input("请输入评估项目名称：")
    
    print("⏳ 正在爬取小红书数据...")
    notes = search_project(project)
    reviews = [n['content'] for n in notes[:15]]  # 取前15条
    
    print("🧠 进行文本分析...")
    text_eval = TextEvaluator()
    text_result = text_eval.analyze("\n".join(reviews))
    
    print("🖼️ 进行图像分析...")
    img_eval = ImageEvaluator()
    image_result = {}
    images = collect_images()
    if images:
        image_scores = [img_eval.analyze(img) for img in images]
        # 取各维度平均值
        keys = image_scores[0].keys()
        image_result = {
            k: round(sum(s[k] for s in image_scores)/len(image_scores), 1)
            for k in keys
        }
    
    final_result = {
        "project": project,
        "text_sources": len(reviews),
        "image_sources": len(images),
        "scores": {**text_result, **image_result}
    }
    
    report_file = generate_report(final_result)
    print(f"\n✅ 评估完成！报告已保存至 {report_file}")
    print(json.dumps(final_result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()