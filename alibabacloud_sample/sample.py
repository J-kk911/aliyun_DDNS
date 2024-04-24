# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import os
import sys

from json import load,loads
from urllib.request import urlopen

from typing import List

from alibabacloud_alidns20150109.client import Client as Alidns20150109Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_alidns20150109 import models as alidns_20150109_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_console.client import Client as ConsoleClient
from alibabacloud_tea_util.client import Client as UtilClient


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
            access_key_id: str,
            access_key_secret: str,
    ) -> Alidns20150109Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 必填，您的 AccessKey ID,
            access_key_id=access_key_id,
            # 必填，您的 AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # Endpoint 请参考 https://api.aliyun.com/product/Alidns
        config.endpoint = f'alidns.cn-hangzhou.aliyuncs.com'
        return Alidns20150109Client(config)

    @staticmethod
    def create_client_with_sts(
            access_key_id: str,
            access_key_secret: str,
            security_token: str,
    ) -> Alidns20150109Client:
        """
        使用STS鉴权方式初始化账号Client，推荐此方式。
        @param access_key_id:
        @param access_key_secret:
        @param security_token:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 必填，您的 AccessKey ID,
            access_key_id=access_key_id,
            # 必填，您的 AccessKey Secret,
            access_key_secret=access_key_secret,
            # 必填，您的 Security Token,
            security_token=security_token,
            # 必填，表明使用 STS 方式,
            type='sts'
        )
        # Endpoint 请参考 https://api.aliyun.com/product/Alidns
        config.endpoint = f'alidns.cn-hangzhou.aliyuncs.com'
        return Alidns20150109Client(config)

    @staticmethod
    def main(
            args: List[str],
    ) -> None:
        # 请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID 和 ALIBABA_CLOUD_ACCESS_KEY_SECRET。
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378659.html
        ip = load(urlopen('http://api.ipify.org/?format=json'))['ip']	
	# 记得写好
	#{
  	#	"access_key_id":"xxx",
  	#	"access_key_secret": "xxx",
  	#	"www_record_id":"123",
 	# 	"@_record_id":"123",
	#}	
	#
        f = open('key.json', 'r')
        content = f.read()
        key = loads(content)
        client = Sample.create_client(key['access_key_id'], key['access_key_secret'])
        update_domain_record_request_www = alidns_20150109_models.UpdateDomainRecordRequest(
            rr='www',
            type='A',
            record_id=key['www_record_id'],
            value=ip
        )
        update_domain_record_request_all = alidns_20150109_models.UpdateDomainRecordRequest(
            rr='@',
            type='A',
            record_id=key['@_record_id'],
            value=ip
        )
        runtime = util_models.RuntimeOptions()
        try:
            resp = client.update_domain_record_with_options(update_domain_record_request_www, runtime)
            ConsoleClient.log(UtilClient.to_jsonstring(resp))
            resp = client.update_domain_record_with_options(update_domain_record_request_all, runtime)
            ConsoleClient.log(UtilClient.to_jsonstring(resp))
            print("当前ip: " + ip + " ip更新成功!")
        except Exception as error:
            # 错误 message
            # print(error.message)
            # 诊断地址
            # print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)
            print("当前ip: " + ip + " ip已是最新!")


    @staticmethod
    async def main_async(
            args: List[str],
    ) -> None:
        # 请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID 和 ALIBABA_CLOUD_ACCESS_KEY_SECRET。
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378659.html
        client = Sample.create_client(os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'],
                                      os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET'])
        update_domain_record_request = alidns_20150109_models.UpdateDomainRecordRequest(
            rr='www',
            type='A',
            record_id='880079727840264192',
            value='59.61.100.135'
        )
        runtime = util_models.RuntimeOptions()
        try:
            resp = await client.update_domain_record_with_options_async(update_domain_record_request, runtime)
            ConsoleClient.log(UtilClient.to_jsonstring(resp))
        except Exception as error:
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)


if __name__ == '__main__':
    Sample.main(sys.argv[1:])
