from algosdk.atomic_transaction_composer import AccountTransactionSigner
from contract import AccountStateExample
from beaker.client import ApplicationClient
from beaker.sandbox import get_client, get_accounts

accts = get_accounts()

acct, sk = accts[0]
signer = AccountTransactionSigner(sk)

client = get_client()

app = AccountStateExample()
app_client = ApplicationClient(client, app, signer=signer)
app_id, app_address, transaction_id = app_client.create()
print(
    f"DEPLOYED: App ID: {app_id} Address: {app_address} Transaction ID: {transaction_id}"
)

print(f"Opting in")
app_client.opt_in()

print("Setting value")
app_client.call(app.doit, note="yo", k=0, v="First item")

print("Getting value")
result = app_client.call(app.getit, k=0)
print(f"Result: {result.return_value}")

print(f"Current account state: {app_client.get_account_state(acct)}")
