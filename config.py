import os


class Config:
    # 设置一个随机的SECRET_KEY值
    SECRET_KEY = os.urandom(24)
    # 指定信号追踪
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 指定执行完增删改之后的自动提交
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        '''初始化配置文件'''
        pass


# the config for development
class DevelopmentConfig(Config):
    # 连接接数据库
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/flask_restful_demo'
    # 指定程序的启动模式为调试模式
    DEBUG = True


# defing the config
config = {
    'default': DevelopmentConfig
}
