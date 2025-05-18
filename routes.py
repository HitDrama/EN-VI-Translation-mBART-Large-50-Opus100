from flask import Blueprint
from controllers.translation_controller import dichenvi


deep_router=Blueprint("deep",__name__)

#định nghĩa router


deep_router.route("/dichenvi",methods=["GET","POST"])(dichenvi)

