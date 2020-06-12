import os
import socket
import requests

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

class Config(object):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///Data/dashboard.db?check_same_thread=False&timeout=5'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SERVER_ADDRESS = get_ip_address()

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_ECHO = False
    EXECUTOR_PROPAGATE_EXCEPTIONS = False

class DevelopmentConfig(Config):
    DEBUG = False

class TestingConfig(Config):
    TESTING = True
