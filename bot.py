import discord
import requests
import os
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
load_dotenv()

# 创建 Intents 对象
intents = discord.Intents.all()

# 使用 intents 实例化 Client
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.guild.name == 'wang2gou server':
        print(f'on_message: {message}')
        # 调用 n8n webhook
        webhook_url = os.getenv('WEBHOOK_URL')
        data = {'id': message.id, 'channelId': message.channel.id, 'serverId': message.guild.id}
        response = requests.get(webhook_url, params=data)
        print(response)

# 从环境变量中获取 Bot Token 并运行客户端
client.run(os.getenv('DISCORD_BOT_TOKEN'))