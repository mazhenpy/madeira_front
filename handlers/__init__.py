import time

import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request)
        self._master = None
        self._slave = None

    @property
    def classifier(self):
        return self.application.classifier

    @property
    def master(self):
        if self._master is None:
            self._master = self.application.sentinel.master_for('madeira')
        return self._master

    @property
    def slave(self):
        if self._slave is None:
            self._slave = self.application.sentinel.slave_for('madeira')
        return self._slave


class CoreHandler(BaseHandler):
    def __init__(self, application, request, **kwargs):
        super(CoreHandler, self).__init__(application, request)

        # from downstream
        self.order_id = None
        self.user_id = None
        self.price = 0
        self.mobile = None
        self.sp_order_id = None
        self.back_url = None
        self.balance = 0
        self.product = None  # new
        # from upstream
        self.up_order_id = None
        self.up_cost = 0
        # processing
        self.value = 0
        self.route = None
        self.cost = 0
        self.carrier = None
        self.area = None
        # result
        self.result = None
        self.up_result = None
        # timestamp
        self.req_time = time.localtime()
        # self.resp_time = None
        self.up_req_time = None
        self.up_resp_time = None
        # data order
        self.plat_offer_id = None
        self.up_back_result = None
        self.effect_type = None
        self.master_id = None
        self.scope = None