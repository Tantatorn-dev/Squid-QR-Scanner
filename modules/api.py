import requests

url = "http://api-avehwzgofa-an.a.run.app/tickets/"

def update_ticket(ticket_id):
    req = requests.post(url+ticket_id ,json={"status":"checked"})
    print(req.status_code)
