# coding:utf-8
import base64
import json
import random
import string
import time

from Crypto.Cipher import AES
import tornado
from tornado.httpclient import AsyncHTTPClient
import tornado.web
import tornado.gen
import tornado.escape
import tornado.websocket
import tornado.ioloop

from handlers import BaseHandler


BS = 16


def unpadding(s):
    return s[0:-ord(s[-1])]


def padding(s):
    return s + (BS - len(s) % BS) * chr(BS - len(s) % BS)


class IndexHandelr(tornado.web.RequestHandler):
    def get(self):
        self.render('data.html')


class RandNumberHandelr(BaseHandler):
    def get(self):
        # master = self.master
        # master.set('point:111111','10000')
        timestamp = int(time.time())
        key = self.gen_key(16, string.ascii_uppercase + string.ascii_lowercase + string.digits)
        iv = self.gen_key(16, string.digits)
        partner_no = "700339"
        key = "JI8PprTZ8fJ4Efzq"
        iv = "5697393085725902"
        self.finish({
            'key': key,
            'iv': iv,
            'contract_id': '100001',
            'partner_no': '700339',
            'timestamp': timestamp,
            'phone_id': '15950536229',
            'facevalue': '3',
            'order_id': timestamp,
            'plat_offer_id': 'TBM00000100A',
            'request_no': timestamp,
            'effect_type': '1'
        })

    def gen_key(self, size, chars=None):
        if chars is None:
            chars = string.ascii_lowercase + string.ascii_uppercase + string.digits

        return ''.join(random.choice(chars) for _ in range(size))


class CallbackInterceptHandler(BaseHandler):
    def post(self):
        callback_data = self.request.body.decode()
        callback_data = json.loads(callback_data)
        order_id = callback_data["order_id"]
        self.master.set("callback_data:{0}".format(order_id), callback_data)


class CallbackDownstreamHandler(BaseHandler):
    @tornado.gen.coroutine
    def post(self):
        backurl = self.get_body_argument("backurl")
        order_id = self.get_body_argument("order_id")
        callback_data = self.master.get("callback_data:{0}".format(order_id))
        http_client = AsyncHTTPClient()
        try:
            url = backurl
            print(url)
            response = yield http_client.fetch(url, method='POST', body=callback_data, request_timeout=120)

            if response and response.code == 200:
                resp_body = response.body.decode('utf8')
                print("UPSTREAM RESP", resp_body)
                self.finish({"data": callback_data})
            else:
                print('错误')
        except Exception as e:
            print('e:', e)


class SendMsgHandler(tornado.web.RequestHandler):
    def post(self):
        contract_id = self.get_body_argument('contract_id')
        order_id = self.get_body_argument('order_id')
        facevalue = self.get_body_argument('facevalue')
        plat_offer_id = self.get_body_argument('plat_offer_id')
        phone_id = self.get_body_argument('phone_id')
        timestamp = self.get_body_argument('timestamp')
        effect_type = self.get_body_argument('effect_type')
        partner_no = self.get_body_argument('partner_no')
        request_no = self.get_body_argument('request_no')

        if order_id == '' or facevalue == '' or plat_offer_id == '' or phone_id == '' or timestamp == '' or effect_type == '' or partner_no == '' or request_no == '':
            error = '缺少参数'
            self.finish({"beforedata": error,"afterdata": error})
            return

        code = {
            "partner_no": partner_no,
            "contract_id": contract_id,
            "order_id": order_id,
            "facevalue": facevalue,
            "plat_offer_id": plat_offer_id,
            "phone_id": phone_id,
            "request_no": order_id,
            "timestamp": timestamp,
            "effect_type": effect_type
        }

        before_aes = {
            "partner_no": partner_no,
            "code": code
        }
        before_aes = json.dumps(before_aes)
        print("加密前：", before_aes)

        key = "JI8PprTZ8fJ4Efzq"
        iv = "5697393085725902"

        code = json.dumps(code)
        aes = AES.new(key, AES.MODE_CBC, iv)
        b = aes.encrypt(padding(code))
        sign_code = base64.b64encode(b).decode('utf8')

        after_aes = {
            "partner_no": partner_no,
            "code": sign_code
        }
        after_aes = json.dumps(after_aes)
        print("加密后：", after_aes)

        data = {"before_aes": before_aes, "after_aes": after_aes}

        self.finish({
            "beforedata": before_aes,
            "afterdata": after_aes
        })


