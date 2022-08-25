
import json
import traceback
from channels.generic.websocket import WebsocketConsumer

class EchoConsumer(WebsocketConsumer):
    
    def close(self, code=None):
        print('[WS INFO] close function')
        return super().close(code)

    def accept(self, subprotocol=None):
        print('[WS INFO] accept function')
        return super().accept(subprotocol)

    def websocket_connect(self, message):
        print('[WS INFO] websocket connect function')
        return super().websocket_connect(message)
    
    def websocket_disconnect(self, message):
        print('[WS INFO] websocket disconnect function')
        return super().websocket_disconnect(message)
    
    def websocket_receive(self, message):
        print(f'[WS INFO] websocket receive function, message:{message}')
        return super().websocket_receive(message)


    def connect(self):
        print (f"[WS INFO] connection opened")
        return self.accept()
    
    """
    '__call__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
     '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
     '__str__', '__subclasshook__', '__weakref__', '_sync',
    
      'accept', 'as_asgi', 'channel_layer_alias', 'close', 'connect', 'disconnect', 'dispatch', 'groups', 'receive', 'send', 'websocket_connect', 'websocket_disconnect', 'websocket_receive']
    """

    def disconnect(self, code):
        print (f"[WS INFO] connection closed, code: {code}")

    def receive(self, text_data):
        try:
            self.send(text_data=json.dumps({
                'message':json.loads(text_data),
                'add data': self.dispatch
            }))
        except json.JSONDecodeError as e:
            self.send(text_data=json.dumps({
                'error': "JSONDecodeError",
                'error detail':str(e)
            }))
        except Exception as e:
            self.send(text_data=json.dumps({
                'error': str(type(e)),
                'error detail':str(e),
                'traceback' : traceback.format_exc()
            }))
            raise e