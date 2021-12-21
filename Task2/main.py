import json

with open('arangodb.txt') as json_file:
    data = json.load(json_file)
    if data['serviceModel']['serviceSpecification']['name'] == 'otn-trunk-cfs':
        for dcs in data['serviceModel']['serviceCharacteristic'][1]['value']['e2e-client-service']['domain-client-service']:
            if dcs['domain'] == 'Ciena':
                print(
                    "".join(
                        [
                            dcs.get(key, f"\n{key} not found!") for key in [
                                "lbz",
                                "rfs-id",
                                "operational-state",
                                "user-label",
                                "ololo",
                                "dfhjsfrtjsrt",
                                "dfghjfgj",
                                "rtjrtjrtj",
                        ]
                        ]
                    )
                )
