
import os


SECURITY_PROTOCOL="SASL_SSL"
SSL_MACHENISM="PLAIN"
API_KEY ="NJJR6YROP2BDV2JA" #os.getenv('API_KEY',None)
API_SECRET_KEY ="ny+XxbUdUGdkDQGFDcdUXI2Douj3foS6OPvmmffGCEQsx0V2du8sUx/GnFoYogyK" #os.getenv('API_SECRET_KEY',None)
BOOTSTRAP_SERVER ="pkc-xrnwx.asia-south2.gcp.confluent.cloud:9092" #os.getenv('BOOTSTRAP_SERVER',None)
#SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL',None)
#SSL_MACHENISM = os.getenv('SSL_MACHENISM',None)
ENDPOINT_SCHEMA_URL  ="https://psrc-7q7vj.ap-southeast-2.aws.confluent.cloud"
SCHEMA_REGISTRY_API_KEY ="BXESC56PPPIYXODR" #os.getenv('SCHEMA_REGISTRY_API_KEY',None)
SCHEMA_REGISTRY_API_SECRET ="VCsfOXFYqbJIBWOrDyxh9edUfBIn063h3WUKSYEKCLdp5n7teEiG/iCVLpQy3CMT" #os.getenv('SCHEMA_REGISTRY_API_SECRET',None)


def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    print(sasl_conf)
    return sasl_conf



def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }

if __name__ == '__main__':
    sasl_conf()

