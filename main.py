# coding=utf8
import os

from redis.sentinel import Sentinel
from tornado.httpclient import AsyncHTTPClient
import tornado.ioloop
import tornado.httpserver
import tornado.web
import yaml

from handlers.core import IndexHandelr, AjaxContractIdHandler, AjaxPartnerNoHandler, AjaxPhoneIdHandler, \
    AjaxPlatOfferIdHandler, AjaxFacevalueHandler, AjaxOrderIdHandler, AjaxEffectTypeHandler, AjaxRequestNoHandler, \
    AjaxTimeStampHandler
from handlers.core import RandNumberHandelr
from handlers.core import SendMsgHandler
from handlers.core import CallbackDownstreamHandler
from handlers.core import SendOrderHandler
from handlers.order import DataOrderHandler
from utils.phone import MobileClassifier


LOGO = r'''
   _____              .___     .__                    /\ ________
  /     \ _____     __| _/____ |__|___________       / / \_____  \
 /  \ /  \\__  \   / __ |/ __ \|  \_  __ \__  \     / /   /  ____/
/    Y    \/ __ \_/ /_/ \  ___/|  ||  | \// __ \_  / /   /       \
\____|__  (____  /\____ |\___  >__||__|  (____  / / /    \_______ \
        \/     \/      \/    \/               \/  \/             \/
A tributary of Amazon
(C) 2014, Quxun Network
'''


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/data/order", DataOrderHandler),

            (r"/data/index", IndexHandelr),
            (r"/rand_number", RandNumberHandelr),
            (r"/send_msg", SendMsgHandler),

            (r"/callback_down", CallbackDownstreamHandler),
            (r"/send_order", SendOrderHandler),

            (r"/ajax_contract_id", AjaxContractIdHandler),
            (r"/ajax_partner_no", AjaxPartnerNoHandler),
            (r"/ajax_phone_id", AjaxPhoneIdHandler),
            (r"/ajax_plat_offer_id", AjaxPlatOfferIdHandler),
            (r"/ajax_facevalue", AjaxFacevalueHandler),
            (r"/ajax_order_id", AjaxOrderIdHandler),
            (r"/ajax_effect_type", AjaxEffectTypeHandler),
            (r"/ajax_request_no", AjaxRequestNoHandler),
            (r"/ajax_timestamp", AjaxTimeStampHandler),


        ]

        settings = dict(
            cookie_secret='VoGTaZcHTAKHF7cIL1/ZxFQxfNT/jEPNrE6KtgBQgVg=',

            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
        )

        tornado.web.Application.__init__(self, handlers, **settings)

        self.config = yaml.load(open('config.yaml', 'r', encoding='utf8'))

        self.classifier = MobileClassifier()  # 判断手机归属地

        if os.path.exists('downstream.yaml'):
            cfg = yaml.load(open('downstream.yaml', 'r', encoding='utf8'))
            self.config['downstream'] = cfg.get('downstream')

        sentinels = [(c['ip'], c['port']) for c in self.config['cache']]
        self.sentinel = Sentinel(sentinels, socket_timeout=0.1, db=1, decode_responses=True)
        self.port = self.config['config']['port']
        self.ip = self.config['config']['ip']

if __name__ == "__main__":
    AsyncHTTPClient.configure(None, max_clients=200)
    print(LOGO)
    app = Application()
    print('http://{0}:{1}/data/index'.format(app.ip,app.port))
    http_server = tornado.httpserver.HTTPServer(app, xheaders=True)
    http_server.listen(app.port)
    tornado.ioloop.IOLoop.instance().start()
