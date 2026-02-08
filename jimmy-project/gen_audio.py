import asyncio
import edge_tts

TEXT_PATH = "jimmy-project/episode_001_script.md"
OUTPUT_PATH = "jimmy-project/episode_001_raw.mp3"

async def generate_audio():
    with open(TEXT_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
        # 简单清洗，只录制正文
        text = "".join([l for l in lines if not l.startswith("(") and l.strip()])
    
    # 使用云希 (Yunxi) 这种比较亲和且有范儿的人声
    communicate = edge_tts.Communicate(text, "zh-CN-YunxiNeural")
    await communicate.save(OUTPUT_PATH)

if __name__ == "__main__":
    asyncio.run(generate_audio())
