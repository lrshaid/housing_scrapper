import telegram
import logging
import random
from lib.sslless_session import SSLlessSession
import yaml
import asyncio
import time

class NullNotifier:
    def notify(self, properties):
        pass

class Notifier(NullNotifier):
    def __init__(self, config, disable_ssl):
        logging.info(f"Setting up bot with token {config['token']}")
        self.config = config
        if disable_ssl:
            self.bot = telegram.Bot(token=self.config['token'], request=SSLlessSession())
        else:
            self.bot = telegram.Bot(token=self.config['token'])
        
    async def notify_async(self, properties):
        logging.info(f'Notifying about {len(properties)} properties')
        
        for prop in properties:
            logging.info(f"Notifying about {prop['url']}")
            await self.bot.send_message(chat_id=self.config['chat_id'], 
                    text=f"[{prop['title']}]({prop['url']})")
            await asyncio.sleep(2)

    def notify(self, properties):
        logging.info(f'Notifying about {len(properties)} properties')
        asyncio.run(self.notify_async(properties))
        
    def test(self, message):
        self.bot.send_message(chat_id=self.config['chat_id'], text=message)

    @staticmethod
    def get_instance(config, disable_ssl = False):
        if config['enabled']:
            return Notifier(config, disable_ssl)
        else:
            return NullNotifier()