# %%
import json
from jsf import JSF
import random
import os


def generate_save_fake_json(faker: JSF, contract_id: int, output_filename: str):
    """
    Function specific to the json schema of the example message.

    Args:
        faker (JSF): fake json generator object
        contract_id (int): contract id to be added to the json message
        output_filename (str): file name of output json file
    """

    test_message = faker.generate()
    # Make sure we have have groups of the same contract number
    test_message["boeking_referentie"]["eb_sleutel"]["contractnummer"] = contract_id

    with open(f"{output_filename}.json", "w") as json_file:
        json.dump(test_message, json_file)


# Generate 100 contract ids
N_contracts = 100
N_messages_per_contract = 100
contract_ids = random.sample(range(10000000, 99999999), N_contracts)

# File path to save messages
os.chdir("Test_JSON_Messages")

# I obtained the schema by using the supplied example message and this website:
# https://www.jsonschema.net/
f = open("example_transaction.schema.json")
schema = json.load(f)

# Initialise fake JSON generator from json schema
# Based on this repo: https://github.com/ghandic/jsf
faker = JSF.from_json("example_transaction.schema.json")

for contract_id in contract_ids:
    for message_number in range(0, N_messages_per_contract):
        output_filename = f"contract_id_{contract_id}_message_id{message_number}"
        generate_save_fake_json(faker, contract_id, output_filename)
# %%