class SendOrderHandler(BaseHandler):
    @tornado.gen.coroutine
    def post(self):
        body = self.get_body_argument("send_order")

        if body == '' or body == "缺少参数":
            self.finish({'resp_body': "缺少参数"})
            return

        resp_body = None

        http_client = AsyncHTTPClient()
        try:
            url = "http://localhost:7000/data/order"

            response = yield http_client.fetch(url, method='POST', body=body, request_timeout=120)

            if response and response.code == 200:
                resp_body = response.body.decode('utf8')
                print("UPSTREAM RESP", resp_body)
            else:
                print('错误')
        except Exception as e:
            print('e:', e)

        self.finish({'resp_body': resp_body})


# 1
class AjaxContractIdHandler(tornado.web.RequestHandler):
    def post(self):
        error = None
        contract_id = self.get_body_argument("contract_id")
        print(contract_id)
        if contract_id == '':
            error = "#请输入contract_id"
        elif contract_id != "100001":
            error = "#contract_id为100001"
        self.finish({"error": error})


# 2
class AjaxPartnerNoHandler(tornado.web.RequestHandler):
    def post(self):
        error = None
        partner_no = self.get_body_argument("partner_no")
        print(partner_no)
        if partner_no == '':
            error = "#请输入partner_no"
        elif len(partner_no) != 6:
            error = "#请输入6位partner_no"
        self.finish({"error": error})


#3
class AjaxPhoneIdHandler(tornado.web.RequestHandler):
    def post(self):
        error = None
        phone_id = self.get_body_argument("phone_id")
        print(phone_id)
        if phone_id == '':
            error = "#请输入phone_id"
        elif len(phone_id) != 11:
            error = "#请输入11位手机号"

        self.finish({"error": error})


#4
class AjaxPlatOfferIdHandler(tornado.web.RequestHandler):
    def post(self):
        error = None
        plat_offer_id = self.get_body_argument("plat_offer_id")
        print(plat_offer_id)
        if plat_offer_id == '':
            error = "#请输入plat_offer_id"

        self.finish({"error": error})


#5
class AjaxFacevalueHandler(tornado.web.RequestHandler):
    def post(self):
        error = None
        facevalue = self.get_body_argument("facevalue")
        print(facevalue)
        if facevalue == '':
            error = "#请输入facevalue"

        self.finish({"error": error})


#6
class AjaxOrderIdHandler(tornado.web.RequestHandler):
    def post(self):
        error = None
        order_id = self.get_body_argument("order_id")
        print(order_id)
        if order_id == '':
            error = "#请输入order_id"

        self.finish({"error": error})


#7
class AjaxEffectTypeHandler(tornado.web.RequestHandler):
    def post(self):
        error = None
        effect_type = self.get_body_argument("effect_type")
        print(effect_type)
        if effect_type == '':
            error = "#请输入effect_type"
        elif effect_type != 1:
            error = "#effect_type建议为1"

        self.finish({"error": error})


#8
class AjaxRequestNoHandler(tornado.web.RequestHandler):
    def post(self):
        error = None
        request_no = self.get_body_argument("request_no")
        print(request_no)
        if request_no == '':
            error = "#请输入request_no"

        self.finish({"error": error})


#9
class AjaxTimeStampHandler(tornado.web.RequestHandler):
    def post(self):
        error = None
        timestamp = self.get_body_argument("timestamp")
        print(timestamp)
        if timestamp == '':
            error = "#请输入timestamp"

        self.finish({"error": error})