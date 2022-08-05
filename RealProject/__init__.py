import os
from RealProject.settings import BASE_DIR
from flask import Flask

def create_app(test_config=None):
    # instance_relative_config设置为True则代表开启从文件加载配置，默认为False
    app = Flask(__name__, instance_relative_config=True)
    # app.config其实调用的是f1ask类的config属性，该属性又被设置为了一个Config的类
    # from_mapping则是该Config类下的一个方法，用来更新默认配置，返回值为True
    ## 至于F1ask的默认配置项都有哪些，其实可以深入源码查看default_config.属性所列出的项
    # 默认配置
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    # 判断运行时是否传入测试配置
    if test_config == None:
        # 如果没有传入，则从py文件加戟配置，si1ent=True代表文件，文件加载成功则返回True
        CONFGI_PATH = BASE_DIR / 'RealProject.settings.py'
        app.config.from_pyfile(CONFGI_PATH, silent=True)
    else:
        # 和最开始的配置意思一致
        app.config.from_mapping(test_config)

    #递归创建目录，确保项目文件存在
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    # 引入blog视图文件
    from app.blog import views as blog
    app.register_blueprint(blog.bp)

    # 注册数据库
    # from app.blog import models

    return app
# app = Flask(__name__)

