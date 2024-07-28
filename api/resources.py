from flask_restful import Resource, Api
from flask import jsonify
from .models import PacketData

api = Api()

class PacketListResource(Resource):
    def get(self):
        packets = PacketData.query.all()
        return jsonify([packet.to_dict() for packet in packets])

api.add_resource(PacketListResource, '/packets')
