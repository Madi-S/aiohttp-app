import argparse
import aiohttp
import asyncio
from demo import create_app
from demo.settings import load_config


try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    print('Library uvloop cannot be imported')

parser = argparse.ArgumentParser(description='Demo project')
parser.add_argument('--host',
                    help='Host to listen', default='0.0.0.0')
parser.add_argument('-p', '--port',
                    help='Port to accept connections', type=int, default=5002)
parser.add_argument('-r', '--reload',
                    action='store_true', help='Autoreload code on change')
parser.add_argument('-c', '--config',
                    help='Path to configuration file', type=argparse.FileType('r'))

args = parser.parse_args()

app = create_app(load_config(args.config))

if args.reload:
    import aioreloader
    print('Start with code reload')
    aioreloader.start()

if __name__ == '__main__':
    aiohttp.web.run_app(app, host=args.host, port=args.port)
