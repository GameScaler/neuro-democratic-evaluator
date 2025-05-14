from PIL import Image, ImageFilter
import numpy as np
import cv2

class ImageEvaluator:
    def __init__(self):
        self.texture_weights = {
            'stone': 0.25,
            'wood': 0.18,
            'metal': 0.15,
            'glass': 0.12,
            'plant': 0.10
        }

    def _calculate_entropy(self, image):
        # 计算图像熵值表征纹理复杂度
        hist = cv2.calcHist([image], [0], None, [256], [0, 256])
        hist = hist / hist.sum()
        entropy = -np.sum(hist * np.log2(hist + 1e-7))
        return entropy

    def analyze(self, img_path):
        img = Image.open(img_path).convert('RGB')
        img_arr = np.array(img)
        
        # 空间褶皱度分析
        gray = cv2.cvtColor(img_arr, cv2.COLOR_RGB2GRAY)
        edges = cv2.Canny(gray, 50, 150)
        edge_density = edges.sum() / (img.size[0]*img.size[1])
        
        # 视觉余像分析
        hsv = cv2.cvtColor(img_arr, cv2.COLOR_RGB2HSV)
        light_variance = hsv[:,:,2].std()
        
        # 触觉民主性模拟
        texture_scores = {}
        for texture in self.texture_weights:
            texture_scores[texture] = np.random.rand()  
        
        tactile_score = sum([v*self.texture_weights[k] 
                           for k,v in texture_scores.items()])
        
        return {
            'spatial_fold': round(edge_density*10, 1),  # 0-5分
            'visual_afterimage': round(light_variance/30, 1),
            'tactile_democracy': round(tactile_score*5, 1)
        }