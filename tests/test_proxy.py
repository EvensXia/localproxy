import os
import unittest

from localproxy.proxy import ProxyConfig, init


class TestProxyConfig(unittest.TestCase):
    def setUp(self):
        self.config_file = "/tmp/test_proxy.toml"
        self.proxy_config = ProxyConfig(self.config_file)

    def tearDown(self):
        if os.path.exists(self.config_file):
            os.remove(self.config_file)

    def test_load_empty_config(self):
        proxies = self.proxy_config.load()
        self.assertEqual(proxies, {})

    def test_save_and_load_config(self):
        proxies = {
            "http": "http://localhost:8080",
            "https": "https://localhost:8443"}
        self.proxy_config.save(proxies)
        loaded_proxies = self.proxy_config.load()
        self.assertEqual(loaded_proxies, proxies)

    def test_init(self):
        proxies = {"http": "http://localhost:8080"}
        self.proxy_config.save(proxies)
        init()
        self.assertEqual(os.environ["http_proxy"], "http://localhost:8080")


if __name__ == '__main__':
    unittest.main()
