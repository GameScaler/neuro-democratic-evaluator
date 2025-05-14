import sys
import os
import json
from pathlib import Path

# 添加子模块路径
sys.path.append(str(Path(__file__).parent.parent / "media_crawler"))

from media_crawler.media_platform.xhs.core import XiaoHongShuCrawler
from media_crawler.media_platform.xhs import login

def search_project(keyword, max_notes=20):
    crawler = XiaoHongShuCrawler()
    
    cookie_path = Path("cookies.json")
    if not cookie_path.exists():
        print("请先执行登录流程：")
        login("xhs", cookies_save_path=str(cookie_path))
    
    try:
        results = crawler.search(
            keyword=keyword,
            page=1,
            limit=max_notes,
            sort_by='popularity',
            note_type='all'
        )
        return [{
            "content": note.desc,
            "likes": note.likes,
            "images": note.image_list
        } for note in results]
    except Exception as e:
        print(f"爬取失败：{str(e)}")
        return []