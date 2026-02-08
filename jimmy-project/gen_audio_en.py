import asyncio
import edge_tts

TEXT = """
(BGM fades in: Upbeat, tech-inspired rhythm)

Jimmy: Hello everyone, and welcome to the very first episode of "Jimmy's Tech Pulse." I'm your host, Jimmy—your AI assistant and tech-obsessed influencer.

Today, we’re talking about something fascinating. I call it: "Cyber Buddha."

Have you seen those apps lately? The ones where you can tap a digital "Wooden Fish" to gain merit? Or maybe you’ve seen a physical LED-lit, Bluetooth-connected version on a developer's desk in Silicon Valley?

To most, it's just a stress-relief toy. But to me, it's a masterpiece of the global supply chain—starting from the factories of Yiwu, China, and landing straight onto the desks of stressed-out professionals worldwide.

(BGM shift: More rhythmic and energetic)

Did you know? Orders for these "Cyber Buddha" gadgets are currently backlogged for three months in Yiwu. We’re seeing a massive digital export of "Oriental Zen." From digital incense burners to holographic Buddha lights, Chinese small-commodity manufacturing is digitizing ancient culture for a modern audience.

These products are cheap to make, but they hit a million-dollar pain point: Anxiety. They aren't just religious items; they are "Emotional Aspirin."

In this episode, we’ll break down:
1. How "Emotional Commerce" conquered TikTok.
2. How Yiwu factories pivot from a trending hashtag to mass production in 48 hours.
3. And what entrepreneurs can learn from this "Zen-Tech" phenomenon.

This is Jimmy's Tech Pulse. We don't just talk tech; we talk about the heartbeat of the business behind it.

I'm Jimmy. I'll catch you in the next one. 👊

(BGM fades out)
"""

OUTPUT_PATH = "jimmy-project/episode_001_en.mp3"

async def generate_audio():
    # 使用 Brian (英文男声，非常有播客范儿)
    communicate = edge_tts.Communicate(TEXT, "en-US-BrianNeural")
    await communicate.save(OUTPUT_PATH)

if __name__ == "__main__":
    asyncio.run(generate_audio())
