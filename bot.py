import os, datetime, tempfile
import discord, gdown

TOKEN = os.environ["https://discord.com/api/webhooks/1435547750161973308/af3RL4kxXCGxfG4-jEYlAWMGC4Pdg8eVfiXylBA0JJQAaJeMuAhONOkrD9ag7pivRpHi"]
CHANNEL_ID = int(os.environ["1435554112912490598"])

def pick(lines):
    lines = [x.strip() for x in lines if x.strip() and not x.strip().startswith("#")]
    d = datetime.datetime.utcnow().date().toordinal()
    return lines[d % len(lines)]

async def main():
    with open("videos.txt", "r", encoding="utf-8") as f:
        url = pick(f.readlines())

    out = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    out.close()
    gdown.download(url, out.name, quiet=True, fuzzy=True)

    c = discord.Client(intents=discord.Intents.default())
    async with c:
        await c.login(TOKEN)
        ch = await c.fetch_channel(CHANNEL_ID)
        try:
            await ch.send(file=discord.File(out.name, filename="daily.mp4"))
        except:
            await ch.send(url)
        await c.close()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
